import cv2
picture = cv2.imread('entrada.jpg')

###### IMPORTANTE: slicing é para a criação de quadrados e retângulos! ###############

#retangulo azul em toda a largura da imagem:
picture[30:50, :] = (255, 0, 0)

#quadrado vermelho:
picture[100:150, 50:100] = (0, 0, 255)

#retangulo amarelo por toda a altura da imagem:
picture[:, 200:220] = (0, 255, 255)

#retangulo verde linhas 150 a 300 nas colunas 250 a 350:
picture[150:300, 250:350] = (0, 255, 0)

#retangulo ciano da linha 150 a 450 nas colunas 75 a 150:
picture[150:450, 75:150] = (255, 255, 0)

#quadrado branco
picture[250:350, 300:400] = (255, 255, 255)

#quadradopreto
picture[70:100, 300: 450] = (0, 0, 0)

cv2.imshow("Resultado", picture)
cv2.imwrite("Resultado.jpg", picture)
cv2.waitKey(0)
