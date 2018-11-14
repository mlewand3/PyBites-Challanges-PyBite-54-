#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Program for storaging clipboard history
'''

import pyperclip
import datetime
from keyboard import add_hotkey as shortcut_pressed
from tkinter import *
from tkinter.ttk import Frame, Button
from subprocess import Popen as use
from pathlib import Path

#C:\Users\User\Document\ 

def directory():
    '''For getting current directory
    '''
    pass

def file_name():
	'''For getting datestamp to filename
	'''
	now = datetime.datetime.now()
	return str(now.year) + "_" + str(now.month) + "_" + str(now.day) + '.txt'

def clipboard_to_file():
    '''Addind clipboard content to file
    '''
    with open(file_name(), "a") as myfile:
        myfile.write("\n")
        myfile.write(pyperclip.paste())

def show_history():
    '''For showing history
    '''
    use('explorer C:\Folder')

class Program(Frame):
    '''Main window content
    '''
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
      
        self.master.title("Clipboard Listener")                #window title            
        self.pack(fill=BOTH, expand=True)                      #window place and stuff

        showHistoryButton = Button(self,                       #setting button
        	                    text="Show Clipboard History", #text on button
        	                    command = show_history)        #function which is activated

        showHistoryButton.place(relx=0.5,                      #setting button on 0,5 of x-axis 
        	                    rely=0.5,                      #setting button on 0,5 of y-axis
        	                    anchor=CENTER)                 #gluing it to center

        status = Label(self.master,                            #setting status bar
        	            text="I`m listening...",               #status bar text
        	            bd=1,                                  #status bar border value
        	            relief=SUNKEN,                         #setting its visuals
        	            anchor=E)                              #gluing text to right side of bar

        status.pack(side=BOTTOM, fill=X)                       #placing status bar
        
def main():
    '''Main functions handling everything
    '''
    
    twindow = Tk()                                             #initialising Tkinter
    twindow.geometry("250x100")                                #setting window size
    app = Program()                                            #initialising window content
    shortcut_pressed('ctrl+c', clipboard_to_file)              #waiting for ctrl+c to be pressed 
    twindow.mainloop()                                         #window loop 

if __name__ == '__main__':                                     #let`s start this shit
    main() 

