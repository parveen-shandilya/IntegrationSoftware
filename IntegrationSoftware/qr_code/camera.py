import cv2

def captureImage() :
    # Open the camera (0 for the default camera, 1 for an external camera, etc.)
    cap = cv2.VideoCapture(0)

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

