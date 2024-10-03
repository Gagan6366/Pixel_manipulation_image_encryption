Encrypting Image

# try block to handle exception
try:
  path = input (r'Enter path of Image : ')                        # take path of image as a input
  
  key = int(input('Enter Key for encryption of Image: '))           # taking encryption key as input

  print('The path of file: ', path)                                   

  print('Key for encryption: ', key)					# open file for reading purpose
  
  fin = open(path, 'rb')
  
  image = fin.read()							# storing image data in variable "image"
  fin.close()

  image = bytearray(image)            # performing XOR operation on each value of bytearray to perform encryption easily on numeric data
  for index, values in enumerate(image):
      
      image[index] = values ^ key
      
  fin = open(path, 'wb')				# opening file for writing purpose
  
  fin.write(image)				# writing encrypted data in image
  
  fin.close()
  print('Encryption Done...')
  
except Exception:
  print('Error caught: ', Exception.___name__)
