import pandas as pd
import torch
from torch import nn
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib
import os

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'cic_mini.csv')
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'threat_model.pt')
FEATURES_PATH = os.path.join(BASE_DIR, 'model', 'features.pkl')

# Load + preprocess
df = pd.read_csv(DATA_PATH)
df['label'] = LabelEncoder().fit_transform(df['label'])
df['protocol_type'] = LabelEncoder().fit_transform(df['protocol_type'])
df['flag'] = LabelEncoder().fit_transform(df['flag'])

X = df.drop('label', axis=1).values
y = df['label'].values

X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2)

X_train = torch.tensor(X_train).float()
y_train = torch.tensor(y_train).long()

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(X_train.shape[1], 16)
        self.fc2 = nn.Linear(16, 8)
        self.out = nn.Linear(8, 2)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.out(x)

model = Net()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()
    if epoch % 10 == 0:
        print(f"Epoch {epoch} Loss: {loss.item()}")

torch.save(model.state_dict(), MODEL_PATH)
joblib.dump(df.columns.drop('label'), FEATURES_PATH)
