# Pixel Shuffle Image Encryptor

A simple Python tool to encrypt and decrypt images by shuffling pixel positions based on a secret numeric key.

---

## Disclaimer

This tool is for **educational purposes only**.  
Pixel shuffling provides basic obfuscation but is **not suitable for serious security applications**.  
Always use proper cryptography libraries (like AES) for real data protection.

---

## Theoretical Background

Traditional pixel manipulation methods (like adding or subtracting color values) are easy to reverse visually and don’t fully hide the image content.

**Pixel shuffling** is more secure for simple learning use cases:
- Treat the image as an array of pixels.
- Use a secret numeric key to seed a pseudo-random shuffle.
- Shuffle pixel positions randomly.
- Decrypt by regenerating the same shuffle order with the same key and reversing it.

---

## How It Works

- Load an image and convert it to RGB.  
- Flatten pixel data into a 1D list of `[R, G, B]` pixels.  
- Shuffle pixel positions using a pseudo-random order generated from the key.  
- Save the shuffled image as the encrypted version.  
- Decrypt by reshuffling in reverse using the same key.

---

## How to Use

### **Clone the Repo**

~~~
git clone https://github.com/mz-mukhtar/PRODIGY_CS_02.git
cd PRODIGY_CS_02
~~~

### Install Dependencies
~~~
pip install pillow numpy
~~~

### Run the Script
~~~
python encryptor.py
~~~
