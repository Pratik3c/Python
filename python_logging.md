# Logging in Python

Logging in Python is how real applications track what’s happening at runtime—errors, warnings, info, debugging details—**without using `print()`**.

---

## 1️⃣ What is Logging & Why Not `print()`?

### `print()` ❌
- No severity level
- No timestamps
- Hard to disable in production
- Not thread-safe
- Not suitable for large applications

### `logging` ✅
- Built-in standard library
- Different levels (`INFO`, `ERROR`, etc.)
- Can write to console, file, cloud
- Works in multi-threaded & production systems
- Configurable per environment

### 👉 Rule
- print() → learning / debugging locally
- logging → real projects / production


---

## 2️⃣ Basic Logging Example

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Application started")
logging.warning("This is a warning")
logging.error("Something went wrong")
```

### Output:
```
INFO:root:Application started
WARNING:root:This is a warning
ERROR:root:Something went wrong
```
---


## 3️⃣ Logging Levels
### Logging Levels (Lowest to Highest Severity)

Logging levels indicate the severity of an event in an application.

| Level     | Usage |
|-----------|-------|
| DEBUG     | Detailed internal information (development only) |
| INFO      | Normal application flow |
| WARNING   | Something unexpected, but the program continues |
| ERROR     | Operation failed |
| CRITICAL  | Severe issue, application may stop |

---

## 4️⃣ Logging Format
### Logs should always contain time and severity.

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Formatted log message")
```

### Output:
```
2026-01-21 10:15:22 - INFO - Formatted log message
```

## Common Logging Format Attributes

Logging format attributes define how log messages are displayed.

| Attribute        | Description  |
|------------------|--------------|
| `%(asctime)s`    | Timestamp |
| `%(levelname)s`  | Log level |
| `%(message)s`    | Log message |
| `%(filename)s`   | File name |
| `%(lineno)d`     | Line number |
| `%(name)s`       | Logger name |

---

## 5️⃣ Writing Logs to a File
```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Server started")
logging.error("An error occurred")
```
#### 📁 A file named app.log will be created automatically.

---

## 6️⃣ Logger vs Root Logger (Critical Concept)
#### ❌ Root Logger (Not Recommended for Large Apps)
```python
import logging

logging.info("Something happened")
```

#### ✅ Module-Level Logger (Best Practice)
```python
import logging

logger = logging.getLogger(__name__)

logger.info("Something happened in this module")
```

### Why Use getLogger(__name__)?

- Identifies which module produced the log
- Allows per-module log control
- Scales well in large applications

