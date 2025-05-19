import React, { useState } from 'react';
import { sendThreatRequest } from '../api/threatAPI';
import './ThreatForm.css';

const defaultInput = {
  duration: 0,
  src_bytes: 146,
  dst_bytes: 0,
  flag: 3,
  protocol_type: 1
};

export default function ThreatForm({ onResult }) {
  const [input, setInput] = useState(defaultInput);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setInput((prev) => ({ ...prev, [name]: Number(value) }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const result = await sendThreatRequest(input);
    onResult(result);
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>🚨 Threat Detection Input</h2>
      {Object.entries(input).map(([key, val]) => (
        <div key={key}>
          <label>{key}: </label>
          <input type="number" name={key} value={val} onChange={handleChange} />
        </div>
      ))}
      <button type="submit">Analyze</button>
    </form>
  );
}
