from PIL import ImageGrab
import time
import pyautogui

time.sleep(3)

pyautogui.press("space")

left = 600
right = 750
top = 660
bottom = 695

while True:
    image = ImageGrab.grab()
    obstacle_detected = False

    for x in range(left,right,5):
        for y in range(top,bottom,5):

            pixel = image.getpixel((x,y))

            if all(value < 100 for value in pixel[:3]):

                obstacle_detected = True
                break
        if obstacle_detected:
            break
    if obstacle_detected:
        pyautogui.press("space")
        time.sleep(0.1)
    time.sleep(0.01)







