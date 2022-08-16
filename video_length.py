import cv2 as cv
import math
vidcapture = cv.VideoCapture('C:\\Users\\DimitriosKasderidis\\Desktop\Editing Software\\samples\\tahm.mp4')
fps = vidcapture.get(cv.CAP_PROP_FPS)
totalNoFrames = vidcapture.get(cv.CAP_PROP_FRAME_COUNT)
durationInSeconds = totalNoFrames / fps
durationInMinutes = durationInSeconds/60

print("durationInSeconds:", durationInSeconds, "s")
print("durationInMinutes:", durationInMinutes, "m")

print(durationInSeconds/39)