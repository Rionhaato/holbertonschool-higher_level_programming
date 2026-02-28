#!/usr/bin/python3
"""API security examples with Basic Auth and JWT in Flask."""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt,
    jwt_required,
)
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-me"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


@auth.verify_password
def verify_password(username, password):
    """Validate credentials for Basic Auth."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@auth.error_handler
def basic_auth_error(_status):
    """Return consistent 401 response for Basic Auth failures."""
    return jsonify({"error": "Unauthorized"}), 401


@jwt.unauthorized_loader
def handle_missing_or_invalid_token(_err):
    """Handle missing JWT."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token(_err):
    """Handle malformed/invalid JWT."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token(_jwt_header, _jwt_payload):
    """Handle expired JWT."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token(_jwt_header, _jwt_payload):
    """Handle revoked JWT."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token(_jwt_header, _jwt_payload):
    """Handle non-fresh token where fresh is required."""
    return jsonify({"error": "Fresh token required"}), 401


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Protected by Basic Authentication."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Authenticate user and return JWT token."""
    try:
        payload = request.get_json(force=False, silent=False)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if not isinstance(payload, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = payload.get("username")
    password = payload.get("password")

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password or ""):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity=username, additional_claims={"role": user["role"]}
    )
    return jsonify({"access_token": access_token})


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Protected by JWT."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Allow access only to admin role."""
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
