from ahk import AHK
import logging
import time

log = logging.getLogger()
log.setLevel(logging.WARNING)
formatter = logging.Formatter("%(asctime)s,%(message)s", "%H:%M:%S")
handler = logging.FileHandler(filename = "log.csv", mode = "w")
handler.setFormatter(formatter)
log.addHandler(handler)

ahk = AHK(executable_path="C:\Program Files\AutoHotkey\AutoHotkey.exe")
win = ahk.win_get(title = "Minecraft 1.14.4")
win.activate()

while True: 
    try:
        if ahk.active_window == win:
            pos = str(ahk.mouse_position)
            pos = pos.replace("(","")
            pos = pos.replace(")","")
            log.warning(pos)
        else:
            print(f"exited {win}")
            raise KeyboardInterrupt()
    except KeyboardInterrupt:
        print("interrupted")
        exit(1)

