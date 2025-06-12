## Threat Detection AI Simulation

A fullstack cyber intrusion detection simulation built to demonstrate AI/ML modeling, secure system logic, and real-time intelligence dashboarding. Designed to emulate key competencies sought by defense contractors like Lockheed Martin Australia.

## Project Summary

This project is a beginner-friendly, fullstack cyber-AI simulator
Used to detect suspicious behavior in simulated logs
Powered by: React + Flask + PyTorch

This app mimics a simplified cyber battlefield:  
- Simulated network telemetry is fed to a backend AI model  
- A PyTorch classifier determines if it's **normal** or **anomalous behavior**  
- A Flask API processes requests and returns threat predictions  
- A React dashboard interfaces with the model in real time

##  Tech Stack

| Layer       | Tech                          |
|-------------|-------------------------------|
| AI Model    | Python, PyTorch               |
| API Server  | Flask (w/ Flask-CORS)         |
| Frontend    | React + Axios + Chart.js      |
| Language    | JavaScript / Python           |
| Training    | Manual, synthetic log data    |
| Deployment  | Localhost (dev)               |

##  Features

-  PyTorch AI model trained on mini-CIC-style threat data  
- 🛰 Flask REST API: `POST /api/predict`  
-  React UI with modern styling and input controls  
-  Real-time classification + confidence levels  
-  Adversarial input ready (expandable to red team data)  
-  Modular, beginner-friendly fullstack codebase  

##  Quickstart

```bash
git clone https://github.com/yourusername/threat-detection-ai-sim.git
cd threat-detection-ai-sim

Backend (Python + PyTorch)

cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python model/train_model.py
python app.py

 Frontend (React)
 cd ../frontend
npm install
npm start

 Example API Payload
 {
  "duration": 0,
  "src_bytes": 146,
  "dst_bytes": 0,
  "flag": 3,
  "protocol_type": 1
}

Response:
{
  "prediction": "anomaly",
  "confidence": [0.12, 0.88]
}
