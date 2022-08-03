# FASTAPI
Python web-Framework for building API's


#Rest uses HTTP Request Methods
GET: Read method that retrives data
PUT: Update the entire resource
POST: create method ,submit data
PATCH: Update part of the resource 
DELETE: Delete the resource
# Using **async** before the function, typically provides performance optimizations when handling asynchronous functions.
# Which will return json object of the fastapi
http://127.0.0.1:8000\openapi.json
# Which will return swaggerUi for the fastapi
http://127.0.0.1:8000/docs

# Enumeration Path parameters
To enable drop down option to list inputs

# Sqlite3 cmd line comands

sqlite> .schema
CREATE TABLE todos (
        id INTEGER NOT NULL,
        title VARCHAR,
        description VARCHAR,
        priority INTEGER,
        complete BOOLEAN,
        PRIMARY KEY (id)
);
sqlite> .mode column
sqlite> select* from todos;
id  title     description  priority  complete
--  --------  -----------  --------  --------
1   Somthing  Hello        1         0
2   Somthing  Hello        2         0
sqlite> .mode markdown
sqlite> select * from todos;
| id |  title   | description | priority | complete |
|----|----------|-------------|----------|----------|
| 1  | Somthing | Hello       | 1        | 0        |
| 2  | Somthing | Hello       | 2        | 0        |
sqlite> .mode box
sqlite> select * from todos;
┌────┬──────────┬─────────────┬──────────┬──────────┐
│ id │  title   │ description │ priority │ complete │
├────┼──────────┼─────────────┼──────────┼──────────┤
│ 1  │ Somthing │ Hello       │ 1        │ 0        │
│ 2  │ Somthing │ Hello       │ 2        │ 0        │
└────┴──────────┴─────────────┴──────────┴──────────┘
sqlite>.mode
sqlite> select * from todos;
+----+----------+-------------+----------+----------+
| id |  title   | description | priority | complete |
+----+----------+-------------+----------+----------+
| 1  | Somthing | Hello       | 1        | 0        |
| 2  | Somthing | Hello       | 2        | 0        |
+----+----------+-------------+----------+----------+
sqlite>

