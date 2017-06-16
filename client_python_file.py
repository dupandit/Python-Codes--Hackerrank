#!/usr/bin/python
#client.py

import socket
import os

commnd=(raw_input('Press 1 for GET\nPress 2 for PUT\nPress 3 for RENAME\n'))

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()

port=9999


if commnd=='1' :
	fname=raw_input('Sir! Which file do you need from server-database?\n')	
	s.connect((host,port))
	s.send(commnd+' '+fname)
	tm=s.recv(1024)
	f=open(fname,"w+")
	f.write(tm)
	f.close()
	s.close
	print("File received! Please check it!!!!")

elif commnd=='2' :
	fname=raw_input('Sir! Which file do you need to put in server-database?\n')
	s.connect((host,port))
	f=open(fname,"r")
	contents=f.read()
	s.send(commnd+';'+fname+';'+contents)
	f.close()
	s.close()
	print("File Sent, Thank You!!")

else :
	fnames=raw_input('Please write filename you want to rename and the new name of that file with a ; in between!\n')
	s.connect((host,port))
	s.send(commnd+';'+fnames)
	msg=s.recv(1024)
	print msg
	s.close()


