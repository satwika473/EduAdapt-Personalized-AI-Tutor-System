import React, { useState, useEffect } from 'react';
import Dashboard from './Components/Dashboard';
import Quiz from './Components/Quiz';
import ProgressTracker from './components/ProgressTracker';

function App() {
  const [studentProgress, setStudentProgress] = useState({});

  useEffect(() => {
    // Fetch student progress from backend
    fetch('/assess', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ student_id: '123', responses: [] })
    })
    .then(response => response.json())
    .then(data => setStudentProgress(data));
  }, []);

  return (
    <div className="App">
      <Dashboard progress={studentProgress} />
      <Quiz />
      <ProgressTracker />
    </div>
  );
}

export default App;