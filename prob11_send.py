#! usr/bin/python2
import socket
recv_ip="127.0.0.1"
recv_port=4444
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
i=1
while i==1:
	msg=raw_input("Enter your message ")
	if len(msg)>150:
		print("plaese Enter message less than 150 characters")
	else:
		s.sendto(msg,(recv_ip,recv_port))
# receive data from sender
		data=s.recvfrom(150)
		print("Received msg from receiver is",data[0])
	i=input("Enter 1 for continue \nEnter 2 for exit chat")
	if i==2:
		s.sendto("###",(recv_ip,recv_port))
		s.close()
		break
