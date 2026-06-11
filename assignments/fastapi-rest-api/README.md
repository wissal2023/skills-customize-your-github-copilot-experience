# Building REST APIs with FastAPI

## Overview

This assignment guides students through building a small REST API using the FastAPI framework. Students will implement a CRUD API for a simple `Item` resource, learn request validation with Pydantic models, explore automatic API docs (OpenAPI/Swagger), and run the app locally using Uvicorn.

## Learning Objectives

- Create REST endpoints (GET, POST, PUT, DELETE) with FastAPI
- Use Pydantic models for request/response validation
- Explore automatic API docs (OpenAPI / Swagger UI)
- Handle errors and HTTP status codes
- Run the server with Uvicorn and test endpoints with curl or HTTP clients

## Prerequisites

- Python 3.8+
- Basic Python knowledge (functions, dicts, lists)

## Tasks

1. Implement the `Item` model using Pydantic.
2. Create endpoints:
   - `GET /items` — list all items
   - `GET /items/{item_id}` — retrieve a single item
   - `POST /items` — create a new item
   - `PUT /items/{item_id}` — update an existing item
   - `DELETE /items/{item_id}` — remove an item
3. Add input validation and appropriate HTTP responses.
4. Document example requests in `curl_examples.md`.
5. (Bonus) Add query parameters for filtering and pagination.

## Deliverables

- A working FastAPI app in `starter_code.py`.
- A short `README.md` describing endpoints and how to run the app.
- Example requests in `curl_examples.md`.

## How to run locally

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Start the app with Uvicorn:

```bash
uvicorn starter_code:app --reload
```

3. Open the interactive docs at `http://127.0.0.1:8000/docs`.

## Evaluation

- Correctness of endpoints and validation
- Clear README and example requests
- Clean, readable code and helpful comments
