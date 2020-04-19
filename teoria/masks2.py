import cv2
import numpy as np

rasp = cv2.imread('entrada.jpg')
cv2.imshow("Original", rasp)

mascara = np.zeros(rasp.shape[:2], dtype = "uint8")
(cX, cY) = (rasp.shape[1] //2, rasp.shape[0] //2)
cv2.circle(mascara, (cX, cY), 180, 255, 70)
cv2.circle(mascara, (cX, cY), 70, 255, -1)
cv2.imshow("Máscara", mascara)

picmask = cv2.bitwise_and (rasp, rasp, mask = mascara)
cv2.imshow("Aplicação de máscara à imagem", picmask)
cv2.waitKey(0)
