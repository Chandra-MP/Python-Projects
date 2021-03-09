import numpy 
import cv2 as cv 

cap=cv.VideoCapture(0)  
fps = cv.VideoCapture.get(cap, 5)
total = 0
print("The width of the video stream is: ", cap.get(3))
print("The height of the video stream is: ", cap.get(4))

while True: #cv.VideoCapture(0) returns a boolen true or false boolean, here it returns true to the cap variable;
    #capture frame by frame;
    ret, frame = cap.read() #cv.VideoCapture(0) aslo returns a boolean true value if read correctly;
    #checking if cap is initialized or not;
    if not cap.isOpened(): 
        cap.open()
    #Operations on the frame;    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #flipping
    #to flip image/frame, use 0 for flipping vertically, 1 for horizontally and -1 for both vertically and horizontally; 
    frame_flipped = cv.flip(frame,1) #flipped horizontally(1);
    gray_flipped = cv.flip(gray, 1) #flipped both horizontally and vertically;
    #display;
    cv.imshow('frame', gray_flipped)
    cv.imshow('RGB output', frame_flipped)
    
    key = cv.waitKey(1) &0xFF
    total+=1
    if key == 27:
        cv.destroyWindow('frame')
        cv.destroyWindow('RGB output')
        break

while cap:
    if not cap.isOpened():
        cap.open(1)
    ret1, frame1 = cap.read()
    ret1=cap.set(3,640)
    ret1=cap.set(4,480)
    cv.imshow("voila", frame1)
    key = cv.waitKey(1) &0XFF
    if key==113:
        break        
print("Total frames captured :", total)
print("FPS:",fps)
print("Everything exited successfully")

#when everything is done, realse the capture; 
cap.release()
cv.destroyAllWindows()        
