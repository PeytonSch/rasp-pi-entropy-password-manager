#this file will handle the entropy generation of passwords.
from file_access import *
import random
import string
import numpy as np
#inputs are from push button status and from sound detector status

class generator:
    def __init__(self):
        print("generator intialized")
    def generateNewPassword():
        #read input lines from save files
        buttonLine = readButtonLines()
        audioLine = readAudioLines()

        total = np.sum(buttonLine)
        total = total + np.sum(audioLine)



        moddedTotal = int(total) % 40 + 10

        password = ""
        for i in range(moddedTotal):
            char = chr(np.random.random_integers(33,122))
            password = password + char



        print("Your password is:",password)

        return password
