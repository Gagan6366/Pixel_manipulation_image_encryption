# Pixel Manipulation Image Encryption

## Overview
This project demonstrates a method for encrypting images through pixel manipulation techniques. By altering pixel values, we can obfuscate image data, making it unreadable without the proper decryption algorithm.

## Features
- Image encryption using pixel manipulation techniques.
- Simple and intuitive user interface.
- Support for various image formats (e.g., JPEG, PNG).
- Decryption functionality to retrieve original images.
- Configurable encryption parameters for enhanced security.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Example](#example)
- [License](#license)

## Installation
To get started, clone this repository and install the required dependencies.

```bash
git clone https://github.com/Gagan6366/pixel_manipulation_image_encryption.git
cd pixel_manipulation_image_encryption

## Usage

To encrypt an image, run the following command:
python3 image_encrypter.py 

To decrypt an image, use:
python3 image_decrypter.py

## How It Works

    Pixel Manipulation: The encryption process modifies pixel values based on a secret key and a specified algorithm.
    Data Obfuscation: By changing pixel values, the original image becomes unreadable.
    Decryption: The reverse process restores the original image using the same secret key.

## Example

Here's a simple example of how to use the scripts provided:

    Encrypting an Image: python3 image_encrypter.py 
                         Enter path of Image : 
                         Enter Key for encryption of Image: 
                         The path of file:  
                         Key for encryption:  
                         Encryption Done...

    Decrypting the Image: python3 image_decrypter.py
                          Enter path of Image :/home/bug/Downloads/flower.jpg
                          Enter Key for encryption of Image: 12
                          The path of file:  /home/bug/Downloads/flower.jpg
                          Note: Encryption key and Decryption key must be same.
                          Key for Decryption:  12
                         Decryption Done...


