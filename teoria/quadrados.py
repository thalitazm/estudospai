import cv2
imagem = cv2.imread('entrada.jpg')
for y in range(0, imagem.shape[0], 10): #percorre linhas
    for x in range(0, imagem.shape[1], 10): #percorre colunas
        imagem[y:y+5, x: x+5] = (115,165,75) #verdepredomina
cv2.imshow("Imagem modificada", imagem)
cv2.imwrite("testeQuadrados.jpg", imagem)
cv2.waitKey(0)
