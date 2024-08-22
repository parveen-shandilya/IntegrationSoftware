# import cv2
# def read_qr_code(image):
#     qr_detector = cv2.QRCodeDetector()
#     img = cv2.imread(image)
#     r,di,p,s = qr_detector.detectAndDecodeMulti(img)
#     return di





import cv2
from pyzbar.pyzbar import decode

# Function to read and decode QR codes from an image
def read_qr_codes(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Decode the QR codes in the image
    qr_codes = decode(img)

    # Loop through detected QR codes and print their index and data
    for index, qr_code in enumerate(qr_codes):
        # Get the data from the QR code
        qr_data = qr_code.data.decode('utf-8')
        
        # Get the bounding box (if you need to know where in the image the QR code is)
        (x, y, w, h) = qr_code.rect
        
        print(f"QR Code {index + 1}:")
        print(f"Data: {qr_data}")
        print(f"Position: x={x}, y={y}, width={w}, height={h}")
        print("-" * 30)




# Specify the path to your image containing QR codes
image_path = r"C:/Users/lenovo/Downloads/Pic_20240821173744693.bmp"

# Call the function to read QR codes
read_qr_codes(image_path)
