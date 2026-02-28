#!/usr/bin/python3
"""Consume and process posts from JSONPlaceholder."""

import csv
import requests


POSTS_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch posts, print status code, then print all post titles on success."""
    response = requests.get(POSTS_URL, timeout=10)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title", ""))


def fetch_and_save_posts():
    """Fetch posts and save id/title/body fields to posts.csv on success."""
    response = requests.get(POSTS_URL, timeout=10)

    if response.status_code == 200:
        posts = response.json()
        rows = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body"),
            }
            for post in posts
        ]

        with open("posts.csv", "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(rows)
