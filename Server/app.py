from flask import Flask,request,jsonify
from flask_cors import CORS
import pickle as pkl 

app = Flask(__name__)
with open('Server/spam.pkl', 'rb') as file:  # relative path to spam.pkl
    model = pkl.load(file)

CORS(app)

@app.route('/api/v1/', methods=['GET'])
def calculate():
     return jsonify({
          "message ": "server is started😍"
     })
@app.route('/api/v1/detect', methods=['POST'])
def Detect():
     message = request.get_json("message")
     prediction = model.predict([message['message']])[0]
     return jsonify({
          "1 ": message['message'],
          "prediction": prediction
     })



if __name__ == '__main__':
     app.run(debug=True, host='localhost', port=4300)