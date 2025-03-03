import React, { useState } from 'react';

function Quiz() {
  const [answers, setAnswers] = useState([]);

  const handleSubmit = () => {
    // Submit answers to backend
    fetch('/assess', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ student_id: '123', responses: answers })
    });
  };

  return (
    <div>
      <h2>Quiz</h2>
      <input type="text" onChange={(e) => setAnswers([...answers, e.target.value])} />
      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
}

export default Quiz;