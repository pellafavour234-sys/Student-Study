from flask import Blueprint, jsonify

import os
import joblib


model_bp = Blueprint(
    "model",
    __name__
)


MODEL_PATH = os.path.join(
    "models",
    "student_performance_model.pkl"
)


@model_bp.route(
    "/model-info",
    methods=["GET"]
)
def model_info():

    if not os.path.exists(MODEL_PATH):

        return jsonify({
            "error": "Model file not found."
        }), 404


    model = joblib.load(
        MODEL_PATH
    )


    return jsonify({

        "model_type":
            type(model).__name__,

        "number_of_features":
            getattr(
                model,
                "n_features_in_",
                None
            ),

        "features": [
            "study_hours",
            "attendance",
            "previous_score",
            "assignments_completed",
            "sleep_hours"
        ]
    })


@model_bp.route(
    "/feature-importance",
    methods=["GET"]
)
def feature_importance():

    model = joblib.load(
        MODEL_PATH
    )


    if not hasattr(
        model,
        "feature_importances_"
    ):

        return jsonify({
            "error":
                "This model does not provide feature importance."
        }), 400


    features = [
        "study_hours",
        "attendance",
        "previous_score",
        "assignments_completed",
        "sleep_hours"
    ]


    importance = {}

    for feature, value in zip(
        features,
        model.feature_importances_
    ):

        importance[feature] = float(
            value
        )


    return jsonify({
        "feature_importance":
            importance
    })