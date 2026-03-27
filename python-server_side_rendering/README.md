# Python - Server-Side Rendering

This project introduces server-side rendering (SSR) in Python using Flask and Jinja. The goal is to generate HTML on the server, work with dynamic data sources, and build pages that are efficient, maintainable, and SEO-friendly.

## Learning Objectives

- Understand server-side rendering and how it differs from client-side rendering.
- Learn the benefits of SSR in web development.
- Implement SSR in Python using Flask.
- Use Jinja templates to generate dynamic HTML.
- Read and display data from JSON, CSV, and SQLite sources.
- Handle dynamic content and user input in web applications.

## Resources

- MDN Web Docs on Server-Side Web Development
- Client-side vs. Server-side vs. Pre-rendering for Web Apps
- Flask Official Documentation
- Python JSON Documentation
- Python CSV Documentation
- Python SQLite Documentation
- Jinja2 Documentation

## Requirements

- Python 3.x
- Standard Python file handling and string templating
- Flask and Jinja will be used in later tasks

## Files

- `task_00_intro.py`: Generates invitation files from a template and attendee data.
- `task_01_jinja.py`: Flask app that renders basic pages with shared templates.
- `task_02_logic.py`: Flask app that renders a dynamic items page from JSON data.
- `task_03_files.py`: Flask app that displays products from JSON or CSV files.
- `task_04_db.py`: Flask app that displays products from JSON, CSV, or SQLite.
- `template.txt`: Base invitation template used for Task 0.
- `items.json`: JSON data source for the dynamic items page.
- `products.json`: JSON product data source for Task 3.
- `products.csv`: CSV product data source for Task 3.
- `products.db`: SQLite database used for Task 4.
- `templates/header.html`: Shared page header with navigation links.
- `templates/footer.html`: Shared page footer.
- `templates/index.html`: Home page template.
- `templates/about.html`: About page template.
- `templates/contact.html`: Contact page template.
- `templates/items.html`: Dynamic items page template using loops and conditions.
- `templates/product_display.html`: Product table template with error handling.

## How to Run Task 0

From the `python-server_side_rendering` directory:

```bash
python3
```

Example test:

```python
from task_00_intro import generate_invitations

with open("template.txt", "r", encoding="utf-8") as file:
    template_content = file.read()

attendees = [
    {
        "name": "Alice",
        "event_title": "Python Conference",
        "event_date": "2023-07-15",
        "event_location": "New York"
    },
    {
        "name": "Bob",
        "event_title": "Data Science Workshop",
        "event_date": "2023-08-20",
        "event_location": "San Francisco"
    },
    {
        "name": "Charlie",
        "event_title": "AI Summit",
        "event_date": None,
        "event_location": "Boston"
    }
]

generate_invitations(template_content, attendees)
```

Expected result:

- The script creates `output_1.txt`, `output_2.txt`, and `output_3.txt`.
- Missing values are replaced with `"N/A"`.
- Empty or invalid inputs print an error message and stop without creating files.

## How to Run Task 1

From the `python-server_side_rendering` directory:

```bash
python3 task_01_jinja.py
```

Then open these routes in your browser:

- `http://127.0.0.1:5000/`
- `http://127.0.0.1:5000/about`
- `http://127.0.0.1:5000/contact`

## How to Run Task 2

From the `python-server_side_rendering` directory:

```bash
python3 task_02_logic.py
```

Then open:

- `http://127.0.0.1:5000/items`

## How to Run Task 3

From the `python-server_side_rendering` directory:

```bash
python3 task_03_files.py
```

Then test routes like:

- `http://127.0.0.1:5000/products?source=json`
- `http://127.0.0.1:5000/products?source=csv`
- `http://127.0.0.1:5000/products?source=json&id=1`
- `http://127.0.0.1:5000/products?source=xml`

## How to Run Task 4

From the `python-server_side_rendering` directory:

```bash
python3 task_04_db.py
```

Then test routes like:

- `http://127.0.0.1:5000/products?source=json`
- `http://127.0.0.1:5000/products?source=csv`
- `http://127.0.0.1:5000/products?source=sql`
- `http://127.0.0.1:5000/products?source=sql&id=2`

## Task Breakdown

### Task 0: Creating a Simple Templating Program

File: `task_00_intro.py`

What it does:

- Validates the template input and attendees list.
- Stops early for empty template or empty attendee data.
- Replaces `{name}`, `{event_title}`, `{event_date}`, and `{event_location}` placeholders.
- Uses `"N/A"` when a value is missing or `None`.
- Generates sequential output files named `output_X.txt`.

Status: Completed

### Task 1: Creating a Basic HTML Template in Flask

File: `task_01_jinja.py`

What it does:

- Creates a basic Flask application running on port `5000`.
- Renders `index.html`, `about.html`, and `contact.html`.
- Reuses `header.html` and `footer.html` across all pages with Jinja `{% include %}`.
- Provides navigation links for Home, About, and Contact pages.

Status: Completed

### Task 2: Creating a Dynamic Template with Loops and Conditions in Flask

File: `task_02_logic.py`

What it does:

- Reads item data from `items.json`.
- Adds a `/items` route to the Flask application.
- Renders `items.html` with a Jinja loop for item output.
- Displays `No items found` when the list is empty.

Status: Completed

### Task 3: Displaying Data from JSON or CSV Files in Flask

File: `task_03_files.py`

What it does:

- Reads product data from either `products.json` or `products.csv`.
- Uses the `source` query parameter to choose the data file.
- Uses the optional `id` query parameter to filter products.
- Displays `Wrong source` for unsupported sources.
- Displays `Product not found` when the requested product id does not exist.

Status: Completed

### Task 4: Extending Dynamic Data Display to Include SQLite in Flask

File: `task_04_db.py`

What it does:

- Extends product loading to support `json`, `csv`, and `sql` sources.
- Reads data from `products.db` when `source=sql`.
- Reuses `product_display.html` for all product sources.
- Preserves source validation and product id filtering.
- Handles SQLite errors and reports them in the template.

Status: Completed

## Suggested Commit Structure

Use one commit per task:

- `Task 0: add invitation templating program`
- `Task 1: add Flask templates with shared header and footer`
- `Task 2: add dynamic items template with JSON data`
- `Task 3: add product display from JSON or CSV sources`
- `Task 4: add SQLite product source support`
- `Task 5: ...`
