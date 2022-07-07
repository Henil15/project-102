import cv2
from cv2 import VideoCapture
import dropbox
import time
import random
def take_snapshot():
    number = random.randint(0,100)
    VideoCaptureObject=cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = VideoCaptureObject.read()
        img_name = "img" + str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
    return img_name    
    VideoCaptureObject.release()
    cv2.destroyAllWindows()                           
take_snapshot()

def upload_file(img_name):
    access_token = "sl.BKOFvg7b2TYdHB-136piUjm-TpoeDwb8YLm9icYLB2maT76nut-dv5x4kde3tkcgA1wfo21niK1RrOESfi8TAsFnlO3lFpZF177n8zDiqZy_WTw294THe9a_rfX4YK3MOz5GkG8"
    file = img_name
    file_from = file
    file_to = "/newfolder1" + (img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from , 'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")