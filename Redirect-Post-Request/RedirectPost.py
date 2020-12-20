#!/usr/bin/python

import json
from flask import Flask, request, jsonify
import requests

APP = Flask(__name__)

API_ENDPOINT = "http://habib.com/test"
headers = {'Content-type':'application/json', 'Accept':'application/json'}

@APP.route('/sendsms',methods=['POST'])
def main():
    phone = request.json["phone"]
    message = request.json["message"]
    NewData = {'phone':phone, 'text':message, 'hide':'true'}
    response = requests.post(url = API_ENDPOINT, json=NewData, headers=headers)
    return jsonify(Success='true', Number=phone, Content=message)

APP.run(host='0.0.0.0', port=5000)