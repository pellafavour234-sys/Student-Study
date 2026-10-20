from .database import db
from datetime import datetime


class Prediction(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    study_hours = db.Column(
        db.Float,
        nullable=False
    )

    attendance = db.Column(
        db.Float,
        nullable=False
    )

    previous_score = db.Column(
        db.Float,
        nullable=False
    )

    assignments_completed = db.Column(
        db.Float,
        nullable=False
    )

    sleep_hours = db.Column(
        db.Float,
        nullable=False
    )

    predicted_score = db.Column(
        db.Float,
        nullable=False
    )

    performance = db.Column(
        db.String(50),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )