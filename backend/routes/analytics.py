from flask import Blueprint, jsonify

from database.models import Prediction

from database.database import db


analytics_bp = Blueprint(
    "analytics",
    __name__
)


@analytics_bp.route(
    "/analytics",
    methods=["GET"]
)
def analytics():

    predictions = Prediction.query.all()


    if not predictions:

        return jsonify({

            "total_predictions": 0,

            "average_score": 0,

            "highest_score": 0,

            "lowest_score": 0
        })


    scores = [
        p.predicted_score
        for p in predictions
    ]


    return jsonify({

        "total_predictions":
            len(scores),

        "average_score":
            round(
                sum(scores) / len(scores),
                2
            ),

        "highest_score":
            round(
                max(scores),
                2
            ),

        "lowest_score":
            round(
                min(scores),
                2
            )
    })