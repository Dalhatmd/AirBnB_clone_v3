#!/usr/bin/python3
""" return endpoint of flask app """
from flask import Flask, abort, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
import os
app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close_storage(exception):
    """ close storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ handles not found error """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
""" runs as main """
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)

    app.run(host, int(port), threaded=True)
