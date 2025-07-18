

Workspace: Collecting workspace information```markdown
# Steganography Image Encoder/Decoder

This project provides a simple Python script ([stego.py](stego.py)) for hiding (encoding) a secret message inside an image and then retrieving (decoding) it using a password. The process uses basic steganography techniques and OpenCV for image manipulation.

## Features

- Hide a secret message inside an image (`mypic.jpg`).
- Protect the message with a password.
- Save the encoded image as `encryptedImage.jpg`.
- Retrieve and display the hidden message after password verification.

## Requirements

- Python 3.x
- OpenCV for Python

Install OpenCV using pip:
```sh
pip install opencv-python
```

## Usage

1. Place your cover image as `mypic.jpg` in the project directory.
2. Run the script:
   ```sh
   python stego.py
   ```
3. Follow the prompts:
   - Enter the secret message to hide.
   - Enter a password for encryption.
   - The script will encode the message and save the result as `encryptedImage.jpg`.
   - The encoded image will open automatically (on Windows).
   - Enter the password again to decrypt and reveal the hidden message.

## How It Works

- Each character of your message is encoded into the pixel values of the image.
- The password is required to decrypt and reveal the message.
- The script modifies the RGB values of the image pixels to store the message.

## Files

- [`stego.py`](stego.py): Main script for encoding and decoding messages in images.
- `mypic.jpg`: The original image used for encoding (must be present in the directory).
- `encryptedImage.jpg`: The output image with the hidden message.
- `readme.md`: Project documentation.

## Limitations

- The length of the message is limited by the size of the image.
- The script currently works best on Windows for automatic image opening.
- No advanced steganography or encryption is used; this is for educational purposes only.

## Example

```
Enter secret message: hello
Enter a passcode: 1234
(encryptedImage.jpg is created and opened)
Enter passcode for Decryption: 1234
Decryption message: hello
```

## License

This project is for educational purposes.

```
