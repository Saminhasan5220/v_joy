
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
        except ConnectionRefusedError:
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

                if not data:
                    print("not data")
                    return
            except ConnectionResetError or ConnectionAbortedError or KeyboardInterrupt:
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
try:
    while True:
        J = c.recieve()
        print(J)
        if J is None:
            print("quitting")
except KeyboardInterrupt:

    pass
