# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using Python and FastAPI to manage a collection of tasks. This assignment introduces students to route design, request models, response formatting, and basic API validation.

## 📝 Tasks

### 🛠️ Set Up the API Project

#### Description
Create a FastAPI app that serves a basic task API. The app should be organized clearly so that routes and data models are easy to understand and maintain.

#### Requirements
Completed program should:

- Create a FastAPI application instance
- Define a simple in-memory data store for tasks
- Add a root endpoint that returns a welcome message
- Use Python type hints and Pydantic models for task data
- Run the app locally with an ASGI server such as Uvicorn

### 🛠️ Implement CRUD Endpoints

#### Description
Add endpoints that allow clients to create, view, update, and delete tasks through a RESTful API.

#### Requirements
Completed program should:

- Create a GET endpoint to list all tasks
- Create a GET endpoint to fetch one task by ID
- Create a POST endpoint to add a new task
- Create a PUT or PATCH endpoint to update an existing task
- Create a DELETE endpoint to remove a task
- Return JSON responses with appropriate task data
- Use clear status codes for success and not-found conditions

### 🛠️ Validate and Test the API

#### Description
Improve the API so it behaves reliably and handles client input appropriately. This task focuses on validation and simple testing ideas.

#### Requirements
Completed program should:

- Validate required fields such as title and completion state
- Prevent invalid task IDs or malformed request payloads
- Return helpful error messages when something goes wrong
- Document the API with a short description of available routes
- Test the endpoints using a browser, curl, or a small API client
