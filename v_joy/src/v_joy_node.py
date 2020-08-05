#! /usr/bin/env python
import sys
import time
import json, ast
import socket
class Client:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    def __init__(self,ip='127.0.0.1',port=10000):
        self.ip = ip
        self.port = port
        self.running = True
        try:
            self.sock.connect((self.ip,self.port))
        except:
            print("Server not ready")
            return

        print("Client UP and recieving ...")


    def recieve(self):
        data_loaded = None

        if self.running:
            try:
                if self.running and self.sock:
                    data = self.sock.recv(1024)
                    data_loaded = ast.literal_eval(json.dumps(json.loads(data)))
                    return data_loaded
                    #print(data_loaded)

                if not data:
                    print("not data")
                    return
            except:
                print("Server Disconnected")
                self.running =False
                self.quit()
                return


    def quit(self):
        self.running = False
        if self.sock:
            self.sock.close()
        sys.exit()

c = Client()
import rospy
from sensor_msgs.msg import Joy
rospy.init_node("v_joy")
pub = rospy.Publisher('/joy', Joy, queue_size=10)

j = Joy()
counter = 0 
try:
    while not rospy.is_shutdown():
        J = c.recieve()
        if J is not None:
            j.axes = []
            j.buttons = []
            j.header.stamp = rospy.Time.now()
            j.header.seq = counter
            j.axes.append(J["ABS_X"])
            j.axes.append(J["ABS_Y"])
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
            j.buttons.append(J["BTN_START"])
            j.buttons.append(0)
            j.buttons.append(J["BTN_THUMBL"])
            j.buttons.append(J["BTN_THUMBR"])
            print(j)
            pub.publish(j)
            counter +=1
        if J is None:
            print("quitting")
            break
except KeyboardInterrupt:
    pass
