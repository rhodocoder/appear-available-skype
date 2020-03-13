import pyautogui #install library first from File > Settings > Project Interpreter > Package > + > pyautogui
width, height = pyautogui.size() #saves the screen resolution
print(width, height) #print screen resolution
for i in range(1000000): #execute movements and clicks below 1000000 times
      pyautogui.moveTo(1000, 500, duration=0.25)
      pyautogui.click(1000, 500, button='left')
      pyautogui.moveTo(700, 300, duration=0.25)
      pyautogui.click(700, 300, button='left')
      pyautogui.moveTo(1000, 500, duration=0.25)
      pyautogui.click(1000, 500, button='left')
      pyautogui.moveTo(700, 300, duration=0.25)
      pyautogui.click(700, 300, button='left')
