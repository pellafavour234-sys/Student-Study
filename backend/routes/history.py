from flask import Blueprint, jsonify

from database.models import Prediction


history_bp = Blueprint(
    "history",
    __name__
)


@history_bp.route(
    "/history",
    methods=["GET"]
)
def history():

    records = Prediction.query.order_by(
        Prediction.created_at.desc()
    ).limit(50).all()


    results = []

    for record in records:

        results.append({

            "id": record.id,

            "study_hours":
                record.study_hours,

            "attendance":
                record.attendance,

            "previous_score":
                record.previous_score,

            "assignments_completed":
                record.assignments_completed,

            "sleep_hours":
                record.sleep_hours,

            "predicted_score":
                record.predicted_score,

            "performance":
                record.performance,

            "created_at":
                record.created_at.isoformat()
        })


    return jsonify({
        "history": results
    })