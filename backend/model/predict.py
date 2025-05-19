import torch
import torch.nn as nn
import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'threat_model.pt')
FEATURES_PATH = os.path.join(BASE_DIR, 'model', 'features.pkl')

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(5, 16)
        self.fc2 = nn.Linear(16, 8)
        self.out = nn.Linear(8, 2)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.out(x)

model = Net()
model.load_state_dict(torch.load(MODEL_PATH))
model.eval()

features = joblib.load(FEATURES_PATH)

def predict_threat(input_data: dict):
    try:
        values = [input_data[feat] for feat in features]
        input_tensor = torch.tensor([values]).float()
        with torch.no_grad():
            output = model(input_tensor)
            predicted = torch.argmax(output, dim=1).item()
        return {
            "prediction": "anomaly" if predicted == 1 else "normal",
            "confidence": torch.softmax(output, dim=1).tolist()[0]
        }
    except Exception as e:
        return {"error": str(e)}
