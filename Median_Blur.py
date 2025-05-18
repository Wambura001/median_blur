import cv2
import numpy as np 
import matplotlib.pyplot as plt 

path = r"C:\Users\USER\Pictures\Screenshots\Screenshot 2025-03-15 161038.png"
image = cv2.imread(path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
median_blur = cv2.medianBlur(image, 5)

plt.subplot(121), plt.imshow(image), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(median_blur), plt.title('Median Blur'),
plt.xticks([]), plt.yticks([])
plt.show()
