from flask import Flask, jsonify, request

app = Flask(__name__)

# Preloaded data (in-memory, no database)
users = [
    {"id": i, "name": f"User{i}", "role": "admin" if i % 10 == 0 else "user"}
    for i in range(1, 101)
]

products = [
    {"id": 100 + i, "name": f"Product{i}", "price": (i * 10) % 500 + 50}
    for i in range(1, 201)
]


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200


@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or "name" not in data or "role" not in data:
        return jsonify({"error": "Invalid payload"}), 400

    new_id = max(u["id"] for u in users) + 1
    new_user = {"id": new_id, "name": data["name"], "role": data["role"]}
    users.append(new_user)
    return jsonify(new_user), 201


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    user.update({k: v for k, v in data.items() if k in ["name", "role"]})
    return jsonify(user)


@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)


@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404


@app.route("/products", methods=["POST"])
def create_product():
    data = request.get_json()
    if not data or "name" not in data or "price" not in data:
        return jsonify({"error": "Invalid payload"}), 400

    new_id = max(p["id"] for p in products) + 1
    new_product = {"id": new_id, "name": data["name"], "price": data["price"]}
    products.append(new_product)
    return jsonify(new_product), 201


@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json()
    product.update({k: v for k, v in data.items() if k in ["name", "price"]})
    return jsonify(product)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
