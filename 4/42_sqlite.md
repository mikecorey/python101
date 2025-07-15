
# SQLite

- First things first: Ess Queue El or Sequel.  Either is fine. 

- SQLite is a built-in database used in everything from Python to Phone apps.  Structured Query Language (SQL) is THE standard for databases. If you're working with data, you need to know SQL.

- SQL is a language standard (ANSI standard from the 80s... so it's super old.  sigh...)


## Why SQLite?

* **serverless** – just a single `.db` file  
* **Transactional** – ACID by default
* **Perfect for 97% of apps** – MVPs, local apps, etc.


## What's ACID?
- Atomicity - given a TRANSACTION either everything succeeds or nothing does
- Consistency - the database stays valid.  (orphaned keys)
- Isolation - a transaction acts like it's all by itself
- Durability - commits are permanent even if power fails or it crashes


## The CLI

```bash
sqlite3 demo.db         # The file we want to create or open...
sqlite> .tables         # Built in commands start with `.` 
```

### dot-commands

| Command | Purpose  |
|---------|---------------|
| `.help` | list all dot-commands |
| `.schema` | dump description of every table |
| `.headers on`  | show column names in query results |
| `.once output.csv` | send *next* query result to a file |


## SQL In a nutshell

### Create a table

```sql
CREATE TABLE users (
  id             INTEGER PRIMARY KEY, 
  name           TEXT NOT NULL,
  email          TEXT UNIQUE,
  creation_date  TEXT DEFAULT CURRENT_TIMESTAMP
);
```

- Note: `INTEGER PRIMARY KEY` auto-increments the primary key
- Note: `TEXT DEFAULT CURRENT_TIMESTAMP` sets the field to the current time.
- Note: You'll need to add `IF NOT EXISTS` to `CREATE TABLE` pretty often when making apps.  You can probably guess why.
- Note: queries end with a semi-colon.


### Insert rows

```sql
INSERT INTO users (name, email) VALUES
  ('Mike', 'mike@example.com'),
  ('Matt', 'matt@example.com'),
  ('Mark', 'mark@example.com');
```

### 3.3 Basic selects

#### Want to get everything from a table?

use a star...

```sql
SELECT * FROM users;
```

#### Want to just get some fields?

separate them by a comma...

```sql
SELECT id, name
FROM users
WHERE name = 'mike'
ORDER BY creation_date DESC
LIMIT 1;
```

- BTW, remember how python doesn't care about singlq quotes or double quotes?  SQL DOES...
- BTW, remember how `=` was for assignment in python... well in sql it's comparison equals
- BTW, SQL is still case sensitive.  Use `LIKE` Operator for case insensitive... but that's not always the case!


### Update

```sql
UPDATE users
SET email = 'mike.corey@example.com'
WHERE name = 'Mike';
```


### Delete

```sql
DELETE FROM users
WHERE id = 3;
```

## What makes it relational...

```sql
CREATE TABLE posts (
  id            INTEGER PRIMARY KEY,
  user_id       INTEGER NOT NULL REFERENCES users(id),
  title         TEXT NOT NULL,
  body          TEXT,
  creation_date TEXT DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO posts (user_id, title, body) VALUES
  (1, 'Favorite Memes', 'That just use SQL one...'),
  (2, 'Something about Cats', 'cats are okay i guess...');
```

- `REFERENCES` keyword tells the table that it's related to a `TABLE(COLUMN)`


### Joins

Sometimes we want to select across multiple related tables.  To do this we can use joins.


```sql
SELECT u.name, p.title
FROM posts AS p
JOIN users AS u ON u.id = p.user_id
ORDER BY p.creation_date;
```

- `AS` keyword: creates an alias for more concise queries.
- `JOIN` table `ON` expression: merges two rows together if they match
- `ORDER BY`: this sorts the resulting rows by a specific column. In this case we're using posts.creation_date (instead of users which also has a creation_date)


## Indexes (indices)

We can create indicies to more quickly scan a table.  Without an index we can still query, but performance is slower as the table is fully scanned.  If we index, we can query more quickly.  If we use `WHERE` or `JOIN` frequently we should use an index.

```sql
CREATE INDEX idx_posts_user_id ON posts(user_id);
```

- Note: When querying we just query as usual.  i.e. we don't use a specific syntax because we added an index.

- Also, we're indexing the foreign key reference not the primary key.  (PK's are automatically indexed.)

