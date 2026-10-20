from flask import Flask, jsonify

from flask_cors import CORS

from database.database import db

from routes.prediction import (
    prediction_bp
)

from routes.history import (
    history_bp
)

from routes.model import (
    model_bp
)

from routes.analytics import (
    analytics_bp
)


app = Flask(__name__)


# ============================================================
# CONFIGURATION
# ============================================================

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "sqlite:///student_ai.db"

app.config[
    "SQLALCHEMY_TRACK_MODIFICATIONS"
] = False


# ============================================================
# EXTENSIONS
# ============================================================

CORS(app)

db.init_app(app)


# ============================================================
# BLUEPRINTS
# ============================================================

app.register_blueprint(
    prediction_bp
)

app.register_blueprint(
    history_bp
)

app.register_blueprint(
    model_bp
)

app.register_blueprint(
    analytics_bp
)


# ============================================================
# HEALTH CHECK
# ============================================================

@app.route(
    "/health",
    methods=["GET"]
)
def health():

    return jsonify({

        "status": "healthy",

        "service":
            "StudentAI API"
    })


# ============================================================
# ROOT
# ============================================================

@app.route("/")
def home():

    return jsonify({

        "message":
            "StudentAI API is running.",

        "version":
            "2.0"
    })


# ============================================================
# DATABASE
# ============================================================

with app.app_context():

    db.create_all()


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )