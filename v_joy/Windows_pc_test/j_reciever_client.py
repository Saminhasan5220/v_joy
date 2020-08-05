from client import *
c = Client()
try:
    while True:
        J = c.recieve()
        print(J)
        if J is None:
            print("quitting")
            break
except KeyboardInterrupt:

    pass