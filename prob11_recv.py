#!usr/bin/python2
import socket
recv_ip="127.0.0.1"
recv_port=4444 # 0-1024 -- you can check free udp port netstat -nulp
#create udp
#    ip type v4,v6
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# fitting ip and port with udp socket
s.bind((recv_ip,recv_port))
while True:
# receive data from sender
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


