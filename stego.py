import cv2 #to run this you need to run pip install opencv-python
import os
import string

img = cv2.imread("mypic.jpg") # Replace with the correct image path#image

msg = input("Enter secret message:")
password = input("Enter a passcode:")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows

message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption")
if password == pas:
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")




#this code is for steganography and it is used to hide the message in the image. it will take the image and the message as input and then it will hide the message in the image and then it will save the image and then it will ask for the password and then it will decrypt the message and then it will print the message.
#the code is working fine and it is tested

