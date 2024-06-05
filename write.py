import os
from time import sleep
def typing():
    doc_name = input("Name Output File (txt format)")
    file = open(doc_name + ".txt", 'w')
    text = input ("start typing below (output will be on single line)\n")
    file.write(text)
    print("saving file and printing output in 5 seconds")
    sleep(5)
    os.system('clear')
    print(text)
