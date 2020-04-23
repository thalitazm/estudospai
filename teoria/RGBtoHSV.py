import cv2
import numpy as np

vermelhoRGB = np.uint8([[[160, 100, 100]]])
vermelhoHSV = cv2.cvtColor(vermelhoRGB, cv2.COLOR_BGR2HSV)

verdeRGB = np.uint8([[[0, 255, 0]]])
verdeHSV = cv2.cvtColor(verdeRGB, cv2.COLOR_BGR2HSV)

azulRGB = np.uint8([[[140, 255, 255]]])
azulHSV = cv2.cvtColor(azulRGB, cv2.COLOR_BGR2HSV)

amareloRGB = np.uint8([[[50, 255, 255]]])
amareloHSV = cv2.cvtColor(amareloRGB, cv2.COLOR_BGR2HSV)

print("Conversão de vermelho RGB para vermelho HSV:", vermelhoHSV)
print("Conversão de verde RGB para verde HSV:", verdeHSV)
print("Conversão de azul RGB para azul HSV: ", azulHSV)

print("Conversão de amarelo RGB para amarelo HSV: ", amareloHSV)