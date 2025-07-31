# FastAPI Todo List API

A simple REST API built with FastAPI for managing a todo list. This project demonstrates basic CRUD operations using FastAPI, Pydantic models, and provides interactive API documentation.

## Features

- Create todo items with text and completion status
- List all todo items with optional limit
- Get specific todo items by ID
- Interactive API documentation with Swagger UI
- Automatic request/response validation with Pydantic

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd fastapi-intro
```

2. Install the required dependencies:
```bash
pip install fastapi uvicorn
```

## Running the Application

Start the development server with auto-reload:
```bash
uvicorn main:app --reload
```

The API will be available at:
- **API Base URL**: http://127.0.0.1:8000
- **Interactive Documentation**: http://127.0.0.1:8000/docs
- **Alternative Documentation**: http://127.0.0.1:8000/redoc

## API Endpoints

### 1. Root Endpoint
- **GET** `/`
- **Description**: Returns a simple hello world message
- **Response**: `{"Hello": "World"}`

### 2. Create Todo Item
- **POST** `/items`
- **Description**: Creates a new todo item
- **Request Body**:
  ```json
  {
    "text": "Buy milk",
    "is_done": false
  }
  ```
- **Response**: Returns the updated list of all items

### 3. List Todo Items
- **GET** `/items`
- **Description**: Retrieves all todo items
- **Query Parameters**:
  - `limit` (optional): Maximum number of items to return (default: 10)
- **Response**: Array of todo items

### 4. Get Specific Todo Item
- **GET** `/items/{item_id}`
- **Description**: Retrieves a specific todo item by ID
- **Path Parameters**:
  - `item_id`: The index of the item (0-based)
- **Response**: Single todo item or 404 if not found

## Usage Examples

### Using curl

1. **Create a new todo item**:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"text": "Buy milk"}' http://127.0.0.1:8000/items
```

2. **List all todo items**:
```bash
curl -X GET http://127.0.0.1:8000/items
```

3. **Get a specific todo item**:
```bash
curl -X GET http://127.0.0.1:8000/items/0
```

4. **List items with limit**:
```bash
curl -X GET "http://127.0.0.1:8000/items?limit=5"
```

### Using the Interactive Documentation

1. Open your browser and navigate to http://127.0.0.1:8000/docs
2. You'll see the Swagger UI with all available endpoints
3. Click on any endpoint to expand it
4. Click "Try it out" to test the endpoint directly from the browser
5. Fill in the required parameters and click "Execute"

## Data Model

### Item Schema
```json
{
  "text": "string",
  "is_done": "boolean (default: false)"
}
```

## Development

### Project Structure
```
fastapi-intro/
├── main.py          # Main FastAPI application
├── README.md        # This file
└── .gitignore       # Git ignore rules
```

### Key Components

- **FastAPI**: Modern web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: ASGI server for running the application

### Adding New Features

To extend this application, you can:
1. Add new endpoints in `main.py`
2. Create new Pydantic models for request/response validation
3. Implement database integration for persistent storage
4. Add authentication and authorization
5. Implement item update and delete operations

## Notes

- This is a simple in-memory implementation - data is lost when the server restarts
- For production use, consider adding a database for persistent storage
- The application uses FastAPI's automatic request/response validation
- Interactive documentation is automatically generated from your code
