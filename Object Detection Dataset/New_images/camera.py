from picamera import PiCamera
from time import sleep
from datetime import datetime

num = 5
camera = PiCamera()
camera.start_preview()

while (num >= 1):
    print(num)
    sleep(1)
    num -= 1

pictureName = 'image_' + str(datetime.now()) + '.jpg'
camera.capture(pictureName)
print('picture taken')
camera.stop_preview()