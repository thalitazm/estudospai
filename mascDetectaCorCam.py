import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #convert BGR to HSV

    # cor vermelha:
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

    # cor azul:
    claro = np.array([94, 80, 2])
    escuro = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, claro, escuro)
    detecta_azul = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # cor verde:
    minimo = np.array([25, 52, 72])
    maximo = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, minimo, maximo)
    detecta_verde = cv2.bitwise_and(frame, frame, mask=green_mask)

    #detecta qualquer cor, exceto branco:
    #low = np.array([0,42,0])
    #high = np.array([179, 255, 255])
    #mask = cv2.inRange(hsv_frame, low, high)
    #result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Frame", frame)
    cv2.imshow("Cor verde", detecta_verde) #mostraCor

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
