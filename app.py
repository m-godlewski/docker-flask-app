from flask import Flask, jsonify
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

@app.route("/", methods=["GET"])
def test():
    return jsonify({'response':'blue whale'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
