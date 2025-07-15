import sqlite3

DB  = 'demo.db'

users_schema = '''
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
