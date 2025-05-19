import React, { useState } from 'react';
import ThreatForm from './components/ThreatForm';
import ThreatDisplay from './components/ThreatDisplay';
import './styles/App.css';

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="App">
      <h1>🛰️ Cyber Threat Detection Dashboard</h1>
      <ThreatForm onResult={setResult} />
      <ThreatDisplay result={result} />
    </div>
  );
}

export default App;
