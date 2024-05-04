import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [question, setQuestion] = useState('');
  const [documents, setDocuments] = useState('');
  const [facts, setFacts] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    const docs = documents.split('\n').filter(doc => doc.trim() !== '');
    try {
      const { data: sessionId } = await axios.post('http://localhost:8000/submit_question_and_documents', { question, documents: docs });
      const res = await axios.get(`http://localhost:8000/get_question_and_facts/${sessionId}`);
      setFacts(res.data.facts);
    } catch (error) {
      console.error('Error fetching facts:', error);
    }
    setLoading(false);
  };

  return (
    <div className="App">
      <h1>Cleric Project - Document Processor</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Question:
          <input type="text" value={question} onChange={e => setQuestion(e.target.value)} required />
        </label>
        <label>
          Document URLs (one per line):
          <textarea value={documents} onChange={e => setDocuments(e.target.value)} required />
        </label>
        <button type="submit" disabled={loading}>Submit</button>
      </form>
      {loading ? <p>Loading...</p> : <ul>{facts.map((fact, index) => <li key={index}>{fact}</li>)}</ul>}
    </div>
  );
}

export default App;

