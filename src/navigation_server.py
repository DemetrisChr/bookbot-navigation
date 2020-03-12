#!/usr/bin/env python
import socket
import json
from navigator import Navigator
from position import Position

class NavigationServer():
    def __init__(self):
        self.nav = Navigator()
        self.start_server()


    def start_server(self):
        s = socket.socket()
        port = 12345
        s.bind(('',port))
        s.listen(1)
        self.client, addr = s.accept()
        print ("Socket Up and running with a connection from",addr)
        while True:
            rcData = self.client.recv(1024).decode()
            json_data = self.decode_json(rcData)
            position = Position(**json_data["position"])
            self.nav.go_to(position, self.send_arrived_msg)

    def send_arrived_msg(self):
        self.client.send("Arrived".encoded())


    def decode_json(self, data):
        json_data = json.loads(data)
        return json_data

if __name__ == '__main__':
    print("Listening")
    nav_server = NavigationServer()
