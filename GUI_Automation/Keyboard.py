import pyautogui

pyautogui.click(100,100) #click to start writing
pyautogui.typewrite('My name is Manith', interval=0.2)#interval between each character typed
pyautogui.click(100,100) 
pyautogui.typewrite(['a','b','left','left'], interval=0.2)#type the character after moving to left twice
print(pyautogui.KEYBOARD_KEYS) #all the keyboard keys that can be used
pyautogui.press('F3')
pyautogui.hotkey('ctrl','F3') #Keys pressed together
