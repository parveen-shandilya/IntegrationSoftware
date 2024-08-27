import os
import time
import cv2
import random as rd

def captureImage() :
    # Open the camera (0 for the default camera, 1 for an external camera, etc.)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()
    print("Wait for Object position")
    time.sleep(5)
# Capture a single frame    
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        exit()

# Display the captured image
    #cv2.imshow('Captured Image', frame)

# Save the captured image
    image_path = 'captured_image' + str(rd.randint(10,100)) +'.jpg'
    cv2.imwrite(image_path, frame)

    print(f"Image saved to {image_path}")

# Wait for a key press and then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Release the camera
    cap.release()
# return image Path 
    return image_path  



def deleteCapturedImage(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print("Image deleted.")
    else:
        print("The file does not exist.")




image = captureImage() 
#deleteCapturedImage(image) 

