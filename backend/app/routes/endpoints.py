from fastapi import APIRouter, HTTPException
from ..models import DocumentRequest, FactsResponse
from .handlers import process_documents, sessions

router = APIRouter()

@router.post("/submit_question_and_documents", response_model=str)
async def submit_question_and_documents(request: DocumentRequest):
    print(":: inside submit_question_and_documents :: request is ::", request)
    session_id = process_documents(request)
    return session_id

@router.get("/get_question_and_facts/{session_id}", response_model=FactsResponse)
async def get_question_and_facts(session_id: str):
    print(":: sessions is :: ", sessions)
    if session_id in sessions:
        return sessions[session_id]
    raise HTTPException(status_code=404, detail="Session not found")

