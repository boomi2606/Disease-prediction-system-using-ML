import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load Dataset
df = pd.read_csv("dataset/disease_dataset.csv")

# Features and Target
X = df.drop("Disease", axis=1)
y = df["Disease"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Random Forest Model
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=15,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(f"{accuracy*100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save Model
joblib.dump(model, "model/disease_model.pkl")

# Save Feature Names
joblib.dump(list(X.columns), "model/feature_names.pkl")

print("\nModel Saved Successfully")