import os
import joblib
import numpy as np


MODEL_PATH = os.path.join(
    "models",
    "student_performance_model.pkl"
)


FEATURES = [
    "study_hours",
    "attendance",
    "previous_score",
    "assignments_completed",
    "sleep_hours"
]


_model = None


def load_model():

    global _model

    if _model is None:

        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(
                f"Model not found: {MODEL_PATH}"
            )

        _model = joblib.load(
            MODEL_PATH
        )

    return _model


def predict_student(data):

    model = load_model()

    values = [
        float(data["study_hours"]),
        float(data["attendance"]),
        float(data["previous_score"]),
        float(data["assignments_completed"]),
        float(data["sleep_hours"])
    ]

    X = np.array(values).reshape(
        1, -1
    )

    prediction = model.predict(X)[0]

    prediction = float(
        np.clip(prediction, 0, 100)
    )

    if prediction >= 70:
        category = "Excellent"

    elif prediction >= 60:
        category = "Good"

    elif prediction >= 50:
        category = "Average"

    else:
        category = "Needs Improvement"

    return {
        "predicted_score": round(
            prediction,
            2
        ),
        "performance": category
    }