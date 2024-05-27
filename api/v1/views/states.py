#!/usr/bin/python3
""" states views """
from api.v1.views import app_views
from models import storage
from flask import Flask, abort, request, jsonify, make_request
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """ gets all states """
    states = storage.all(State)
    states = [state.to_dict() for state in states.values()]
    return jsonify(states)


@app_views.route('/states/<string:state_id>', methods=['GET'],
                 strict_slashes=False)
def get_state(state_id):
    """Get a state by id"""
    state = storage.get(State, state_id)
    if state:
        return jsonify(state.to_dict())
    abort(404)


@app_views.route('/states/<string:state_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_state(state_id):
    """ deletes a state by id"""
    state = storage.get(State, state_id)
    if state:
        state.delete()
        storage.save()
        return {}, 200
    abort(404)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post_state():
    """ creates a state """
    if not request.get_json():
        return make_request(jsonify({"error": "Not a JSON"}), 400)
    if 'name' not in request.get_json():
        return make_request(jsonify({"error": "Missing name"}), 400)
    state = State(**request.get_json())
    state.save()
    return jsonify(state.to_dict()), 200


@app_views.route('/states/<string:state_id>', methods=['PUT'],
                 strict_slashes=False)
def update_state(state_id):
    """ updates a state by id """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if not request.get_json():
        return make_request(jsonify({"error": "Not a JSON"}), 400)
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200
