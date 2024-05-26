#!/usr/bin/python3
from models import storage
from api.v1.views import app_views
from flask import jsonify
app = app_views


@app.route('/status')
def status():
    return (jsonify({'status': 'OK'}))


@app.route('/stats', strict_slashes=False)
def stats():
    return jsonify({"users": storage.count("User"),
        "reviews": storage.count("Review"),
        "places": storage.count("Place"),
        "cities": storage.count("City"),
        "amenities": storage.count("Amenity")})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
