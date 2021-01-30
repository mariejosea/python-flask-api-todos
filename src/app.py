from flask import Flask, jsonify, request, json

app = Flask(__name__) 
#Instancia de flask

todos = [
    {"label": "First task", "done": False}
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

#request objeto que representa la solicitud. (data) propiedad del objeto request.
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    return jsonify(todos)

#<int:position> variable 
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)