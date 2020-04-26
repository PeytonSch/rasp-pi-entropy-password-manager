#This file will handle the reading of our sensor data from our rpi

import time
import numpy as np
import RPi.GPIO as GPIO
import adcUtil  as adc
import matplotlib.pyplot as plt

from file_access import *


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
        np_time_array = np.array([])
        np_value_array = np.array([])
        np_envelope_array = np.array([])
        while t < to+10:
            #####################
            #Microphone
            #####################
            gateState = GPIO.input(gatePin)
            Vaudio    = adc.readADC(channel=0)
            Venvelope = adc.readADC(channel=1)
            gateStateArray = np.append(gateStateArray,gateState)
            np_value_array = np.append(np_value_array,gateState)
            np_envelope_array = np.append(np_envelope_array,gateState)

            #####################
            #Push Button
            #####################
            # get the state of the pin
            buttonState = GPIO.input(buttonPin)


            buttonStateArray = np.append(buttonStateArray,buttonState)

            #####################
            #LED
            #####################
            GPIO.output(ledPin, True)   # turn on
            time.sleep(.5)             # wait
            GPIO.output(ledPin, False)  # turn off
            time.sleep(0.5)             # wait, then repeat

            t = time.time()

            np_time_array = np.append(np_time_array,t)


        plt.plot(np_time_array,np_value_array, label="Vaudio")
        plt.plot(np_time_array,np_envelope_array,label="Venvelope")
        plt.plot(np_time_array,np_gate_state_array,label="Gate State")
        plt.ylabel("Voltage Value")
        plt.xlabel("Time")
        plt.title("Mic Data")
        plt.legend()
        plt.show()

        plt.plot(np_time_array,buttonStateArray,label="ButtonState")

        writeNewData(buttonStateArray,gateStateArray)

        return
