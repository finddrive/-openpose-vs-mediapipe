import cv2
import mediapipe as mp
import os
import time
import datetime
import posemodule as pm
import math

def pushup(video_path):
    pTime = 0
    
    # Store the input video specifics
    cap = cv2.VideoCapture(video_path)
    n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))# 总帧数
    fps = int(cap.get(cv2.CAP_PROP_FPS))# 帧率信息
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    hight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    size = (width,hight)
    detector = pm.poseDetector()

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
        #print(lmlist[3])
        
        if len(lmlist)!=0:
            cv2.circle(img,(lmlist[14][1],lmlist[14][2]),10,(0,0,255),cv2.FILLED)
            cv2.circle(img,(lmlist[0][1],lmlist[0][2]),10,(0,0,255),cv2.FILLED) 
            y1 = lmlist[14][2]  #right_elbow
            y2 = lmlist[0][2]   #nose
            
            length = y2-y1
            if length>=0 and f==0:
                f=1
            elif length<-10 and f==1:
                f=0
                count=count+1

            cTime = time.time()
            fps = 1/(cTime-pTime)
            pTime = cTime
            if O_ret:
                #img = pm.vidCollages(img,O_img)
                cv2.putText(img,"Total push ups: {}".format(int(count)),(5,40),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
                cv2.imshow("Image",img)
                #output.write(img)

            if cv2.waitKey(2) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                break
            
            
            #calories = 0.29*count
    curtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return curtime, "俯卧撑", count


if __name__ == '__main__':
    vid_path = "C:\\users\\yyg20\\OneDrive - zrmmg\\capstone\\test_vid"
    vid = vid_path + "\\pushup2.mp4"
    print(pushup(vid))  