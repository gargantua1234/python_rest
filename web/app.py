from flask import Flask, jsonify
app = Flask(__name__)

message = {'value': 'Hello World'}

@app.route('/')
def hello_world():
  return jsonify(message)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
