#This file will handle the reading of our sensor data from our rpi




#
#Im not sure if I actually want this file or not
#


class collector:

    def collectData():

        to = time.time()
        t = to
        i = 0
        gateStateArray = np.array([])
        buttonStateArray = np.array([])
        while t < to+30:
            #####################
            #Microphone
            #####################
            gateState = GPIO.input(gatePin)

            #####################
            #Push Button
            #####################
            # get the state of the pin
            buttonState = GPIO.input(buttonPin)

            gateStateArray.append(gateState)
            buttonStateArray.append(buttonState)

            #####################
            #LED
            #####################
            GPIO.output(ledPin, True)   # turn on
            time.sleep(.5)             # wait
            GPIO.output(ledPin, False)  # turn off
            time.sleep(0.5)             # wait, then repeat


        writeNewData(buttonStateArray,gateStateArray)

        return
