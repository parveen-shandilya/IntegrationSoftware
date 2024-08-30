import cv2

from flask import Flask, send_file, jsonify, request
from daheng_sdk import Camera  # Assuming there's a Python SDK provided
import os

def captureImage() :
    # Open the camera (0 for the default camera, 1 for an external camera, etc.)
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

# Capture a single frame    
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        exit()

# Display the captured image
    cv2.imshow('Captured Image', frame)

# Save the captured image
    image_path = 'captured_image.jpg'
    cv2.imwrite(image_path, frame)

    print(f"Image saved to {image_path}")

# Wait for a key press and then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Release the camera
    cap.release()
# return image Path 
    return image_path    




   #app = Flask(__name__)

   # Initialize the camera
camera = Camera()
camera.initialize()

  
def capture_image():
    image_path = 'captured_image.jpg'
    camera.capture(image_path)  # Capture and save image to a file
       
       # Assuming further processing is needed
    processed_image_path = process_image(image_path)  # Your processing function
       
    return processed_image_path

def process_image(image_path):
       # Implement your image processing here, like QR code scanning, etc.
       # For now, just returning the original image as an example
    return image_path

   
   

   
     









#captureImage()