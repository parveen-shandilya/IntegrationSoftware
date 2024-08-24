import cv2
from flask import Flask, jsonify ,render_template,url_for,send_file
import numpy as np
from qr_code.ReadQRCodes import read_qr_codes
from flask import request
import os
from flask_cors import CORS
import base64

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploaded_images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def readcodes(image_path,bottles):
    l = read_qr_codes(image_path,bottles)
    return l



@app.route("/readQRs", methods=['POST'])
def ReadQR_Codes():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    uploaded_file = request.files['file']
    
    if uploaded_file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400

    # Now you can pass the image to your QR code reader function
    l,p = readcodes(uploaded_file, 24)
    with open(p, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    # print(l,encoded_string)
    
    return jsonify({"data":l,"image":encoded_string})

@app.route('/get-image')
def get_image(image_name):
    return send_file(image_name, mimetype='image/jpeg')