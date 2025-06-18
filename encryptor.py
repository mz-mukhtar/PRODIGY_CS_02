from PIL import Image

def load_and_show_image(path):
    # Open the image
    img = Image.open(path)
    # Show the image in default image viewer
    img.show()

if __name__ == "__main__":
    # Example: replace 'sample.jpg' with your image filename
    load_and_show_image("sample.jpg")
