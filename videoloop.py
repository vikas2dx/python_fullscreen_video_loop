import cv2
widow_name="window"
videoFileName="video.mp4"
#Loop for playing video in repeat model
while True:
    isClose=False
    video=cv2.VideoCapture(videoFileName)
    #Set Video Frame to Full Screen
    cv2.namedWindow(widow_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(widow_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    #Loop for Reading Video Frame
    while(True):
       ret, frame=video.read()   
       if(ret==True):
           cv2.imshow(widow_name,frame)
           #Esc button(27) to exit the video
           if(cv2.waitKey(1)==27):
               isClose=True
               break
       else:
           break
    #Close Repeat Video Loop
    if(isClose):
        break
# Release video and destory frame after ESC press
video.release()
cv2.destroyAllWindows()    