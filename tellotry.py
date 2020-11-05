from djitellopy import Tello
import cv2
import time

tello = Tello()
tello.connect()
print(tello.get_battery())
tello.streamon()


while True:
    img = tello.get_frame_read()
    count = 0

    tello.takeoff()
    time.sleep(4)
    n = 0
    p = 1
    while count < 4:
        tello.rotate_clockwise(90)
        time.sleep(3)
        tello.move_forward(90)
        cv2.imwrite(f'move{n}.png', img.frame)
        time.sleep(3)
        tello.move_forward(10)
        cv2.imwrite(f'move{p}.png', img.frame)
        time.sleep(3)
        count += 1
        n += 2
        p += 2
    tello.rotate_clockwise(90)
    time.sleep(3)
    tello.land()
    print(tello.get_battery())
    break