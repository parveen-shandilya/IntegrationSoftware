from flask import Flask
from qr_code.ReadQRCodes import read_qr_codes
app = Flask(__name__)


image_path = r"C:/Users/lenovo/Downloads/Pic_20240821173744693.bmp"



@app.route("/")
def ReadQR_Codes():
    l = read_qr_codes(image_path)
    return l

