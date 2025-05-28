import cv2
import cv2.data
import random
filename = "haarcascade_frontalface_default.xml"
path = cv2.data.haarcascades + filename
modal = cv2.CascadeClassifier(path)

cam = cv2.VideoCapture(0)

while True:
    status,image = cam.read()
    if status == False:
        print("camera is not supporting..")
        break
    faces = modal.detectMultiScale(image,1.3,5)
    for face in faces:
        x1 = face[0]
        y1 = face[1]
        x2 = x1 + face[2]
        y2 = y1 + face[3]
        b = random.randint(0,255)
        g = random.randint(0,255)
        r = random.randint(0,255)

        color = [b,g,r]

        cv2.rectangle(image,(x1,y1),(x2,y2),color,2)
        cv2.putText(image,
        "face",
        (x1,y1-20),
        cv2.FONT_HERSHEY_SIMPLEX,1,[255,255,255],2)
    cv2.imshow("facedeterction",image) 
    key = cv2.waitKey(1)
    if key == ord("g"):
        cv2.destroyAllWindows()
        break
cam.release()

