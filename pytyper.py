#import libs
import os
from time import sleep


#program start
print(" Pytyper Copyright (C) 2024  Jack Catchpole \n This program comes with ABSOLUTELY NO WARRANTY; \n This is free software, and you are welcome to redistribute it")
sleep (1)
print("IMPORTANT: READING AND OR EDITING FILES NOT YET SUPORTED")
open_read = int(input("are we wanting to read a file (1 is yes 0 is no)"))
if open_read == 1:
    file_read_name = input("Enter file path: ")    
    print(open(file_read_name + ".pytype", 'r').read()) 
    
else:
    doc_name = input("Name Output File (txt format with .pytype extention)")
    line_num = int(input("enter aprox line numbers needed (cant add more later so good luck)"))
    file = open(doc_name + ".txt", 'w')
    while line_num > 0:
        lines_left = str(line_num)
        print(lines_left + "lines remaining")
        file = open(doc_name + ".pytype", 'a')
        text = input ("start typing below\n")
        file.write(text+"\n")
        line_num = line_num - 1

#To-Do
#Saving in other folders
#Editing Files using the
#Make App Use A GUI instead of command line refer to https://realpython.com/pysimplegui-python/

