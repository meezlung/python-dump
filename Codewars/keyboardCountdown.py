# type: ignore

from re import X
import keyboard
import time

#for x in range(0, 10):
 #   keyboard.write('.')
#    keyboard.press_and_release('enter')

def pyramid(base, top, step=4):
    dot = '.'        
    time.sleep(1)
    for i in range(top, base+1, step):
        keyboard.write((dot*i).center(base, ' '))
        #keyboard.press_and_release('enter')
        time.sleep(0.1)
    for i in range(base+1, -1, -step):
        keyboard.write((dot*i).center(base, ' '))
        #keyboard.press_and_release('enter')       
        time.sleep(0.1) 
                        

def countdown(x):
    for x in range(x, 0, -1):
        keyboard.write(str(x))
        keyboard.press_and_release('enter')
        time.sleep(0.3)

#countdown(120)
pyramid(100, 1)                                                                                           