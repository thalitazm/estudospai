# Importação biblioteca openCV
import cv2
# Leitura de uma imagem
imagem = cv2.imread('entrada.jpg')
print('Largura em pixels: ', end='')
print(imagem.shape[1]) # mostra a largura da imagem
print('Altura em pixels: ', end='')
print(imagem.shape[0]) # mostra altura da imagem
print('Qtde de canais: ', end='')
print(imagem.shape[2])
# imshow => mostrar imagem
cv2.imshow("Nome da janela", imagem)
cv2.waitKey(0) # fecha com qualquer tecla
# função imwrite() => salva a imagem em disco
cv2.imwrite("saida.jpg", imagem)

# Diz a lenda que se voce nao der um "hello, world" em alguma linguagem de programacao, muito
# provavel que voce nao ira aprender essa linguagem. Este eh um hello, world de imagem com a biblioteca openCV.
