#!/usr/bin/python3
"""Task 4: display product data from JSON, CSV, or SQLite in Flask."""

import csv
import json
import sqlite3

from flask import Flask, render_template, request


app = Flask(__name__)


def normalize_products(products):
    """Normalize product values for template rendering and id filtering."""
    normalized = []

    for product in products:
        normalized.append(
            {
                "id": int(product["id"]),
                "name": product["name"],
                "category": product["category"],
                "price": float(product["price"]),
            }
        )

    return normalized


def load_products_from_json():
    """Load products from the local JSON file."""
    with open("products.json", "r", encoding="utf-8") as file:
        products = json.load(file)
    return normalize_products(products)


def load_products_from_csv():
    """Load products from the local CSV file."""
    with open("products.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        products = list(reader)
    return normalize_products(products)


def load_products_from_sql():
    """Load products from the local SQLite database."""
    connection = sqlite3.connect("products.db")
    connection.row_factory = sqlite3.Row

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        products = [dict(row) for row in cursor.fetchall()]
    finally:
        connection.close()

    return normalize_products(products)


def filter_products(product_list, product_id):
    """Filter products by id."""
    if product_id is None:
        return product_list, None

    try:
        product_id = int(product_id)
    except ValueError:
        return [], "Product not found"

    filtered = [product for product in product_list if product["id"] == product_id]
    if not filtered:
        return [], "Product not found"

    return filtered, None


@app.route("/products")
def products():
    """Render the product listing page."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    try:
        if source == "json":
            product_list = load_products_from_json()
        elif source == "csv":
            product_list = load_products_from_csv()
        elif source == "sql":
            product_list = load_products_from_sql()
        else:
            return render_template(
                "product_display.html",
                products=[],
                error="Wrong source",
            )
    except sqlite3.Error:
        return render_template(
            "product_display.html",
            products=[],
            error="Database error",
        )

    product_list, error = filter_products(product_list, product_id)
    return render_template(
        "product_display.html",
        products=product_list,
        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
