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

print "Searching inside : "+sys.argv[1]

newdirectory = sys.argv[1]+"txt"
if not os.path.exists(newdirectory):
    os.makedirs(newdirectory) #Creates a newdirectory
combined = open(os.path.join(newdirectory,"allcombined.txt"),'w') #Creates a file of all the subs combined for dataset

for file in os.listdir(sys.argv[1]): #Gets All the files inside DIR (Argument1)

    newfile = open(os.path.join(newdirectory,file.replace(".vtt", ".txt")),'w') #Creates a newfile
    if file.endswith(".vtt"):
        print "Formating : "+file #Shows current File
        with open(os.path.join(sys.argv[1], file)) as f:

            for line in f: #a line for each file
                 if not line.startswith('0') : #Couldnt Get the "or" working
                     if not line.startswith('WEBVTT') :#Cleaning
                         if not line.startswith('Kind:') :#Cleaning
                             if not line.startswith('Language:') :#Cleaning
                                 if not line.startswith('\n') :#Cleaning
                                    if not line.startswith('[BLANK_AUDIO]') :#Cleaning
                                        newfile.write("%s" % line) #Add new line to new file
                                        combined.write("%s" % line) #Add new line to combinedfile
            print "DONE!" #NEXT ONE!
