import cv2
import pyttsx3

video = cv2.VideoCapture(0)
audio = pyttsx3.init()

while (True):

    success, image = video.read()
    cv2.imshow('image', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        audio.say('Window closed successfully')
        audio.runAndWait()
        break
video.release()
cv2.destroyAllWindows()