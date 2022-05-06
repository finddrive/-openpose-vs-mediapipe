import cv2
import mediapipe as mp
import os
import time
import datetime
import posemodule as pm
import math
import matplotlib.pyplot as plt

def crunch(video_path):
    pTime = 0
    
    # Store the input video specifics
    cap = cv2.VideoCapture(video_path)
    n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))# 总帧数
    fps = int(cap.get(cv2.CAP_PROP_FPS))# 帧率信息
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    hight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    size = (width,hight)
    detector = pm.poseDetector()

    #up3 y500
    # down 1000
    # up15 1100
    #  down 1100
    def rescale_frame(frame, percent=75):
        width = int(frame.shape[1] * percent/ 100)
        height = int(frame.shape[0] * percent/ 100)
        dim = (width, height)
        return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)


    count = 0

    f=0
    time.sleep(5)
    while cap.isOpened():
        success, img = cap.read()

        if not success:
            print("Ignoring empty camera frame.")
            break
        
        if( width>=800 or hight >=800 ):
            img = cv2.resize(img, (int(width/2),int(hight/2)))
        img = detector.findPose(img)
        lmlist = detector.getPosition(img)
        #print(lmlist[3])
        
        if len(lmlist)!=0:
            #cv2.circle(img,(lmlist[15][1],lmlist[15][2]),10,(0,0,255),cv2.FILLED)
            #cv2.circle(img,(lmlist[3][1],lmlist[3][2]),10,(0,0,255),cv2.FILLED) 
            x1 = lmlist[0][1]
            x2 = lmlist[12][1]
            
            length = x1-x2
            if length>=2 and f==0:
                f=1
            elif length<2 and f==1:
                f=0
                count=count+1


            cTime = time.time()
            fps = 1/(cTime-pTime)
            pTime = cTime
            cv2.putText(img,"Total Number of Crunches  "+str(int(count)),(70,50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(60,100,255),2)
            cv2.imshow("Image",img)
            
            if cv2.waitKey(2) & 0xFF == ord('q'):
                # cv2.destroyAllWindows()
                cap.release()
                cv2.destroyAllWindows()
                break
            
    curtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  

    return curtime, "卷腹", count,     
    

if __name__ == '__main__':
    vid_path = "C:\\users\\yyg20\\OneDrive - zrmmg\\capstone\\test_vid"
    vid = vid_path + "\\crunches.mp4"
    t = crunch(vid)
    print(t)   
    

