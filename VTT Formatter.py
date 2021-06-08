#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'AxelAli'
import os
import sys


#MADE BY AXEL ALI
#https://github.com/AxelAli



#USAGE:
# $ VTT Formatter.py [DIR]
# $ VTT Formatter.py ./subs

print(f"Searching inside : {sys.argv[1]}")

newdirectory = sys.argv[1]+"txt"
if not os.path.exists(newdirectory):
    os.makedirs(newdirectory) #Creates a newdirectory
combined = open(os.path.join(newdirectory,"allcombined.txt"),'w') #Creates a file of all the subs combined for dataset

for file in os.listdir(sys.argv[1]): #Gets All the files inside DIR (Argument1)

    newfile = open(os.path.join(newdirectory,file.replace(".vtt", ".txt")),'w') #Creates a newfile
    if file.endswith(".vtt"):
        print("Formating : "+file) #Shows current File
        with open(os.path.join(sys.argv[1], file)) as f:

            previous = '0'
            for line in f: #a line for each file
                 if line.find('-->') == -1 : #Avoid timestanps
                     if not line.startswith('WEBVTT') :#Cleaning
                         if not line.startswith('Kind:') :#Cleaning
                             if not line.startswith('Language:') :#Cleaning
                                 if not line.startswith('\n') :#Cleaning
                                    if not line.startswith('[BLANK_AUDIO]') :#Cleaning
                                        if not line.startswith(previous) :#Avoiding repetitions 
                                            newfile.write("%s" % line) #Add new line to new file
                                            combined.write("%s" % line) #Add new line to combinedfile
                                            previous = line
            print("DONE!") #NEXT ONE!
