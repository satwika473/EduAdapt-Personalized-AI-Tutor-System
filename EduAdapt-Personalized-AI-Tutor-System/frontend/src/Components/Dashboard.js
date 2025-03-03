import React from 'react';

function Dashboard({ progress }) {
  return (
    <div>
      <h1>Welcome to EduAdapt</h1>
      <p>Your Learning Level: {progress.learning_level}</p>
      <p>Recommended Modules: {progress.recommended_modules?.join(', ')}</p>
    </div>
  );
}

export default Dashboard;