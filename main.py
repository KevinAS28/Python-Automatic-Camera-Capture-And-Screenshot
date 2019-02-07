import subprocess
import time

delay = 3 #seconds
name = 0 #secuence name
while True:
    try:
        try:
            subprocess.check_output("gnome-screenshot --filename=%s.png" %(str(name)*2), shell=True)
        except:
            print("Error while gnome-screenshot. is gnome-screenshot installed?")
        try:
            subprocess.check_output("streamer -f jpeg -o %s.jpeg" %(str(name)), shell=True)
        except:
            print("Error while streamer. is streamer installed?")
        time.sleep(delay)
        name += 1
    except KeyboardInterrupt:
        break
