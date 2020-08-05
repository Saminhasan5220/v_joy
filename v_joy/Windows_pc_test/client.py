
import sys
import time
import json
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
                    data_loaded = json.loads(data)

                if not data:
                    print("not data")
                    return
            except ConnectionResetError or ConnectionAbortedError or KeyboardInterrupt:
                print("Server Disconnected")
                self.running =False
                self.quit()
                return
            finally:
                if data_loaded:
                    #print("From Server to Client =>",data_loaded,type(data_loaded))
                    return data_loaded
                else:
                    return

            
    def quit(self):
        self.running = False
        if self.sock:
            self.sock.close()
        sys.exit()
        
        
        
#client = Client()
#try:
#    client.recieve()
#except KeyboardInterrupt:
#    pass