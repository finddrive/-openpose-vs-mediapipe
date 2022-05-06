import cv2
import mediapipe as mp
import os
import time
import datetime
import posemodule as pm
import math

def squat(video_path):
    pTime = 0
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
        lmlist = detector.getPosition(img,draw=False)
        
        # if u want all dots then put draw= true and comment out the cv2.circle part in the if part below
        
        if len(lmlist)!=0:
            cv2.circle(img,(lmlist[25][1],lmlist[25][2]),10,(0,0,255),cv2.FILLED)
            cv2.circle(img,(lmlist[23][1],lmlist[23][2]),10,(0,0,255),cv2.FILLED) 
            #print(lmlist[23])
            y1 = lmlist[25][2]
            y2 = lmlist[23][2]
            
            length = y2-y1
            if length>=0 and f==0:
                f=1
            elif length<-50 and f==1:
                f=0
                count=count+1


            cTime = time.time()
            fps = 1/(cTime-pTime)
            pTime = cTime
            cv2.putText(img,"Total Number of Squats  "+str(int(count)),(70,50),cv2.FONT_HERSHEY_DUPLEX,1,(60,100,255),2)
            #cv2.putText(img,"Calories Burnt  "+str(int(count)*0.32),(70,150),cv2.FONT_HERSHEY_DUPLEX,1,(60,100,255),2)
            #img = cv2.resize(img, (900,900))                    # Resize image
            cv2.imshow("Image",img)
            #calories = 0.32*count
            if cv2.waitKey(2) & 0xFF == ord('q'):
                # cv2.destroyAllWindows()
                cap.release()
                cv2.destroyAllWindows()
                break
            
            
        #cv2.destroyWindow(windowname)
    curtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return curtime, "深蹲", count


if __name__ == '__main__':
    vid_path = "C:\\users\\yyg20\\OneDrive - zrmmg\\capstone\\test_vid"
    vid = vid_path + "\\suqat.mp4"
    print(squat(vid))  