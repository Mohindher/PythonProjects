import cv2 
cap=cv2.VideoCapture(0)
face_cascade =cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

while True:
    ## capture camera frame, and ret store true and false
    r, frame= cap.read()
    gray_frame =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    if r==False:
        continue
    faces=face_cascade.detectMultiScale(gray_frame,1.3,5)
  
    
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,125,0),2)## color and width 
        cv2.putText(frame,"DETECTED",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(100,125,255),1,cv2.LINE_AA)
    cv2.imshow("video frame",frame)
    key_pressed =cv2.waitKey(1) & 0xFF
   
    
    ### ord converts characters in unicode
    if key_pressed ==ord('n'):
        break
        
cap.release()
cv2.destroyAllWindows()
