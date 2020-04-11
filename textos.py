import numpy as np
import cv2
#encoding: utf-8
rasp = cv2.imread('entrada.jpg')

charactere = cv2.QT_FONT_NORMAL
cv2.putText(rasp, 'Python is soooooo cool!!!', (25,65), charactere, 2, (135, 165, 45), 2, cv2.LINE_AA)

cv2.imshow("Raspberry", rasp)
cv2.imwrite("testeTexto.jpg", rasp)
cv2.waitKey(0)

