#This file will setup the rpi and initialize
#everything, it will also contain cleanup functions for the rpi

# import the GPIO library
import RPi.GPIO as GPIO
import adcUtil  as adc

#####################
#LED STUFF
#####################

# set GPIO numbering
GPIO.setmode(GPIO.BCM)
# assign a variable for the pin numer
ledPin = 27
# set the GPIO pin to output mode
GPIO.setup(ledPin, GPIO.OUT)

'''
Turn on and off:
GPIO.output(ledPin, True)   # turn on
time.sleep(0.2)             # wait
GPIO.output(ledPin, False)  # turn off
time.sleep(0.5)             # wait, then repeat
'''

#####################
#Push Button
#####################
# use GPIO numbering
GPIO.setmode(GPIO.BCM)
# assign a variable for the pin numer
buttonPin = 27
# configure the GPIO pin to accept inputs, and activate the pull-up resistor
# PUD_UP for internal pull-up resistor - returns 1 when the button is released
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


'''
Button stuff:
# get the state of the pin
print(GPIO.input(buttonPin))
'''


#####################
#Microphone
#####################
GPIO.setmode(GPIO.BCM)
gatePin = 20
GPIO.setup(gatePin, GPIO.IN)

'''
gateState = GPIO.input(gatePin)
Vaudio    = adc.readADC(channel=0)
Venvelope = adc.readADC(channel=1)
'''


#####################
#Cleanup
#####################
def cleanup():
    # clean-up GPIO
    GPIO.cleanup()
    return
