import cv2 as cv
import numpy as np

cap = cv.VideoCapture("samples/swain.mp4")

if (cap.isOpened()== False): 
  print("Error opening video  file")

video_on_off = input("Press 1 for Video 0 for no Video: ")
video_on_off = int(video_on_off)

if(video_on_off == 1):
  print("Video has been turned on")
  show_video = True
else:
  show_video = False
  print("Video has been turned ")



while(cap.isOpened()):

    ret, frame = cap.read()
    if ret == True:

        new_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        width =  new_frame.shape[1]
        height = new_frame.shape[0]

        if(new_frame.shape[1] != 1920 or new_frame.shape[0] != 1080):
          new_width  = 1920
          new_height = 1080
          #width = [1], height = [0]
          print("Width pre change: ", new_frame.shape[1], "and Height pre change: ", new_frame.shape[0])
          new_frame = cv.resize(new_frame, (new_width, new_height)) 
                                     #height #width 
          focus_in_score = new_frame[0:25, int(new_width/2)+705:new_width-180]
          (thresh, black_and_white_image) = cv.threshold(focus_in_score, 100, 255, cv.THRESH_BINARY )

        else:
          focus_in_score = new_frame[0:25, int(width/2)+705:width-180]
          (thresh, black_and_white_image) = cv.threshold(focus_in_score, 100, 255, cv.THRESH_BINARY )


        if(show_video):
          cv.imshow("Video", black_and_white_image)

    if cv.waitKey(25) & 0xFF == ord('q'):
        break
   
   
cap.release()
cv.destroyAllWindows()



