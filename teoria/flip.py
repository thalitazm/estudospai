########## Flip image => Imagem Espelhada ############

import numpy as np
import cv2
panda = cv2.imread('panda.jpg')
cv2.imshow("Foto original", panda)
#flip_horizontal = panda[::-1,:] #comando equivalente a linha de baixo
flip_horizontal = cv2.flip(panda, 1)


cv2.imshow("Flip Horizontal", flip_horizontal)
#flip_vertical = panda[:,::-1] #comando equivalente a linha de baixo
flip_vertical = cv2.flip(panda,0)

cv2.imshow("Flip Vertical", flip_vertical)
#flip_hv = panda[::-1,::-1] #comando equivalente a linha de baixo
flip_hv = cv2.flip(panda, -1)
cv2.imshow("Flip Horizontal e Vertical", flip_hv)
cv2.waitKey(0)
