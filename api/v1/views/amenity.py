#!/usr/bin/pytbon3
from api.v1.views import app_views
from flask import Flask, jsonify, request
from models import storage
from modesl.amenity import Amenity


@app_views.route(
