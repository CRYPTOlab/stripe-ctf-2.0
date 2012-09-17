#!/usr/bin/env python 

""" 
A simple echo server 
""" 

import socket 

host = 'localhost'
backlog = 5 
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 


def get_open_port():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind(("",0))
  s.listen(1)
  port = s.getsockname()[1]
  s.close()
  return port

port = get_open_port()
s.bind((host,port)) 
s.listen(backlog) 
print "Listening on port " + str(port)
last_port = 0
path = ""
all_filename = "all.txt"
last_filename = "last.txt"
while 1: 
    client, address = s.accept() 
    data = client.recv(size)
    remote_host, remote_port = address
    print remote_port
    diff = remote_port - last_port
    print diff
    with open(path + all_filename, "a") as myfile:
        myfile.seek(0)
        myfile.write('{"prev": ' + str(last_port) + ', "current": ' + str(remote_port) + '}\n' )
        myfile.truncate()
        myfile.close()
    with open(path + last_filename, "w") as last_file:
        last_file.seek(0)
        last_file.write(str(diff))
        last_file.truncate()
        last_file.close()
    last_port = remote_port
