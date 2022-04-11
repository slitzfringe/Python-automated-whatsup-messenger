# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 22:30:56 2022

@author: revan
"""
from subprocess import Popen
import datetime
import time
import pywhatkit as pwt
import pyautogui as pg
import sys


t = '\n\n\nPrerequisties :-\n  Caution\n\n    "If any chrome is open it will close so be cautious about it"\n    "Repated opening and closing of whatsapp and chrome will be happening nothing to worry "\n    "The list is to be setted up before the execution of the program"\n    "If all are satisfied then your good to go"'

print(t)

list = [""] #list can have multiple contact numbers with country code enclosed in quotes

print("\nList of the contacts:-\n")

for _ in list:
    print(_)

i = input("Press 1 and Enter to exit\n            or\nPress Enter to proceed : ")    
    
if i == '1':
    print("\n\n    Exiting")
    sys.exit()




"""


prerequisties :-

  Caution 
  
    "If any chrome is open it will close so be cautious about it"
    "Repated opening and closing of whatsapp and chrome will be happening nothing to worry "
    "The list is to be setted up before the execution of the program"
    "If all arer satisfied then your good to go"
"""


def close_chrome():
    Popen('taskkill /F /IM chrome.exe', shell=True)
    
    
def open_chrome_web(url):
    Popen(['start', 'chrome' , url], shell=True)
    
    
close_chrome()
time.sleep(2)



#count = 0

for _ in list:
    url = "https://wa.me/"
    url = "https://wa.me/" + _
    
    open_chrome_web(url)
    
    time.sleep(4)
    
    pg.write('Hi its python automated!!')
    pg.press('Enter')
    
    print("Msg send to " + _ )
    #print("Count = ",count)
    #count += 1
    
    time.sleep(1)
    
    close_chrome()