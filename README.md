# 📁 Python File Handling (Industry-Level Basics)

This document explains **industry-standard file handling practices in Python** with clear and minimal examples.

---

## 1. Always Use `with` (Context Manager)

### ✅ Recommended (Industry Standard)

```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

### Why use `with`?

* Automatically closes the file
* Prevents memory leaks
* Safe for production systems

---

### 🚫 Avoid This

```python
f = open("data.txt", "r")
content = f.read()
# forgetting f.close()
```

This can cause:

* File descriptor leaks
* Application crashes in long-running servers

---

## 2. File Modes (Commonly Used)

| Mode | Description       | Industry Usage     |
| ---- | ----------------- | ------------------ |
| `r`  | Read              | Config files, logs |
| `w`  | Write (overwrite) | Reports, exports   |
| `a`  | Append            | Logging            |
| `rb` | Read binary       | Images, PDFs       |
| `wb` | Write binary      | File uploads       |

### Example: Writing to a File

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, Industry!")
```

---

## 3. Path Handling (Best Practice)

### ❌ Avoid Hardcoded Paths

```python
file_path = "C:/Users/Name/Desktop/data.txt"
```

---

### ✅ Use `pathlib` (Industry Preferred)

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / "data" / "data.txt"

with file_path.open("r", encoding="utf-8") as f:
    print(f.read())
```

### Benefits

* Cross-platform compatibility
* Cleaner and readable code
* Production-ready paths

---

## 4. JSON File Handling

### Create & Write JSON

```python
import json

data = {
    "name": "Pratik",
    "role": "Developer",
    "active": True
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
```

---

### Read JSON

```python
import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data["name"])
```

---

## 5. CSV File Handling

### Create & Write CSV

```python
import csv

with open("users.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "email"])
    writer.writerow([1, "Pratik", "pratik@email.com"])
```

---

### Read CSV

```python
import csv

with open("users.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["email"])
```

---

## 6. Industry Best Practices Summary

* ✔ Always use `with`
* ✔ Use correct file modes
* ✔ Prefer `pathlib` over hardcoded paths
* ✔ Use `json` and `csv` modules
* ✔ Add error handling in production code

---

## 7. Common Industry Use Cases

* Flask / Django backend applications
* Data engineering pipelines
* Machine learning preprocessing
* Logging and monitoring systems

---

### Q: Why do we use `if __name__ == "__main__"` (main guard)?
```
Answer:
To ensure that code executes only when the script is run directly, and not when imported as a module.
```

### 🚀 Ready for Industry-Level Python File Handling
