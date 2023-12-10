import cv2
import numpy as np
import pyautogui
import time
# lopping over the template matching

# reading the templates
template3 = cv2.imread('t1.png', 0)
template4 = cv2.imread('t2.png', 0)
template5 = cv2.imread('t3.png', 0)
template6 = cv2.imread('t4.png', 0)

# setting the threshold for confidence in template matching
threshold = 0.7

# alert box for stopping criteria
pyautogui.alert(text = 'Keep the mouse pointer on the top left corner of screen to stop the program', title= 'Stopping Criteria')

# continuous loop to check for youtube ad
while True:
    time.sleep(1)
    im1 = pyautogui.screenshot()
    im1 = np.asarray(im1.convert(mode = 'L'))
#     im1.save('im1.png')
#     im1 = cv2.imread('im1.png', 0)
        
# checking for template 1   
    res = cv2.matchTemplate(im1, t1, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    
# checking if template is matched
    if loc[0].size != 0:
# clicking on the first match
        pyautogui.click(list(zip(*loc[::-1]))[0])
        continue # continue loop from start without further execution of the loop
        
# checking for template 2       
    res = cv2.matchTemplate(im1, t2, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    
# checking if template is matched
    if loc[0].size != 0:
# clicking on the first match
        pyautogui.click(list(zip(*loc[::-1]))[0])
        continue # continue loop from start without further execution of the loop
        
# checking for template 3        
    res = cv2.matchTemplate(im1, t3, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    
# checking if template is matched
    if loc[0].size != 0:
# clicking on the first match
        pyautogui.click(list(zip(*loc[::-1]))[0])
        continue # continue loop from start without further execution of the loop    
    
# checking for template 4        
    res = cv2.matchTemplate(im1, t4, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    
# checking if template is matched
    if loc[0].size != 0:
# clicking on the first match
        pyautogui.click(list(zip(*loc[::-1]))[0])
    
#     Stopping criteria
    if pyautogui.position() == (0,0):
    	pyautogui.alert(text = 'Adskipper is Closed', title = 'Adskipper Closed')
    	break
