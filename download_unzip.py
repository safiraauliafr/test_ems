from selenium import webdriver
from selenium.webdriver.common.by import By
from pywinauto import Application, Desktop
import pyautogui
import time
import keyboard

driver = webdriver.Chrome(executable_path = 'C:\\Users\\Safira\\Desktop\\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(15)
driver.maximize_window()

# download zip file in idrive
driver.get('https://www.idrive.com/idrive/sh/sh?k=j3z6r9f1t3')
driver.find_element(By.NAME, value='password').send_keys('safira')
driver.find_element(By.ID, value='password_submit').click()

driver.find_element(By.XPATH, value='//div[contains(@class, "file_menu_list")]').click()

# open downloaded folder
time.sleep(4)
pyautogui.click(317,982)

time.sleep(1)
pyautogui.click(425,869)

# copy zip file to selected folder
time.sleep(2)
keyboard.send('ctrl+c')

# find folder name
time.sleep(2)
keyboard.send('ctrl+f')

time.sleep(1)
pyautogui.typewrite('safira_test_ems', interval=0.2)

time.sleep(2)
keyboard.send('down')

time.sleep(1)
keyboard.send('enter')

# paste zip file
time.sleep(2)
keyboard.send('ctrl+v')

# open WinRAR
app = Application(backend="uia").start("C:\\Program Files\\WinRAR\\WinRAR.exe")
time.sleep(3)
keyboard.send('alt+f4')
cwin = app.window(title="Downloads (evaluation copy)")

if cwin.is_maximized() == False:
    cwin.maximize()

# dialog = Desktop(backend="uia").window(title="Downloads (evaluation copy)")
# dialog.child_window(auto_id="16", control_type="ComboBox").click()
# print(dialog.print_control_identifiers())

time.sleep(5)

# find the folder
pyautogui.click(441,175)
keyboard.send('right')

pyautogui.typewrite('\safira_test_emsisoft', interval=0.1)

# open the folder
time.sleep(2)
keyboard.send('enter')

time.sleep(1)
pyautogui.click(182,270)

# unzip zip file
keyboard.send('alt+w')

time.sleep(1)
pyautogui.typewrite('emsisoft', interval=0.1)

dialog = Desktop(backend="uia").window(title="safira_test_emsisoft (evaluation copy)")
# time.sleep(1)
dialog.child_window(title="OK", auto_id="1", control_type="Button").wrapper_object().click_input()
