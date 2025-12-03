from PIL import Image, ImageDraw, ImageFont
import numpy as np

def create_image_with_hidden_message():
    # Create a new image with white background
    width, height = 600, 400
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Add some text to make it look like a normal image
    try:
        # Try to use a nice font if available
        font = ImageFont.truetype("arial.ttf", 24)
    except IOError:
        # Fallback to default font
        font = ImageFont.load_default()
    
    # Draw some text
    draw.text((50, 50), "Beautiful Landscape", fill="black", font=font)
    draw.text((50, 80), "A peaceful scene with a hidden message...", fill="gray", font=font)
    
    # Draw a simple landscape
    draw.rectangle([50, 150, 550, 350], fill="#87CEEB")  # Sky
    draw.rectangle([50, 350, 550, 400], fill="#2E8B57")  # Grass
    draw.ellipse([200, 200, 400, 300], fill="#FFD700")   # Sun
    
    # Convert image to RGB array
    img_array = np.array(img)
    
    # The message to hide (in binary)
    message = "CTF{st3g4n0gr4phy_1s_c00l}"
    binary_message = ''.join(format(ord(c), '08b') for c in message)
    
    # Add end of message marker
    binary_message += '00000000'  # Null terminator
    
    # Make sure the image is large enough to hold the message
    max_bits = img_array.shape[0] * img_array.shape[1] * 3
    if len(binary_message) > max_bits:
        raise ValueError("Message too long for the image")
    
    # Embed the message in the least significant bits
    bit_index = 0
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            for k in range(3):  # R, G, B channels
                if bit_index < len(binary_message):
                    # Clear the least significant bit and set it to the message bit
                    img_array[i, j, k] = (img_array[i, j, k] & 0xFE) | int(binary_message[bit_index])
                    bit_index += 1
                else:
                    break
            if bit_index >= len(binary_message):
                break
        if bit_index >= len(binary_message):
            break
    
    # Save the image
    result_img = Image.fromarray(img_array)
    result_img.save('hidden_message.png')
    print("Image with hidden message created: hidden_message.png")

if __name__ == "__main__":
    create_image_with_hidden_message()
