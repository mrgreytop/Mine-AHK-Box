#NoEnv
#Persistent
#Include, C:\Users\tompr\OneDrive\coding\Mine-AHK-Box\ahk\templates\joystick\XInput.ahk
XInput_Init()

SetTimer, WatchTriggers, {{timer}}
return

GetKeysState(triggers){
    KeysState := {}
    for key, value in triggers
        if value > {{threshold}}
            KeysState[key] := "Down"
        else if value < {{threshold}}
            KeysState[key] := "Up"
    return KeysState
}

WatchTriggers:
    PrevKeysState := KeysState
    State := XInput_GetState({{joystick}}-1)

    LT := State.bLeftTrigger
    RT := State.bRightTrigger

    triggers := { {{mapping["LT"]}}:LT, {{mapping["RT"]}}:RT}

    KeysState := GetKeysState(triggers)

    for key, state in KeysState
        if (PrevKeysState[key] = state){
        }else if (state = "Down"){        
            MouseClick, %key%, , , 1, 0, D
        }else if (state = "Up"){
            MouseClick, %key%, , , 1, 0, U
        }

    return

ExitApp