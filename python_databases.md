- Databases connect to Python through database drivers / connectors that act as a bridge between your Python code and the database engine.

```pgsql
         Python App
           ↓
 Database Driver / Connector
           ↓
Database Engine (MySQL / PostgreSQL / SQLite / MongoDB)
```

### Example Code:
```python
import snowflake.connector

#Configure the Connections
conn = snowflake.connector.connect(
    user="pratik",
    pw="Password",
    account="ACCOUNT_ID",
    warehouse="COMPUTE_WH",
    database="DEMO_DB",
    schema="PUBLIC"
)

#Open a Cursor : tool to execute SQL commands
cursor = conn.cursor()

#Execute a Query
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER,
    amount INTEGER,
    country STRING
    )
    """
)

#Insert a record
try:
    cursor.execute(
        """
        INSERT INTO orders(order_id, amount, country)
        VALUES (%s, %s, %s)
        """,
        (3, 100, "IN")
    )
    print("Insert successful")
except Exception as e:
    print("Insert failed:", e)

#Select Data from table
cursor.execute(
    "SELECT order_id, amount, country FROM orders"
)

rows = cursor.fetchall()

for row in rows:
    print(row)

#Close Cursor
cursor.close()
conn.close()
```

### We connect the database engine to Python because Python acts as the application layer that controls logic, security, validation, scalability, and integration — SQL alone cannot do this.
