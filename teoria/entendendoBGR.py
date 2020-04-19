############### Estudo 01 ############################

import cv2
#imagem = cv2.imread('entrada.jpg')
#(b,g,r) = imagem[0, 0] #importante! BGR e nao RGB
#print ('O pixel (0,0) tem as seguintes cores:')
#print('Vermelho:', r, 'Verde:', g, 'Azul:', b)
#cv2.imshow("Imagem modificada", imagem)
#cv2.waitKey(0) => se quiser testar, retire o jogo da velha ali no do começo de todas as linhas e coloque antes da seta; o código está funcionando ;)


############### Estudo 02 ############################

#varredura de pixels com lacos de repeticao:
#substitucao dos pixels pela cor azul

#import cv2
#imagem = cv2.imread('entrada.jpg')
#for y in range(0, imagem.shape[0]):
#    for x in range(0, imagem.shape[1]):
#        imagem[y, x] = (255,0,0)
#cv2.imshow("Imagem modificada", imagem)
#cv2.waitKey(0) => se quiser testar, retire o jogo da velha ali no do começo de todas as linhas e coloque antes da seta; o código está funcionando ;)

############### Estudo 03 ############################
#import cv2
#imagem = cv2.imread('entrada.jpg')
#for y in range(0, imagem.shape[0]): #percorre linhas
#    for x in range(0, imagem.shape[1]): #percorre colunas
#        imagem[y, x] = (x%256, y%256, x%256)
#cv2.imshow("Imagem modificada", imagem)
#cv2.waitKey(0) => se quiser testar, retire o jogo da velha ali no do começo de todas as linhas e coloque antes da seta; o código está funcionando ;)

############### Estudo 04 ############################
imagem = cv2.imread('entrada.jpg')
for y in range (0, imagem.shape[0], 1): #percorre as linhas
    for x in range (0, imagem.shape[1], 1): #percorre as colunas
        imagem[y, x] = (0, (x*y)%256,0)
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)
