import time
import sys
import os
import logging

logging.basicConfig(level=logging.INFO)

libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
logging.info("Trying to import from " + str(libdir))
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_POE_HAT_B import POE_HAT_B
 

POE = POE_HAT_B.POE_HAT_B()
        
try:  
    while(1):
        POE.POE_HAT_Display(43)
        time.sleep(2)
        
except KeyboardInterrupt:    
    print("ctrl + c:")

