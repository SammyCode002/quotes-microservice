# Quotes Microservice

## Description

This microservice retrieves random quotes by category from a local SQLite database.  
It allows clients to:

- Request a random quote from a specific category
- Retrieve a list of available categories

The service uses a locally imported JSON dataset and does not rely on external APIs.



## Developer

Philip Gadsden, Hunter Havice

---

## Technology Stack

- Python
- Flask
- SQLite
- JSON dataset (Kaggle quotes dataset)

---

## Communication Contract

### How to Request Data

#### Retrieve a Random Quote

**Endpoint:**  
GET /quote

**Query Parameter:**

| Parameter | Type   | Required | Description |
|-----------|--------|----------|-------------|
| category  | string | Yes      | Category of quote to retrieve |

**Example Request (Browser):**

http://localhost:5004/quote?category=life

**Example Request (Python):**

```python
import requests

url = "http://localhost:5004/quote"
params = {"category": "life"}

response = requests.get(url, params=params)
print(response.json())
```

---

#### Retrieve All Categories

**Endpoint:**  
GET /categories

No parameters required.

**Example Request:**

http://localhost:5004/categories

---

### How to Receive Data

Response format: JSON

#### Successful Quote Response

```json
{
  "quote": "Don't cry because it's over, smile because it happened.",
  "author": "Dr. Seuss",
  "category": "life"
}
```

#### Successful Categories Response

```json
{
  "categories": [
    "life",
    "love",
    "success",
    "wisdom"
  ]
}
```

---

### Error Responses

#### Missing Category Parameter (400)

```json
{
  "error": "category parameter required"
}
```

#### Category Not Found (404)

```json
{
  "error": "No quotes found for that category"
}
```

---

## Endpoints

GET /quote?category=<category>  
GET /categories  

---

## Running the Microservice

### 1. Install Dependencies

```
pip install flask
```

---

### 2. Initialize Database

Ensure `quotes.json` is in the project directory.

Run:

```
python import_quotes.py
```

This creates `quotes.db`.

---

### 3. Start the Service

```
python app.py
```

The service will run at:

http://localhost:5004

---

## Example Requests

Random life quote:

http://localhost:5004/quote?category=life

List categories:

http://localhost:5004/categories

---

## Status Codes

| Code | Meaning |
|------|---------|
| 200  | Success |
| 400  | Missing category parameter |
| 404  | Category not found |
| 500  | Internal server error |

---

## UML Sequence Diagram
```
Client                        Quotes Microservice
  |                                  |
  | GET /quote?category=life         |
  |--------------------------------->|
  |                                  | Query SQLite DB
  |                                  | ORDER BY RANDOM()
  |                                  | LIMIT 1
  |                                  |
  | 200 OK                           |
  | {quote, author, category}        |
  |<---------------------------------|

```