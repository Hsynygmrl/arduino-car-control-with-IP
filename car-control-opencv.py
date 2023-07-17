import cv2
import HandTrackingModule as htm
import numpy as np
import time 
import serial
import math
import pyfirmata

# board=pyfirmata.Arduino('COM5')
# iter8 = pyfirmata.util.Iterator(board)
# iter8.start()

cap = cv2.VideoCapture(0) 
pTime = 0 
detector = htm.handDetector(detectionCon=0.7,maxHands= 1) # en fazla 1 el bul

vol = 0
volBar = 0
volPer = 0
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))   # float `width`
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw = False)
    cv2.rectangle(img,((width//2)+50,(height//2)+50),((width//2)-50,(height//2)-50),(0,0,0),cv2.FILLED)
    if len(lmList) != 0:
        x1,y1 = lmList[8][1] , lmList[8][2]
        cv2.circle(img,(x1,y1),10,(255,0,0),cv2.FILLED)
        if y1<(height//2)-50:
            cv2.putText(img,"FORWARD",(width-150,height-20),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),3)
            cv2.line(img,(0,height//2),(width,height//2),(255,255,255),2)
            # board.digital[5].write(1)
            # board.digital[3].write(1)
            # board.digital[2].write(0)
            # board.digital[4].write(0)

        elif y1>(height//2)+50:
            cv2.putText(img,"BACKWARD",(width-180,height-20),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),3)
            cv2.line(img,(0,height//2),(width,height//2),(255,255,255),2)
            # board.digital[5].write(0)
            # board.digital[3].write(0)
            # board.digital[2].write(1)
            # board.digital[4].write(1)

        elif x1>(width//2)+50:
            cv2.putText(img,"RIGHT",(width-150,height-20),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),3)
            cv2.line(img,(width//2,0),(width//2,height),(255,255,255),2)
            # board.digital[5].write(0)
            # board.digital[3].write(1)
            # board.digital[2].write(0)
            # board.digital[4].write(0)

        elif x1<(width//2)-50:
            cv2.putText(img,"LEFT",(width-180,height-20),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),3)
            cv2.line(img,(width//2,0),(width//2,height),(255,255,255),2)
            # board.digital[5].write(1)
            # board.digital[3].write(0)
            # board.digital[2].write(0)
            # board.digital[4].write(0)

        elif (width//2)-50<x1<(width//2)+50 and (height//2)-50<y1<(height//2)+50:
            cv2.putText(img,"STOP",(width-150,height-20),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),3)
            # board.digital[5].write(0)
            # board.digital[3].write(0)
            # board.digital[2].write(0)
            # board.digital[4].write(0)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40,70), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3)
    # img = cv2.resize(img,(900,600))
    cv2.imshow('Img',img)
    if  cv2.waitKey(20) & 0xFF == 27:
        break
cap.release()
# board.digital[5].write(0)
# board.digital[3].write(0)
# board.digital[2].write(0)
# board.digital[4].write(0)
cv2.destroyAllWindows()