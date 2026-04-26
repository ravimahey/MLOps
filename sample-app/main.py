from flask import Flask, render_template, jsonify
import requests
from flask import request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET'])
def form():
    return render_template('form.html')

# Post Method
@app.route('/submit', methods=['POST'])
def submit():
    print(request.form)
    print(request.form['name'])
    print(request.form['email'])
    return "Form Submitted"

# Todo List
items =[
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"},
    {"id": 3, "name": "Item 3", "description": "This is item 3"},
]

@app.route('/items', methods=['GET'])
def get_items():
    return {"items": items}

@app.route('/item/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return item
    else:
        return jsonify({"error": "Item not found"}), 404

@app.route('/item', methods=['POST'])
def create_item():
    # get json from request

    data = request.get_json()
    print(data)

    new_item = {
        "name": data['name'],
        "description": data['description'],
        "id": len(items) + 1
    }
    # items.append(new_item)
    return {"item": new_item}, 201

@app.route('/item/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return {"message": "Item deleted"}

@app.route('/item/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    for item in items:
        if item["id"] == item_id:
            item["name"] = data['name']
            item["description"] = data['description']
            return {"item": item}
    return jsonify({"error": "Item not found"}), 404

@app.route('/todo', methods=['GET'])
def todo():
    return render_template('todo.html')
# Wsgi server
if __name__ == '__main__':
    app.run(debug=True)
