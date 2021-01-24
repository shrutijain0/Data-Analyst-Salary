# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 15:45:39 2021

@author: milin
"""


import flask
from flask import Flask, jsonify, request
import json
from data_in import data_input
import numpy as np
import pickle



def load_models():
    file_name = "models/classifier.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

app = Flask(__name__)
@app.route('/predict', methods=['GET'])
def predict():
    # stub input features
    request_json = request.get_json()
    x = request_json['input']
    #print(x)
    x_in = np.array(x).reshape(1,-1)
    # load model
    model = load_models()
    prediction = model.predict(x_in)[0]
    response = json.dumps({'response': prediction})
    return response, 200

if __name__ == '__main__':
    application.run(debug=True)