import cv2
import dropbox
import time 
import random

start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)

    result=True

    while(result):
        ret,frame=videoCaptureObject.read()
        image_name="Img"+ str(number) + ".png"
        cv2.imWrite(image_name,frame)
        start_time=time.time
        result=False
    return image_name
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token="****"
    file=img_name
    fileFrom=file
    fileTo="/test/"+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(fileFrom, 'rb') as f:
            dbx.files_upload(f.read(),fileTo,mode=dropbox.files.WriteMode.overwrite)
            print("files uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)

if __name__ == "__main__":
    main()
    