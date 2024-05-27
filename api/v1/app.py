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
    """ Runs if run as main """
    my_host = os.getenv('HBNB_API_HOST') or '0.0.0.0'
    my_port = os.getenv('HBNB_API_PORT') or 5000
    app.run(host=my_host, port=my_port, threaded=True)
