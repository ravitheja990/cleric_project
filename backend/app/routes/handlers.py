import requests
from uuid import uuid4
from ..models import DocumentRequest, FactsResponse
from threading import Thread
import logging

# Configure logging to display messages of level INFO and above
logging.basicConfig(level=logging.INFO)

sessions = {}

def process_documents(request: DocumentRequest):
    session_id = str(uuid4())
    # Initialize the session
    sessions[session_id] = {
        "question": request.question,
        "facts": [],
        "status": "processing"
    }
    # Start the document processing in a new thread to avoid blocking
    thread = Thread(target=process_documents_background, args=(session_id, request.documents))
    thread.start()
    return session_id

def process_documents_background(session_id, document_urls):
    try:
        facts = []
        # Iterate over each document URL
        for url in document_urls:
            text = fetch_document(url)
            print("text is :: ", text)
            extracted_facts = extract_facts_from_text(text)
            print("extracted_facts is :: ", extracted_facts)
            facts.extend(extracted_facts)  # Extend the list of facts with new findings

        # Update the session with the new facts, mark as done
        sessions[session_id]["facts"] = facts
        sessions[session_id]["status"] = "done"
    except Exception as e:
        # Handle exceptions, mark as error
        sessions[session_id]["status"] = "error"
        sessions[session_id]["error"] = str(e)

def fetch_document(url):
    response = requests.get(url)
    response.raise_for_status()  # Will raise an HTTPError for bad responses
    return response.text

import re
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_facts_from_text(text):
    # Combining both regex and NLP extraction results
    facts = set()  # Using a set to avoid duplicates

    # Regex-based extraction
    facts.update(regex_based_extraction(text))
    
    # NLP-based extraction
    facts.update(nlp_based_extraction(text))
    
    return list(facts)

def regex_based_extraction(text):
    # Patterns to identify decision-making and planning phrases
    patterns = [
        r"\b\w+ will \w+ \w+",  # Simple future decisions
        r"\b\w+ will be \w+ing \w+",  # Future continuous decisions
        r"\bwe have decided to \w+ \w+",  # Concluded decisions
        r"\bwe are planning to \w+ \w+",  # Future plans
        r"\bwe plan to \w+ \w+",  # Alternative to planning
        r"\bwe will \w+ \w+ \w+",  # Explicit future decision
        r"\bit is agreed that \w+ \w+",  # Agreements in meetings
        r"\bdecision to \w+ \w+",  # Direct mention of a decision
        r"\b\w+ has been approved to \w+",  # Approval statements
        r"\b\w+ has been authorized to \w+",  # Authorization statements
        r"\bwe aim to \w+ \w+",  # Statements of intent
        r"\bwe intend to \w+ \w+",  # Stronger statements of intent
        r"\bwe expect to \w+ \w+",  # Expectations
        r"\bwe must \w+ \w+",  # Obligations or requirements
        r"\b\w+ should \w+ \w+",  # Recommendations or advice
        r"\b\w+ could \w+ \w+",  # Possibilities
        r"\b\w+ might \w+ \w+",  # Possibilities with less certainty
        r"\bwe agreed on \w+ing \w+",  # Agreements on specific actions
        r"\bwe committed to \w+ing \w+",  # Commitments made
        r"\baction to \w+ \w+ \w+",  # Specific actions to be taken
        r"\bstrategic priority to \w+ \w+",  # Strategic moves
        r"\binitiative to \w+ \w+",  # Initiatives being launched
        r"\bmeasures to \w+ \w+",  # Measures or steps to be implemented
        r"\bresolve to \w+ \w+",  # Resolutions made in meetings
        r"\bobjectives include \w+ing \w+",  # Stated objectives
        r"\b\w+ was tasked with \w+ing \w+",  # Assignments of responsibility
        r"\b\w+ is responsible for \w+ing \w+",  # Delegation of duties
        r"\bfocus on \w+ing \w+",  # Focus areas identified
        r"\bkey focus will be on \w+ing \w+",  # Key strategic focuses
        r"\bpriority will be given to \w+ing \w+",  # Prioritization statements
        r"\b\w+ must ensure \w+ \w+"  # Obligatory measures
    ]

    all_matches = set()
    for pattern in patterns:
        regex = re.compile(pattern)
        matches = regex.findall(text)
        all_matches.update(matches)
    return all_matches

def nlp_based_extraction(text):
    doc = nlp(text)
    facts = set()
    # Iterating over sentences in the text
    for sent in doc.sents:
        # Check for modal verbs and decision-related keywords
        if 'will' in sent.text or 'decide' in sent.text or 'plan' in sent.text:
            facts.add(sent.text.strip())
    return facts