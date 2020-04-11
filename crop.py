########## Crop Photo ############

#import cv2
#panda = cv2.imread('panda.jpg')
#recorte = panda[100:200, 100:200]
#cv2.imshow("crop da imagem", recorte)
#cv2.imwrite("crop.jpg", recorte) #gravaDisco
#cv2.waitKey(0)

########## Resize Photo ############
import numpy as np
import cv2

panda = cv2.imread('panda.jpg')
cv2.imshow("Original", panda)
largura = panda.shape[1]
altura = panda.shape[0]
proporcao = float (altura/largura)
nova_largura = 320 #pixels
nova_altura = int(nova_largura*proporcao)
novo_tamanho = (nova_largura, nova_altura)

panda_resize = cv2.resize(panda, novo_tamanho, interpolation = cv2.INTER_AREA)

cv2.imshow('Resultado', panda_resize)
cv2.waitKey(0)

########## Resize Photo com slicing ############
#import numpy as np
#import imutils
#import cv2

panda = cv2.imread('panda.jpg')
cv2.imshow("Original", panda)
panda_resize = panda [::2, ::2]

cv2.imshow("Foto redimensionada", panda_resize)
cv2.waitKey(0)










