from flask import Blueprint, request, jsonify

from services.prediction_service import predict_student
from services.recommendation_service import generate_recommendations

from database.database import db
from database.models import Prediction

prediction_bp = Blueprint(
    "prediction",
    __name__
)


REQUIRED_FIELDS = [
    "study_hours",
    "attendance",
    "previous_score",
    "assignments_completed",
    "sleep_hours"
]


def validate_data(data):

    for field in REQUIRED_FIELDS:

        if field not in data:
            return f"Missing field: {field}"

        try:
            value = float(data[field])

        except (ValueError, TypeError):
            return f"{field} must be numeric."


    if not 0 <= float(data["study_hours"]) <= 24:
        return "Study hours must be between 0 and 24."

    if not 0 <= float(data["attendance"]) <= 100:
        return "Attendance must be between 0 and 100."

    if not 0 <= float(data["previous_score"]) <= 100:
        return "Previous score must be between 0 and 100."

    if not 0 <= float(data["assignments_completed"]) <= 100:
        return "Assignments must be between 0 and 100."

    if not 0 <= float(data["sleep_hours"]) <= 24:
        return "Sleep hours must be between 0 and 24."

    return None


@prediction_bp.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No JSON data provided."
        }), 400


    # =========================
    # VALIDATE INPUTS
    # =========================

    error = validate_data(data)

    if error:
        return jsonify({
            "error": error
        }), 400


    # =========================
    # CONVERT VALUES TO NUMBERS
    # =========================

    clean_data = {

        "study_hours":
            float(data["study_hours"]),

        "attendance":
            float(data["attendance"]),

        "previous_score":
            float(data["previous_score"]),

        "assignments_completed":
            float(data["assignments_completed"]),

        "sleep_hours":
            float(data["sleep_hours"])

    }


    # =========================
    # MAKE PREDICTION
    # =========================

    result = predict_student(clean_data)


    # =========================
    # GENERATE RECOMMENDATIONS
    # =========================

    recommendations = generate_recommendations(
        clean_data,
        result["predicted_score"]
    )


    # =========================
    # SAVE PREDICTION
    # =========================

    record = Prediction(

        study_hours=
            clean_data["study_hours"],

        attendance=
            clean_data["attendance"],

        previous_score=
            clean_data["previous_score"],

        assignments_completed=
            clean_data["assignments_completed"],

        sleep_hours=
            clean_data["sleep_hours"],

        predicted_score=
            result["predicted_score"],

        performance=
            result["performance"]

    )


    db.session.add(record)

    db.session.commit()


    # =========================
    # SEND RESULT TO FRONTEND
    # =========================

    return jsonify({

        "success": True,

        "prediction": result,

        "recommendations": recommendations,

        "prediction_id": record.id

    })