from socket import *
import sys
import time
import json


def create_message(action, time_s, type_s):
    return {
        "action": action,
        "time": time_s,
        "type": type_s,
    }




if __name__ == "__main__":
    socket = socket(AF_INET, SOCK_STREAM)
    if (len(sys.argv) > 2):
        socket.connect((int(sys.argv[1]), int(sys.argv[2])))
    elif(len(sys.argv) > 1):
        socket.connect(("localhoost", int(sys.argv[2])))
    else:
        socket.connect(("localhost", 7777))
    socket.send(json.dumps(create_message("presence", time.ctime(time.time()), "status")).encode("utf-8"))
    data = socket.recv(1024 * 1024 * 5)
    print(data.decode("utf-8"))