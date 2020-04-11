import cv2
import numpy as np

#affine => possui conexão // uma rotação é um tipo de transformaão affine

panda = cv2.imread('panda.jpg')
(alt, lar) = panda.shape[:2] #captura largura e altura
centro = (lar // 2, alt // 2) #acha o centro

M = cv2.getRotationMatrix2D(centro, 30, 1.0) #rotaciona 30 graus
panda_rotate = cv2.warpAffine(panda, M[(lar, alt)])

cv2.imshow("Panda rotate", panda_rotate)
cv2.waitKey(0)



