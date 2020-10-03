import pyautogui
print(pyautogui.size()) #size of screen
print(pyautogui.position()) #position of cursor
pyautogui.moveTo(10,10,duration=1.5) #moves cursor in 1.5s to position 10,10
pyautogui.moveRel(20,-100) #relative movement by pixels
pyautogui.click(300,100)
pyautogui.doubleclick(300,100)


#a failsafe to stop GUI scripts are to bring the cursor to 0,0 cordinates(top left) which stops program from running
