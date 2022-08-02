# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sYCJuDsuPCOarJURbHFJetsv214PU9Gy
"""

import numpy as np
import cv2
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt

img = cv2.imread("/content/IMG_7385.JPG")

cv2_imshow(img)

gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 cv2_imshow(gray_scale)

histg = cv2.calcHist([img],[0],None,[256],[0,256])

plt.plot(histg)
plt.show()

kernel = np.ones((6,6),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

blur = cv2.GaussianBlur(img,(3,3),0)
cv2_imshow(blur)
# Apply Laplacian operator in some higher datatype
laplacian = cv2.Laplacian(blur,cv2.CV_64F)

#cv2_imshow(laplacian)

#edges = cv2.Canny(image=blur, threshold1=100, threshold2=200)
sobelx = cv2.Sobel(src=blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(src=blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
sobelxy = cv2.Sobel(src=blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
# Display Sobel Edge Detection Images
cv2_imshow(sobelx)
cv2.waitKey(0)



#cv2_imshow(edges)

cv2_imshow(sobely)
cv2.waitKey(0)

cv2_imshow(sobelxy)
cv2.waitKey(0)

edges = cv2.Canny(image=img, threshold1=10, threshold2=50)
cv2_imshow(edges)

