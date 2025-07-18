from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
users = {
    1: {"name": "Alice", "age": 30},
    2: {"name": "Bob", "age": 25}
}

## Call 127.0.0.1:5005/users

# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

## Call 127.0.0.1:5005/users/1

# GET one user
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

## Post name and age to 127.0.0.1:5005/users {"name": "mike", "age": 21}

# POST create new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or "name" not in data or "age" not in data:
        return jsonify({"error": "Missing name or age"}), 400
    new_id = max(users.keys()) + 1
    users[new_id] = {"name": data["name"], "age": data["age"]}
    return jsonify({"id": new_id, "user": users[new_id]}), 201

## Put to 127.0.0.1:5005/users/1 {"name": "mike", "age": 21}

# PUT update existing user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    users[user_id].update(data)
    return jsonify(users[user_id])

if __name__ == "__main__":
    app.run(debug=True, port=5005)
