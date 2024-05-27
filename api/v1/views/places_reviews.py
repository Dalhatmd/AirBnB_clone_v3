#!/usr/bin/python3
""" reviews view """
from api.v1.views import app_views
from models import storage
from models.review import Review
from flask import Flask, jsonify, abort


@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def get_reviews(place_id):
    """gets revies of a place """
    place = storage.get(Place, place_id)
    if place:
        reviews = [review.to_dict() for review in place.reviews]
        return jsonify(reviews)
    abort(404)


@app_views.route('/reviews/<review_id>', methods=['GET'],
                 strict_slashes=False)
def get_review(review_id):
    """gets a review """
    review = storage.get(Review, review_id)
    if review:
        return jsonify(review.to_dict())
    abort(404)


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_review(review_id):
    """deletes a review """
    review = storage.get(Review, review_id)
    if review:
        storage.delete(review)
        storage.save()
        return jsonify({}), 200
    abort(404)


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def create_review(place_id):
    """creates a review """
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    review = request.get_json()
    if not review:
        return jsonify({'error': 'Not a JSON'}), 400
    if 'user_id' not in review:
        return jsonify({'error': 'Missing user_id'}), 400
    user = storage.get(User, review['user_id'])
    if not user:
        abort(404)
    if 'text' not in review:
        return jsonify({'error': 'Missing text'}), 400
    review['place_id'] = place_id
    review = Review(**review)
    review.save()
    return jsonify(review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['PUT'],
                 strict_slashes=False)
def update_review(review_id):
    """updates a review """
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    review_data = request.get_json()
    if not review_data:
        return jsonify({'error': 'Not a JSON'}), 400
    for key, value in review_data.items():
        if key not in ['id',
                       'user_id',
                       'place_id',
                       'created_at',
                       'updated_at']:
            setattr(review, key, value)
    review.save()
    return jsonify(review.to_dict()), 200
