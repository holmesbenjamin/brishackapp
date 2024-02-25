from flask import Flask, request, jsonify
import json
import os
import base64
app = Flask(__name__)

@app.route('/test')
def test():
    return {"test": ["Blurb..."]}

@app.route('/upload', methods=['POST'])
def upload():
    string = request.json
    if "," in string:
        string = string.split(",")[1]
    print(request.json, flush=True) 
    path = "./uploads/test.jpeg"
    bdata= base64.b64decode(string)
    print(bdata, flush=True)
    with open(path, "wb") as f:
        f.write(bdata)
    return {"upload": request.json}

if __name__ == '__main__':
    app.run(debug=True)