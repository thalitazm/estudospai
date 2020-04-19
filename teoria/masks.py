#imagem onde cada pixel pode estar ligado ou desligado

import cv2
import numpy as np

panda = cv2.imread('panda.jpg')
cv2.imshow("Original", panda)
mascara = np.zeros(panda.shape[:2], dtype = "uint8")
(cX, cY) = (panda.shape[1] // 2, panda.shape[0] // 2)
cv2.circle(mascara, (cX, cY), 100, 255, -1)
picmask = cv2.bitwise_and(panda, panda, mask = mascara)
cv2.imshow("Máscara aplicada à imagem", picmask)
cv2.waitKey(0)
