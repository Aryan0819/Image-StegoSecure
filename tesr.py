import cv2
import os
import string

img = cv2.imread("encryptedImage.png")
if img is None:
    print("Error: Encrypted image not found.")
    exit()

message = ""
n = 0
m = 0
z = 0

password = input("Enter a passcode for decryption: ")
original_password = input("Re-enter the original passcode: ")  # Simulating the original encryption passcode
c = {}
for i in range(255):
    c[i] = chr(i)

if password == original_password:
    msg_length = int(input("Enter the length of the original message: "))  # Ensuring correct decryption length
    for i in range(msg_length):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")