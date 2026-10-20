import pandas as pd
import joblib


# Load the trained model
model = joblib.load(
    "models/student_performance_model.pkl"
)


# Information about a new student
student = pd.DataFrame({
    "study_hours": [1],
    "attendance": [40],
    "previous_score": [50],
    "assignments_completed": [2],
    "sleep_hours": [10]
})


# Make prediction
prediction = model.predict(student)


print(
    "Predicted Score:",
    prediction[0]
)