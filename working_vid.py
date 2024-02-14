import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (1280,720))
  
while True:
    ret, frame = cap.read() #return will tell wheather the video is stopped or running.
    out.write(frame)
    # print(ret)

    #To convert image to grayscale in webcam
    # img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY   )
    
    # cv2.imshow("webcam", img_gray)
    cv2.imshow("webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
out.release()
cv2.destroyAllWindows()