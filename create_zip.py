import os
import keyboard
import time
import pyautogui

# unzip file stored in here
path_file = 'C:\\Users\\Safira\\Downloads\\test_ems'

os.startfile(path_file)
time.sleep(3)

# maximize window
keyboard.send('f11')

time.sleep(3)
pyautogui.rightClick(332,163)

# zip file by WinRar
time.sleep(2)
pyautogui.click(456,607)

# set password
time.sleep(2)
pyautogui.click(1021,735)

# enter password
pyautogui.typewrite('emsisoft', interval=0.25)

# re-enter password
pyautogui.click(792,525)
pyautogui.typewrite('emsisoft', interval=0.25)

# save password
time.sleep(2)
pyautogui.click(797,781)

# click OK
time.sleep(2)
pyautogui.click(1005,805)

time.sleep(2)
pyautogui.click(393,331)

# close windows explorer
time.sleep(2)
keyboard.send('alt+f4')
