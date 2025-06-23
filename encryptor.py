from PIL import Image
import numpy as np
import random

def encrypt_image_shuffle(input_path, output_path, key):
    img = Image.open(input_path).convert("RGB")
    width, height = img.size

    pixels = np.array(img)
    flat_pixels = pixels.reshape(-1, 3)

    random.seed(key)
    indices = list(range(len(flat_pixels)))
    random.shuffle(indices)

    shuffled_pixels = flat_pixels[indices]
    shuffled_pixels = shuffled_pixels.reshape(height, width, 3)

    encrypted_img = Image.fromarray(shuffled_pixels.astype('uint8'))
    encrypted_img.save(output_path)
    print(f"Encrypted image saved as: {output_path}")

def decrypt_image_shuffle(input_path, output_path, key):
    img = Image.open(input_path).convert("RGB")
    width, height = img.size

    pixels = np.array(img)
    flat_pixels = pixels.reshape(-1, 3)

    random.seed(key)
    indices = list(range(len(flat_pixels)))
    random.shuffle(indices)

    unshuffled_pixels = np.empty_like(flat_pixels)
    for i, idx in enumerate(indices):
        unshuffled_pixels[idx] = flat_pixels[i]

    unshuffled_pixels = unshuffled_pixels.reshape(height, width, 3)

    decrypted_img = Image.fromarray(unshuffled_pixels.astype('uint8'))
    decrypted_img.save(output_path)
    print(f"Decrypted image saved as: {output_path}")

if __name__ == "__main__":
    # Simple user interface with input()
    action = input("What do you want to do? (encrypt/decrypt): ").strip().lower()
    input_path = input("Enter the input image path (e.g., sample.jpg): ").strip()
    output_path = input("Enter the output image path (e.g., result.jpg): ").strip()
    key = int(input("Enter your numeric key (e.g., 12345): ").strip())

    if action == "encrypt":
        encrypt_image_shuffle(input_path, output_path, key)
    elif action == "decrypt":
        decrypt_image_shuffle(input_path, output_path, key)
    else:
        print("Invalid option! Please choose 'encrypt' or 'decrypt'.")
