# external library

import pyjokes
# print("Prining Jokes.. ")
joke = pyjokes.get_joke()
# print(joke)

""" 
so thanks
that was my program
"""

'''
this is a 
multi-line comment
'''

# another external library

import pyttsx3
engine = pyttsx3.init()
engine.say("This is a text-to-speech conversion library in Python")
# engine.runAndWait()

# built-in library

import os

# path to the directory 
path = '/users/mansi.gehlot/OneDrive - I2e Consulting/Desktop'

# get the list of entries in the directory
contents = os.listdir(path)

# print the content of directory
for i in contents:
    print(i)