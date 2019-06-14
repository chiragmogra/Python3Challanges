#!usr/bin/python2
import socket
recv_ip="127.0.0.1"
recv_port=4444 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((recv_ip,recv_port))
while True:

	data=s.recvfrom(150)
	if data[0]=="###":
		break
	else:
		print("message from sender is",data[0])
		msg=raw_input("Enter reply of message ")
		if len(msg)>150:
			print("Please enter message less than 150 character ")	
		else:
			s.sendto(msg,data[1])


