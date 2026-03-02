from flask import Flask
from routes.studentroutes import student_bp
# from middleware.logger import register_middlewares

def create_app():
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(student_bp)

    # Register Middlewares
    # register_middlewares(app)

    return app

app = create_app()

@app.route("/")
def home():
    return {"message": "Backend Server is running"}

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)