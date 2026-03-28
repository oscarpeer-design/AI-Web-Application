"""
Routes and views for the flask application.
"""

from flask import request, jsonify, send_from_directory
from AI_Web_Application import app
from AI_Web_Application.wharehouse_valuator import Valuation

@app.route('/api/data')
def get_data():
    return jsonify({
        "message": "Hello from Flask backend"
    })

@app.route("/api/valuate", methods=["POST"])
def valuate():
    data = request.get_json()

    marketCap = data.get("marketCap")
    area = data.get("area")
    clearance = data.get("clearance")
    location = data.get("location")

    valuation = Valuation(marketCap, area, clearance, location)
    valuation.valuate_warehouse()
    result = valuation.return_values()

    return jsonify(result)

@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory(app.static_folder, path)

@app.route("/")
def serve_react():
    return send_from_directory(app.static_folder, "index.html")