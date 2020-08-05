import json
import time
from inputs import get_gamepad
from server import *
s = Server() 
'''
/joy.buttons
0 A BTN_SOUTH 
1 B BTN_EAST
2 X BTN_WEST
3 Y BTN_NORTH
4 LB BTN_TL
5 RB BTN_TR
6 BTN_BACK NULL
7 start BTN_START 
8 power NULL
9 Button stick left BTN_THUMBL
10 Button stick right BTN_THUMBR
/joy.axes
0 Left/Right Axis stick left ABS_X
1 Up/Down Axis stick left ABS_Y
2 LT ABS_Z
3 Left/Right Axis stick right ABS_RX
4 Up/Down Axis stick right ABS_RY
5 RT ABS_RZ
6 cross key left/right ABS_HAT0X
7  cross key up/down ABS_HAT0Y

'''
'''

j.axes.append(J["ABS_X"])
j.axes.append((J["ABS_Y"])
j.axes.append(J["ABS_Z"])
j.axes.append(J["ABS_RX"])
j.axes.append(J["ABS_RY"])
j.axes.append(J["ABS_RZ"])
j.axes.append(J["ABS_HAT0X"])
j.axes.append(J["ABS_HAT0Y"])
j.buttons.append(J["BTN_SOUTH"]) 
j.buttons.append(J["BTN_EAST"])
j.buttons.append(J["BTN_WEST"])
j.buttons.append(J["BTN_NORTH"])
j.buttons.append(J["BTN_TL"])
j.buttons.append(J["BTN_TR"])
j.buttons.append(0)
j.buttons.append(J["start BTN_START"])
j.buttons.append(0)
j.buttons.append(J["BTN_THUMBL"])
j.buttons.append(J["BTN_THUMBR"])
'''

joystick_values = {"timestamp" : 0,"BTN_NORTH" : 0,"BTN_SOUTH" : 0,"BTN_EAST" : 0,"BTN_WEST" : 0,"BTN_TR" : 0,"BTN_TL" : 0,"BTN_THUMBR" : 0,"BTN_THUMBL" : 0,"BTN_SELECT" : 0,"BTN_START" : 0,"ABS_RY" : 0,"ABS_RX" : 0,"ABS_RZ" : 0,"ABS_HAT0X" : 0,"ABS_HAT0Y" : 0,"ABS_X" : 0,"ABS_Y" : 0, "ABS_Z" : 0}
def main():
    """Just print out some event infomation when the gamepad is used."""

    while 1:
        try:
            events = get_gamepad()
            for event in events:
                if event.ev_type != "Sync":
                    joystick_values[event.code] = event.state
                    #print(event.code, event.state)
            joystick_values["timestamp"] = time.time()
            #print(joystick_values)
            s.send(joystick_values)
            #s.send(time.time())
            #time.sleep(1)
        except KeyboardInterrupt:
            s.quit()
        #print(joystick_values)



if __name__ == "__main__":
    main()
    
    
    
"""Simple example showing how to get gamepad events.
BTN_SOUTH 0
BTN_EAST 0
BTN_WEST 0
BTN_NORTH 0
BTN_TR 0
BTN_TL 0
BTN_THUMBR 0
BTN_THUMBL 0
BTN_SELECT 0
BTN_START 0
ABS_RY 0
ABS_RX 0
ABS_RZ 0
ABS_HAT0X 0
ABS_HAT0Y 0
"""

"""
import json

data_string = json.dumps(data) #data serialized
data_loaded = json.loads(data) #data loaded
"""