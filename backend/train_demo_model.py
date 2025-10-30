from sklearn.ensemble import RandomForestClassifier
import numpy as np
import joblib
import os

# Synthetic data
X = np.random.rand(100, 2) * [100, 40]  # soil_moisture, temp
y = ["Water" if x[0] < 30 else "Hot" if x[1] > 35 else "Normal" for x in X]

clf = RandomForestClassifier()
clf.fit(X, y)

os.makedirs("backend/models", exist_ok=True)
joblib.dump(clf, "backend/models/demo_model.joblib")
print("✅ Demo AI model saved.")
