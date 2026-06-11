# Consuming REST APIs — Requests & Postman

## 🎯 Objective

Students will learn how to call and test REST APIs from the client side using Python's `requests` library and Postman. They'll parse JSON responses, handle HTTP status codes, and chain requests to build simple workflows.

## 📝 Tasks

### 🛠️ Make HTTP requests with `requests`

#### Description
Write a small Python client that calls a public REST API (e.g., JSONPlaceholder) to list resources, fetch a single resource, create a new resource, and handle errors.

#### Requirements

- Implement functions for `GET` (list & single), `POST`, and error handling.
- Parse JSON responses and extract meaningful fields.
- Gracefully handle non-2xx responses and network errors.

### 🛠️ Use Postman to test endpoints

#### Description
Create a Postman collection that issues the same requests as your Python client and documents expected responses.

#### Requirements

- Create requests for list, get, and create operations.
- Add example responses and short descriptions.

## Deliverables

- A working Python script in `starter_code.py` that demonstrates requests to the API.
- A `requirements.txt` listing dependencies.
- Example `curl_examples.md` and `postman_instructions.md` showing how to run and test the requests.

## How to run

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the starter client:

```bash
python starter_code.py
```

## Extensions / Bonus

- Authenticate requests using API keys or OAuth (if available).
- Save responses to a local JSON file and analyze them.
