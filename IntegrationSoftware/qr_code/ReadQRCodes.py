from PIL import Image, ImageDraw
from pyzbar.pyzbar import decode

def read_qr_codes(image_path):
    # Open the image file
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # Decode QR codes in the image
    qr_codes = decode(img)
    results = []

    # Extract and draw the bounding boxes
    for index, qr_code in enumerate(qr_codes, start=1):
        qr_data = qr_code.data.decode('utf-8')
        qr_rect = qr_code.rect
        position = {
            'x': qr_rect.left,
            'y': qr_rect.top,
            'width': qr_rect.width,
            'height': qr_rect.height
        }
        
        # Draw the bounding box on the image
        draw.rectangle([
            (position['x'], position['y']),
            (position['x'] + position['width'], position['y'] + position['height'])
        ], outline='red', width=7)
        
        results.append({
            'index': index,
            'data': qr_data,
            'position': position
        })

    # Save or show the image with bounding boxes
    img.save('annotated_image.png')  # Save with bounding boxes
    img.show()  # Display the image

    return results


