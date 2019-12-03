from ahk import AHK
from ahk.window import Window
import time
from threading import Thread

# ahk_path = "E:\Programs\AutoHotKey\AutoHotkey.exe"

ahk = AHK()
# try:
#     MineWin = ahk.find_window(title = b'Minecraft 1.14.4')
# except Exception as e:
#     print(e)
#     exit(1)

# MineWin.activate()


def quit_loop(quit_shortcut=["{Control}",  "{Alt}", "e"]):
    
    quit_flag = [False for i in range(len(quit_shortcut))]

    while not any(quit_flag):

        for i in range(len(quit_shortcut)):
            quit_flag[i] = ahk.key_state(quit_shortcut[i])
    
    print("Quiting...")
    SafeStop()

def SafeStop():
    pass
        
if __name__ == "__main__":
    quit_thr = Thread(target = quit_loop)
    quit_thr.start()
    


    quit_thr.join()

        



