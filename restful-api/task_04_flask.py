#!/usr/bin/python3
"""Simple Flask API with in-memory user storage."""

from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Keep empty for submission; users are added via POST /add_user.
users = {}


@app.route("/", methods=["GET"])
def home():
    """Root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def data():
    """Return all usernames."""
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    """Health/status endpoint."""
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return user object by username."""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user from JSON payload."""
    try:
        payload = request.get_json(force=False, silent=False)
    except BadRequest:
        return jsonify({"error": "Invalid JSON"}), 400

    if not isinstance(payload, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = payload.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = payload
    return jsonify({"message": "User added", "user": payload}), 201


if __name__ == "__main__":
    app.run()
