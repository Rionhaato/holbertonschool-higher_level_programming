#!/usr/bin/python3
"""Task 3: display product data from JSON or CSV files in Flask."""

import csv
import json

from flask import Flask, render_template, request


app = Flask(__name__)


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


@app.route("/products")
def products():
    """Render the product listing page."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source == "json":
        product_list = load_products_from_json()
    elif source == "csv":
        product_list = load_products_from_csv()
    else:
        return render_template(
            "product_display.html",
            products=[],
            error="Wrong source",
        )

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                "product_display.html",
                products=[],
                error="Product not found",
            )

        product_list = [product for product in product_list if product["id"] == product_id]
        if not product_list:
            return render_template(
                "product_display.html",
                products=[],
                error="Product not found",
            )

    return render_template(
        "product_display.html",
        products=product_list,
        error=None,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
