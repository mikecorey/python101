# Flask (web servers)


## Overview

Flask is a micro-framework.  That means there's no heavy ORM or template engine liek Django (an alternative) would have.

Flask allows us to quickly build fast rest apis with minimal dependencies.

### installation

```bash
pip install flask
```

### Hello, Flask

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(port=5005, debug=True)
```

Visit `http://127.0.0.1:5005/`

Note the decorator.  Remember a decorator is a function that modifies the behavior of another function or method, without changing its source code.  Wrapping a function to add functionality.


##  “Users” API demo

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In‑memory “database”
users = {
    1: {"name": "Alice", "age": 30},
    2: {"name": "Bob",   "age": 25}
}

# GET /users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# GET /users/1
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# POST /users   { "name": "Mike", "age": 21 }
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or "name" not in data or "age" not in data:
        return jsonify({"error": "Missing name or age"}), 400
    new_id = max(users) + 1
    users[new_id] = {"name": data["name"], "age": data["age"]}
    return jsonify({"id": new_id, "user": users[new_id]}), 201

# PUT /users/1   { "age": 31 }
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    users[user_id].update(data)
    return jsonify(users[user_id])

if __name__ == "__main__":
    app.run(debug=True, port=5005)
```


---

##  Adding DELETE

```python
# DELETE /users/1
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = users.pop(user_id, None)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"deleted": user})
```

### CLI testing

```bash
curl -X DELETE http://127.0.0.1:5005/users/2
```

### Simple validation helper

```python
def validate_user(data):
    if not isinstance(data.get("name"), str):
        return False, "Name must be a string"
    if not (isinstance(data.get("age"), int) and data["age"] > 0):
        return False, "Age must be a positive integer"
    return True, ""
```

##  Blueprints — Routing Beyond One File

Create **users.py**

```python
from flask import Blueprint, request, jsonify

bp = Blueprint("users", __name__, url_prefix="/users")
_users = {1: {"name": "Alice", "age": 30}}

@bp.get("/")
def all_users():
    return jsonify(_users)

@bp.post("/")
def add_user():
    data = request.get_json()
    new_id = max(_users) + 1
    _users[new_id] = data
    return jsonify({"id": new_id, **data}), 201
```

Main **app.py**

```python
from flask import Flask
from users import bp as users_bp

app = Flask(__name__)
app.register_blueprint(users_bp)

if __name__ == "__main__":
    app.run(debug=True, port=5005)
```
