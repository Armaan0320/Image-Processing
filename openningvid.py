import cv2
import time

#openning an already existing video
cap = cv2.VideoCapture('----')

while True:
    ret, frame = cap.read()

    time.sleep(1/20)
    cv2.imshow("webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()