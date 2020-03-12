#!/usr/bin/env python
import socket
import json
from navigator import Navigator

class NavigationServer():
    def __init__(self):
        print("blah")
        self.nav = Navigator()
        start_server()


    def start_server(self):
        socket = socket.socket()
        port = 12345
        socket.bind(('',port))
        socket.listen(1)
        self.client, addr = self.socket.accept()
        print ("Socket Up and running with a connection from",addr)
        while True:
            rcData = c.recv(1024).decode()
            json_data = decode_json(rcData)
            position = Position(**json_data["position"])
            self.nav.go_to(position, self.send_arrived_msg)

     def send_arrived_msg(self):
        self.client.send("Arrived".encoded())


    def decode_json(self, data):
        json_data = json.loads(data)
        return json_data

if __name__ == '__main__':
    nav_server = NavigationServer()

    print("Listening")
