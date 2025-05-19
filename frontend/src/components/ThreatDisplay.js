import React from 'react';
import './ThreatDisplay.css';

export default function ThreatDisplay({ result }) {
  if (!result) return null;
  if (result.error) return <div className="error">❌ Error: {result.error}</div>;

  return (
    <div className="result-box">
      <h2>🧠 Threat Analysis Result</h2>
      <p><strong>Prediction:</strong> {result.prediction.toUpperCase()}</p>
      <p><strong>Confidence:</strong> {result.confidence.map((c, i) => (
        <span key={i}>Class {i}: {(c * 100).toFixed(2)}% </span>
      ))}</p>
    </div>
  );
}
