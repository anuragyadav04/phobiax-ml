import pandas as pd
##from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
df = pd.read_csv("data.csv")

# Check for NaN values
if df.isnull().values.any():
    print("⚠️ NaN values found — cleaning...")
    df = df.dropna()  # OR: df = df.fillna(0)


X = df.drop("Label", axis=1)
y = df["Label"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
print(X.head())
print(y.head())
print(X.isnull().sum())
print(y.isnull().sum())

model.fit(X_train, y_train)

# Test Accuracy
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save model
with open("phobia_model.pkl", "wb") as f:
    pickle.dump(model, f)
