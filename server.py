#! /bin/usr/python3

import socket

recv_ip='172.31.32.68'
recv_p=9572

#creating socket for udp connection
#socketfunction(ipv4,udp)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while(4>3):

#to take input
	msg=input("Enter your message : ")
	emsg=msg.encode('ascii')

#sending data to sender
	s.sendto(emsg,(recv_ip,recv_p))
#receiving data from receiver
	print(s.recvfrom(10))

s.close()
