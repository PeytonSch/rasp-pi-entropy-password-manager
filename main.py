#The main file will drive our program, it will handle
#calling the setup for the rasp pi, running the menu,
#cleaning up, and exiting

from setup import *
from menu import *


#setup rpi
setup()

#instantiate classes
generate = generator()
manager = manager()
collector = collector()

#call menu
run_main_menu()

#cleanup
cleanup()
