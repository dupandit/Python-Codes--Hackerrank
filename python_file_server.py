#!/usr/bin/python
#server.py
import socket
import time
import os
from os import rename, listdir

#create a socket object
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#get local machine name
host=socket.gethostname()

port=9999

#bind to the port
serversocket.bind((host,port))

#queue upto 5 requests
serversocket.listen(5)

#
while True  :
	#establish a connection
	clientsocket,addr=serversocket.accept()
	print("Got a connection from %s"%str(addr))
	num_request=clientsocket.recv(1024)

#GET FUNCTION : ACCEPT request with filename and send data in bytes
	if num_request[0]=='1' :
		request=num_request.split()	
		l=len(request)
		#print num_request,request
		fname=request[1]
		f=open(fname,"r")
		contents=f.read()
		clientsocket.send(contents)
		f.close()
		clientsocket.close()

	elif num_request[0]=='2' : 
		request=num_request.split(';')
		l=len(request)
		#print num_request,request
		fname=request[1]
		f=open(fname,"w+")
		contents=request[2]
		f.write(contents)
		f.close()
		clientsocket.close()

	else :
		request=num_request.split(';')
		l=len(request)
		fnames=listdir('.')
		for fname in fnames :
			if fname==request[1] :
				rename(fname, fname.replace(request[1],request[2]))
		mseg='Renamed'
		clientsocket.send(mseg)
		clientsocket.close()
		










		
