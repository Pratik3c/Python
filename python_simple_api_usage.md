### API example:
```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
data = response.json()

print(len(data))

parsed = []

for post in data:
    parsed.append({
        "post_id": post["id"],
        "user_id": post["userId"],
        "title": post["title"]
    })

print(parsed[:2])
```

---

### Pagination
```python
import requests

page = 1
all_data = []

while True:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params={"_page": page, "_limits": 5}
    )

    if not response.json():
        break
    
    all_data.extend(response.json())
    page += 1

print(len(all_data))
```
---

### Retry_API
```python
import time
import requests

retries = 3

for attempt in range(retries):
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        response.raise_for_status()
        print("request successful")
        break
    except Exception as e:
        print(f"Attempt {attempt + 1} failed")
        time.sleep(2)
```

## HTTP Methods

| Method | Purpose          |
| ------ | ---------------- |
| GET    | Read data        |
| POST   | Create data      |
| PUT    | Update full data |
| PATCH  | Partial update   |
| DELETE | Remove data      |

## HTTP Status Codes

### 2xx – Success
| Code | Meaning |
| ---- | ------- |
| 200  | OK |
| 201  | Created |
| 204  | No Content |

### 4xx – Client Errors
| Code | Meaning |
| ---- | ------- |
| 400  | Bad Request |
| 401  | Unauthorized |
| 403  | Forbidden |
| 404  | Not Found |
| 409  | Conflict |
| 422  | Unprocessable Entity |

### 5xx – Server Errors
| Code | Meaning |
| ---- | ------- |
| 500  | Internal Server Error |
| 502  | Bad Gateway |
| 503  | Service Unavailable |


> Always return proper HTTP status codes to make APIs predictable and debuggable.

