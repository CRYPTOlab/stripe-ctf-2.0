#!/usr/bin/env python

"""
 simple echo server 
""" 

import socket 

host = '0.0.0.0'
backlog = 5 
size = 1024 


def get_open_port():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind(("",0))
  s.listen(1)
  port = s.getsockname()[1]
  s.close()
  return port

port = get_open_port()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
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
    diff = remote_port - last_port
    print "Remote: " + str(remote_port) + ", Prev: " + str(last_port) + ", Diff: " + str(diff) + ", Data: " + str(len(data))
    if len(data) != 113:
        print "DONE!!!!!!!!!!!!!!!!!!!"
        diff = 1
    with open(path + all_filename, "a") as myfile:
        myfile.seek(0)
        myfile.write('{"prev": ' + str(last_port) + ', "current": ' + str(remote_port) + 'i, "diff": ' + str(diff) + '}\n' )
        myfile.truncate()
        myfile.close()
    with open(path + last_filename, "w") as last_file:
        last_file.seek(0)
        last_file.write(str(diff))
        last_file.truncate()
        last_file.close()
    last_port = remote_port

