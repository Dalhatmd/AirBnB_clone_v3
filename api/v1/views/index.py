#!/usr/bin/python3
""" index view """
from models import storage
from api.v1.views import app_views
from flask import Flask
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """ returns the status """
    return (jsonify({'status': 'OK'}))


@app_views.route('/stats', strict_slashes=False)
def stats():
    """ returns count of all objects """
    return jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")})
