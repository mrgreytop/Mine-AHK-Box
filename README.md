# Mine-AHK-Box
Extended python API for AutoHotKey to map xbox controller input to keyboard and mouse buttons.

In this project I have extended the API written by Spencer Young (see here: https://pypi.org/project/ahk/#deps ).The project aims to provide a high-level python API to map joystick buttons, and analogue sticks to a keyboard or mouse. 

## Acknowledgements
All the additions I have made to Spencer's API are contained within ahk/joystick.py or ahk/templates/joystick/\*.

I have also used the AHK script, 'XInput.ahk' provided by "Lexikos" (see here: https://autohotkey.com/board/topic/35848-xinput-xbox-360-controller-api/page-1) to get the individual states of the triggers on the xbox controller.

Hence I do NOT claim any credit for the code OUTSIDE of ahk/joystick.py or ahk/templates/joystick/\*, nor the XInput.ahk script which is located inside the ahk/templates/joystick/ folder.

## Compatability
In theory alot of what I have written could be used with any controller. However, currently I have only tested using a wired xbox controller, so i cannot guarentee it will work with any other controllers. 

For the "triggers_2_mouseclick" function I have used an AHK script written by "Lexikos" (see here: https://autohotkey.com/board/topic/35848-xinput-xbox-360-controller-api/page-1). This script provides key functions from XInput (the Microsoft Common Controller API). Therefore, a controller that makes use of XInput should be able to use this script.

All testing was either done within the windows desktop or on Minecraft 1.15.1. Therefore I cannot guarentee compatability with other games, programs, or OSs. However, in theory all scripts should work with any game. 
