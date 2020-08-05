import sys
import time
import json
import socket

class Server:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    def __init__(self,ip='127.0.0.1',port=10000):
        self.ip = ip
        self.port = port

        self.sock.bind((self.ip,self.port))
        self.sock.listen(1)
        self.running = True
        self.client = None
        self.client_address = None

        self.client,self.client_address = self.sock.accept()

    def send(self,data):
        if self.client:
            try:
                data_string = json.dumps(data)
            
                self.client.send(data_string.encode('utf-8'))
                time.sleep(0.001)
                #print("From Server to Client->",data_string)
            except OSError:
                return
        else:
            return
        

        
    def quit(self):
        self.running = False
        if self.client:
            self.client.close()
        sys.exit()

        
#server = Server()
#try:
#    server.send(0)
#except KeyboardInterrupt:
#    pass