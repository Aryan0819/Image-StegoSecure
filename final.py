import cv2
import os
import string

img = cv2.imread(r"C:\hp\xyz\Screenshot 2025-01-10 155407.png")  # Replace with the correct image path

if img is None:
    print("Error: Image not found. Check the file path.")
    exit()

msg = input("Enter secret message:")
password = input("Enter a passcode:")

d = {}
for i in range(255):
    d[chr(i)] = i

m = 0
n = 0
z = 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.png", img)
os.system("start encryptedImage.png")  # Use 'start' to open the image on Windows