- In fact, the only reason to know if we're using an index (besides a performance improvement) is using `EXPLAIN`.

```sql
-- Verify planner usage
EXPLAIN QUERY PLAN
SELECT * FROM posts WHERE user_id = 1;
```


## Transactions

We use transactions to ensure everything happened together or nothing happens at all, for example if we create a user and a post we can undo creating the user if creating the post fails... (in this case we accidentally set ALL user emails to NULL, yikes)

```sql
BEGIN;
UPDATE users SET email = NULL;
ROLLBACK;

BEGIN;
UPDATE users
SET email = 'mike.c@example.com'
WHERE id = 1;
COMMIT;                             
```

Note: `BEGIN;` starts a transaction, `ROLLBACK;` cancels it and rolls back the log to before `BEGIN`.  `COMMIT` writes everything from `BEGIN` to `COMMIT` to the log.


## Ok but this is a PYTHON course...

Again, Python comes with a module for interacting with sqlite dbs.

```python
import sqlite3
```

### Connecting

```python
conn = sqlite3.connect('demo.db') 
```

- we can also `:memory:` (normally) to make a database session that exists only while the app is alive.


### Selecting data

```python
with sqlite3.connect('demo.db') as conn:
    conn.row_factory = sqlite3.Row
    for row in conn.execute('SELECT id, name FROM users'):
        print(row['id'], row['name'])
```

- `with` again will ensure that we safely close our database.  Remember the file stuff.

### inserts

```python
posts = [
    (1, 'Floppy Disks',   'it\'s an article about this emoji... 💾'),
    (3, 'Trampoline Parks',   'An article about how exciting jumping is...')
]

with sqlite3.connect("demo.db") as conn:
    conn.executemany(
        "INSERT INTO posts (user_id, title, body) VALUES (?, ?, ?)",
        posts]
    )
```

- Of course this only works if we have a users and posts table


## The complete script

```python
import sqlite3

DB  = 'demo.db'

user_schema = '''
CREATE TABLE IF NOT EXISTS users (
  id             INTEGER PRIMARY KEY, 
  name           TEXT NOT NULL,
  email          TEXT UNIQUE,
  creation_date  TEXT DEFAULT CURRENT_TIMESTAMP
);
'''

posts_schema = '''
CREATE TABLE IF NOT EXISTS posts (
  id            INTEGER PRIMARY KEY,
  user_id       INTEGER NOT NULL REFERENCES users(id),
  title         TEXT NOT NULL,
  body          TEXT,
  creation_date TEXT DEFAULT CURRENT_TIMESTAMP
);
'''

with sqlite3.connect(DB) as conn:
    conn.executescript(users_schema)
    conn.executescript(posts_schema)

    users = [
        ('mike', 'mike@example.com'),
        ('matt', 'matt@example.com')
    ]

    posts = [
        (1, 'python is fun', 'python is the most fun programming language in the world...'),
        (2, 'libraries are relevant', 'You\'d be surprised at how relevant libraries stil are...')
    ]

    conn.executemany('INSERT INTO users (name, email) VALUES (?, ?)', users)

    conn.executemany('INSERT INTO posts (user_id, title, body) VALUES (?, ?, ?)', posts)

    
    cursor = conn.execute('''
        SELECT users.name, posts.title, posts.body
        FROM posts
        JOIN users ON users.id = posts.user_id
    ''')

    for row in cursor:
        print(row)

```
