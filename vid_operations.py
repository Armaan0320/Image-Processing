#accessing mobile's camers using IP


import cv2

camera = "http://192.168.1.6:8080/shot.mp4"
cap = cv2.VideoCapture(camera)  # Open your mobile's camera.

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (1280, 720))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Colorframe', frame)
        out.write(frame)  # Write the frame to the output file.
        if cv2.waitKey(0) & 0xFF == ord('x'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

# # Import essential libraries 
# import requests 

# import numpy as np 


# # While loop to continuously fetching data from the Url 
# while True: 
# 	img_resp = requests.get(url) 
# 	img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8) 
# 	img = cv2.imdecode(img_arr, -1) 
# 	img = imutils.resize(img, width=1000, height=1800) 
# 	cv2.imshow("Android_cam", img) 

# 	# Press Esc key to exit 
# 	if cv2.waitKey(1) & 0xFF == ord('x'): 
# 		break

# cv2.destroyAllWindows() 
