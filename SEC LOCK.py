#whenever a person tries to acess the computer physically by using mouse/keyboard the system will lock automatically.
#Kindly install [pynput] before running program.
from pynput import keyboard
from pynput.mouse import Listener
import threading 
import subprocess
import time
#print("press 'p' to release the automatic lock for yourself")
def lock(): #function for locking system 
        cmd='rundll32.exe user32.dll, LockWorkStation'
        subprocess.call(cmd)
def PR(d):
    print(str(d))
    if str(d)=="'r'": ######press this key to release the automatic lock for yourself,You can set yours [PATICULAR] key also
        exit()
    lock()








def mousemove(x12,y12):
    #print(x12,"    ",y12)
    lock()

    
    
    

    

def mouseclick(x,y,b,p):
    """
    """
    #print(b,x,y,p)
    lock()



def mousescroll(x1,y1,x2,y2):
    print(x1,y1,x2,y2)
    lock()





def M(): #mouse activity listener
    with Listener(on_click=mouseclick,on_scroll=mousescroll,on_move=mousemove)as gistener:
        gistener.join()
def K():#keyboard activity listener
    with keyboard.Listener(on_press=PR) as listener:
        listener.join()


mousethr = threading.Thread(target=M)
keyboardthr = threading.Thread(target=K) 
  
#to run two activities simultaneously     
mousethr.start() 
keyboardthr.start() 



