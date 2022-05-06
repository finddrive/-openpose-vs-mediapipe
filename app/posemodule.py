import cv2
import mediapipe as mp
import os
import time
import numpy as np
import math


class poseDetector():
    def __init__(self,mode= False, upBody= False,smooth = True,detectionCon = 0.5,trackCon=0.5):
            

                self.mode = mode
                self.upBody = upBody
                self.smooth = smooth
                self.detectionCon = detectionCon
                self.trackCon = trackCon

                self.mpDraw = mp.solutions.drawing_utils

                self.mpPose = mp.solutions.pose
                self.pose = self.mpPose.Pose(static_image_mode=False,  min_detection_confidence=0.5)
                
                


    def findPose(self,img,draw = True): #画图
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        #print(results.pose_landmarks)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img,self.results.pose_landmarks,self.mpPose.POSE_CONNECTIONS,
                                self.mpDraw.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                self.mpDraw.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=1) 
                                ) 

        return img
        

    def getPosition(self,img,draw =True):
        self.lmlist = []
        if self.results.pose_landmarks:

            for id,lm in enumerate(self.results.pose_landmarks.landmark):
                h, w ,c = img.shape
                cx,cy = int(lm.x*w) ,int(lm.y*h)
                self.lmlist.append([id,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
            

        return self.lmlist

    def find_angle(self, img, p1, p2, p3, draw=True):
        '''
        :param p1\2\3: 第1\2\3个点
        :param draw: 是否画出3个点的连接图
        :return: 角度
        '''
        x1, y1 = self.lmlist[p1][1], self.lmlist[p1][2]
        x2, y2 = self.lmlist[p2][1], self.lmlist[p2][2]
        x3, y3 = self.lmlist[p3][1], self.lmlist[p3][2]

        # 使用三角函数公式获取3个点p1-p2-p3，以p2为角的角度值，0-180度之间
        angle = int(math.degrees(math.atan2(y1 - y2, x1 - x2) - math.atan2(y3 - y2, x3 - x2)))
        if angle < 0:
            angle = angle + 360
        if angle > 180:
            angle = 360 - angle

        if draw:
            cv2.circle(img, (x1, y1), 20, (0, 255, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 30, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 20, (0, 255, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255, 3))
            cv2.line(img, (x2, y2), (x3, y3), (255, 255, 255, 3))
            cv2.putText(img, str(angle), (x2 - 50, y2 + 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2)

        return angle


def vidCollages(frameL,frameR):
    frameLeft = cv2.resize(frameL, (500,400), interpolation=cv2.INTER_CUBIC)
    frameRight = cv2.resize(frameR, (500,400), interpolation=cv2.INTER_CUBIC)
    frameUp = np.hstack((frameLeft, frameRight))
    return frameUp

    

def main():
    pTime = 0
    path = os.path.dirname(os.path.realpath(__file__))+'/videos/'+'squats1.mp4'
    cap = cv2.VideoCapture(path)
    detector = poseDetector()
    
    

    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmlist = detector.getPosition(img,draw=False)
        # if(len(lmlist)!=0):
        #     print(lmlist[14])
        #     cv2.circle(img,(lmlist[14][1],lmlist[14][2]),10,(0,0,255),cv2.FILLED)
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,
        (255,0,0),3)
        # img = cv2.resize(img, (1100,1100))
        cv2.imshow("Image",img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()