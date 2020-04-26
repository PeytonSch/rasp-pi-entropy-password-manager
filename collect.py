#This file will handle the reading of our sensor data from our rpi

import time
import numpy as np
import RPi.GPIO as GPIO
import adcUtil  as adc

class collector:


    def __init__(self):
        print("collector intialized")

    def collectData(self):

        ledPin = 25
        buttonPin = 26
        gatePin = 27

        to = time.time()
        t = to
        i = 0
        gateStateArray = np.array([])
        buttonStateArray = np.array([])
        while t < to+10:
            #####################
            #Microphone
            #####################
            gateState = GPIO.input(gatePin)

            #####################
            #Push Button
            #####################
            # get the state of the pin
            buttonState = GPIO.input(buttonPin)

            gateStateArray = np.append(gateStateArray,gateState)
            buttonStateArray = np.append(buttonStateArray,buttonState)

            #####################
            #LED
            #####################
            GPIO.output(ledPin, True)   # turn on
            time.sleep(.5)             # wait
            GPIO.output(ledPin, False)  # turn off
            time.sleep(0.5)             # wait, then repeat

            t = time.time()


        writeNewData(buttonStateArray,gateStateArray)

        return
