import numpy as np
import cv2
import base64
import os
import json
from flask import Flask
from flask import request
import os
import json

from WeJRcount import JRcount
from Wepushup import pushup
from Wepullup import pullup
from Wecrunch import crunch
from Wesquat import squat

app = Flask(__name__)

def jumprpoe_count(video):
    tmp = JRcount(video)
    return tmp

def pushup_count(video):
    tmp = pushup(video)
    return tmp

def pullup_count(video):
    tmp = pullup(video)
    return tmp

def crunch_count(video):
    tmp = crunch(video)
    return tmp    

def squat_count(video):
    tmp = squat(video)
    return tmp    


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/uploadvid", methods=["POST"])
def get_upload_video():
    print(request)
    up_video = base64.b64decode(request.form.get("video"))  #base64进行解码还原。    
    with open("1.mp4","wb") as f:                           #存入，存入地址为服务器中的项目地址。
         f.write(up_video) 

    type = request.form.get("info")
    print(type)
    tep=[]
    if type == '跳绳':
        tep = jumprpoe_count("1.mp4")

    if type == '俯卧撑':
        tep = pushup_count("1.mp4")

    if type == '引体向上':
        tep = pullup_count("1.mp4")

    if type == '卷腹':
        tep = crunch_count("1.mp4")    

    if type == '深蹲':
        tep = squat_count("1.mp4")        

    os.remove("1.mp4")
    print(tep)
    
    return dict(date=str(tep[0]), type=str(tep[1]), count=str(tep[2]))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

    