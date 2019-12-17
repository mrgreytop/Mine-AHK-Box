import logging
import logging.handlers
import time
import os
from ahk import AHK
from ahk.keys import KEYS

log = logging.getLogger()

handler = logging.FileHandler(filename="log.txt",mode="w+")
formatter = logging.Formatter(logging.BASIC_FORMAT)

handler.setFormatter(formatter)
log.addHandler(handler)
log.setLevel(logging.DEBUG)

ahk = AHK()

holdbind = {
    "Joy2":"q",
    "Joy1":KEYS.SPACE.name
}

simplebind = {
    "Joy3":"e",
    "Joy4":"f",
    "Joy7":"F3",
    "Joy8":KEYS.ESCAPE.name,
    "Joy5": "WheelUp",
    "Joy6": "WheelDown"
}

modifiers = {
    ("Joy9",""):KEYS.LControl.name,
    ("Joy10","T"):KEYS.LShift.name
}

procs = []

#left analogue stick for movement
#modifiers Ctrl and Shift used for sprint and sneak
procs.append(ahk.joyXY_keyboard(modifiers=modifiers))

#right for camera and mouse
procs.append(ahk.joy_2_mouse())

#button bindings
procs.append(ahk.joy_bind(mode="hold", bindings=holdbind))
procs.append(ahk.joy_bind(mode="simple", bindings=simplebind))

#maps triggers to left and right mouse buttons 
#uses Xinput from Xbox Controllers
procs.append(ahk.triggers_2_mouseclick())

#makes the D-pad move the mouse by dx or dy pixels 
#(used for interation with crafting benches/ inventory/ chest)
procs.append(ahk.joy_gridmouse(dx = 35, dy = 35))

#Can safely kill all ahk scripts by entering Ctrl+c
#In this case Ctrl+c is entered by pressing Joy9 (left analogue) + c
while True:
    try:
        time.sleep(5)
    except KeyboardInterrupt:
        for p in procs:
            p.kill()
        exit()
