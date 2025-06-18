from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img = img.convert("RGB")

    width, height = img.size
    encrypted_img = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))

            r_enc = (r + key) % 256
            g_enc = (g + key) % 256
            b_enc = (b + key) % 256

            encrypted_img.putpixel((x, y), (r_enc, g_enc, b_enc))

    encrypted_img.save(output_path)
    print(f"Encrypted image saved as: {output_path}")

if __name__ == "__main__":
    encrypt_image("sample.jpg", "encrypted_sample.jpg", key=50)