import numpy as np
import cv2

rasp = cv2.imread('entrada.jpg')
cv2.imshow("Picture", rasp)

gray = cv2.cvtColor(rasp, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
hsv = cv2.cvtColor(rasp, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv) # => muito importante para detecção de cor!!!

#lab = cv2.cvtColor(rasp, cv2.COLOR_BGR2LAB)
#cv2.imshow("L*a*b*", lab)
cv2.waitKey(0)
