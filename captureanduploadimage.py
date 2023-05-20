import cv2
import dropbox
import time
import random

start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret , frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time()
        result = False
    
    return img_name
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token="sl.BeockEMJ8qZD4mn36WOER-Ho_GWPqmRoRp-eQPpvOps84VVJX9_IsAuN6NzHvtLmva4Zfj7dO-hCWWIipF0F_SBZJRvnrPzrn7eA-bEi5PUeypYdhtJeMTIhCZQkn05H6QYqRmM"
    file=img_name
    file_from=file
    file_to = "/newFolder1/"+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open (file_from,'rb') as d:
        dbx.files_upload(d.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time() - start_time)>=15):
             name = take_snapshot()
             upload_file(name)

main()
