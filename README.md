# Task Manager

A lightweight Flask web app for adding and removing tasks from an in-memory list.

## Requirements

- Python 3.10 or newer
- pip

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000). Tasks are held in process memory and are lost when the server restarts. The Flask development server is for local development only.

## Routes

| Method | Route | Purpose |
|---|---|---|
| `GET` | `/` | Display the task list and add form. |
| `POST` | `/add_task` | Add a task from the form. |
| `POST` | `/remove_task/<index>` | Remove a task by its zero-based list index. |

Run the request-level tests with:

```bash
python -m unittest discover -s tests -v
```

## Layout

```text
app.py             Flask routes and task list
templates/index.html  Task-list page
style.css          Page styles
```
