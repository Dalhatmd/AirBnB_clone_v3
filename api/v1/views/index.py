#!/usr/bin/python3
""" index view """
from models import storage
from api.v1.views import app_views
from flask import jsonify
app = app_views


@app.route('/status', strict_slashes=False)
def status():
    """ returns the status """
    return (jsonify({'status': 'OK'}))


@app.route('/stats', strict_slashes=False)
def stats():
    """ returns count of all objects """
    return jsonify({"users": storage.count("User"),
                    "reviews": storage.count("Review"),
                    "places": storage.count("Place"),
                    "cities": storage.count("City"),
                    "amenities": storage.count("Amenity"),
                    "states": storage.count("State")})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
