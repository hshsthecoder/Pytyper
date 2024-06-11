#import libs
import os
from time import sleep

#program start
print("Welcome To Pytyper by Jack")
print("IMPORTANT: READING AND OR EDITING FILES NOT YET SUPORTED")
read = int(input("are we wanting to read a file (1 is yes 0 is no)"))
if read == 1:
    file_read_name = input("Enter file path")    
    file_read = open(file_read_name)
    print(file_read)
else:
    doc_name = input("Name Output File (txt format)")
    line_num = int(input("enter aprox line numbers needed (cant add more later so good luck)"))
    file = open(doc_name + ".txt", 'w')
    while line_num > 0:
        lines_left = str(line_num)
        print(lines_left + "lines remaining")
        file = open(doc_name + ".txt", 'a')
        text = input ("start typing below\n")
        file.write(text+"\n")
        line_num = line_num - 1


#To-Do
#Saving in other folders
#add reading mode
#make reading mode
#make own file ext that pytyper can open
