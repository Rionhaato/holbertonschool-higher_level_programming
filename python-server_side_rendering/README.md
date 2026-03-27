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
- `template.txt`: Base invitation template used for Task 0.

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

## Suggested Commit Structure

Use one commit per task:

- `Task 0: add invitation templating program`
- `Task 1: ...`
- `Task 2: ...`
- `Task 3: ...`
- `Task 4: ...`
- `Task 5: ...`
