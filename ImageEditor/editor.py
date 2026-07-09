from PIL import Image, ImageEnhance, ImageFilter

def edit_image(path, output):
    # Open your uploaded image
    img = Image.open(path)

    # Resize
    img = img.resize((400, 400))

    # Rotate
    img = img.rotate(45)

    # Apply filter
    img = img.filter(ImageFilter.BLUR)

    # Enhance brightness
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.5)

    # Show image immediately
    img.show()

    # Save edited image
    img.save(output)
    print(f"Edited image saved as {output}")

if __name__ == "__main__":
    edit_image("img.jpg", "output.jpg")
