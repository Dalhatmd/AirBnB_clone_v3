#!/usr/bin/pytbon3
""" amenity views """
from api.v1.views import app_views
from flask import Flask, jsonify, request, abort
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    """ get all amenities """
    amenities = storage.all(Amenity)
    amenities = [amenity.to_dict() for amenity in amenities.values()]
    return jsonify(amenities)

@app_views.route('/amenities/<amenity_id>',methods=['GET'], strict_slashes=False)
def get_amenity(amenity_id):
    """ gets amenity by id """
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_amenity(amenity_id):
    """ deletes amenity by id """
    amenity = storage.get(Amenity, amenity_id)
    if amenity:
        amenity.delete()
        storage.save()
        return {}, 200
    abort(404)

@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_amenity():
    """ creates amenity """
    """ creates an amenity """
    if not request.get_json:
        return 'Not a JSON', 400
    if 'name' not in request.json:
        return 'Missing name', 400
    amenity = Amenity(**request.get_json())
    amenity.save()
    return jsonify(amenity.to_dict()), 200


@app_views.route('/amenities/<amenity_id>', methods=['PUT'], strict_slashes=False)
def update_amenity(amenity_id):
    """ updates amenity by id """
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    if not request.json:
        return 'Not a JSON', 400
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)
    amenity.save()
    return jsonify(amenity.to_dict()), 200
