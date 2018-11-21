#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Program for storaging clipboard history
'''

import pyperclip
import datetime
from keyboard import add_hotkey as shortcut_pressed
from tkinter import Tk, BOTH, CENTER, Label, SUNKEN, E, BOTTOM, X
from tkinter.ttk import Frame, Button
from os import chdir, makedirs, startfile

script_directory = 'C:/Clipboard_history'

def change_directory():
    '''Change directory for script work directory
    '''
    chdir(script_directory)

def create_folder():
    '''Creating directory for clipboard history
    '''    
    makedirs(script_directory, exist_ok=True)

def file_name():
    '''For getting datestamp to filename
    '''
    now = datetime.datetime.now()                              
    return str(now.year) + "_" + str(now.month) + "_" + str(now.day) + '.txt'

def create_timestamp():
    '''For getting timestamp
    '''
    now = datetime.datetime.now()
    return str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)

def clipboard_to_file():
    '''Addind clipboard content to file
    '''
    with open(file_name(), "a") as myfile:                     #opening file in addition style
        myfile.write("\n")                                     #new line for clarity
        myfile.write(create_timestamp())                       #timestamp of getting content from clipboard
        myfile.write("\n")                                     #new line for clarity
        myfile.write(pyperclip.paste())                        #passing clipboard content to file
        myfile.write("\n")                                     #new line for clarity

def show_history():
    '''For showing history
    '''
    startfile('C:/Clipboard_history')                          #opening folder with history

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
    
    create_folder()                                            #creating folder for data
    change_directory()                                         #changing working directory 

    twindow = Tk()                                             #initialising Tkinter
    twindow.geometry("250x100")                                #setting window size
    app = Program()                                            #initialising window content
    shortcut_pressed('ctrl+c', clipboard_to_file)              #waiting for ctrl+c to be pressed 
    twindow.mainloop()                                         #window loop 

if __name__ == '__main__':                                     #let`s start this shit
    main()