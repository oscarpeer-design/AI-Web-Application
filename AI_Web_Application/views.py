"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, jsonify
from AI_Web_Application import app

from flask import jsonify
from AI_Web_Application import app
from flask import send_from_directory

@app.route('/api/data')
def get_data():
    return jsonify({
        "message": "Hello from Flask backend"
    })
@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory(app.static_folder, path)

@app.route("/")
def serve_react():
    return send_from_directory(app.static_folder, "index.html")