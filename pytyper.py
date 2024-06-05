import os
from time import sleep
import write
import reader
print("Welcome To Pytyper by Jack")
r_or_w = input("enter W to write or any other key to read\n")
if r_or_w == 'w':
    write.typing()


##To-Do
##Saving in other folders
##line break support
##add reading mode
##make reading mode less "hacky"
##make own file ext that pytyper can open
