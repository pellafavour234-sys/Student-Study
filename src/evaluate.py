import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

#Load the dataset
data = pd.read_csv("data/students.csv")

# Select features
X = data[
    [
        "study_hours",
        "attendance",
        "previous_score",
        "assignments_completed",
        "sleep_hours"
    ]
]


# Select target
y = data["final_score"]


# Split the data in the same way as train.py
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Load the trained model
forest_model = joblib.load(
    "models/student_performance_model.pkl"
)

# Make prediction
predictions = forest_model.predict(X_test)

#Calculate MAE
mae = mean_absolute_error(
    y_test,
    predictions
)

#Calculate MSE
mse = mean_squared_error(
    y_test,
    predictions
)

# Calculate R2
r2 = r2_score(
    y_test,
    predictions
)

print("MAE:", mae)
print("MSE:", mse)
print("R²:", r2)