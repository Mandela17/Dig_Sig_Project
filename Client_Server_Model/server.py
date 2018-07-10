import socket
from random import getrandbits
from math import sqrt
from sys import exit
import math
import random
import hashlib
from Cryptodome.Math.Numbers import Integer
from Cryptodome.Math import Primality
import _thread


q = 11
p = 23
g = 4
x = 7
y = 8

msg=b'mandela'


def on_new_client(clientsocket,addr):
	while True:
		# msg = clientsocket.recv(1024) 

		data = clientsocket.recv(1024).decode()
		rr,ss=data.split(" ")
		msss=verification(int(rr),int(ss))
		# print(msss)

		if not data:
			break
		# print("From connected user: " + a)
		# print(a)
		# print(b)
		clientsocket.send(msss.encode())
		#do some checks and if msg == someWeirdSignal: break:
		# print addr, ' >> ', msg
		# msg = raw_input('SERVER >> ') 
		#Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
		# clientsocket.send(msg) 
	clientsocket.close()

def verification(r,s):
	global p,q,g,msg,y
	if 0 < r and r < q and 0 < s and s < q:
		w = inverse(s, q)
		m=hashlib.sha1()
		m.update(msg)
		z = int("0x" + m.hexdigest(), 0)
		u1 = (z*w) % q
		u2 = (r*w) % q
		v = ((powmod(g,u1,p) * powmod(y,u2,p)) % p) % q
		if v == r:
			return "verification Successful"
		else: 
			return "verification Error"


def inverse(a, m) :
	m0 = m
	y = 0
	x = 1
	if (m == 1) :
		return 0
	while (a > 1) :
		q = a // m
		t = m
		m = a % m
		a = t
		t = y
		y = x - q * y
		x = t
	if (x < 0) :
		x = x + m0
	return x

def powmod(x,c,n):
	c = '{0:b}'.format(c)
	z = 1
	l = len(c)
	for i in range(0, l):
		z = (z**2)%n
		if (c[i] == "1"):
			z = (z*x) % n
	return z;


def Main():
	host = '127.0.0.1'
	port = 5000
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host,port))

	s.listen(5)
	# print("Connection from: " + str(addr))
	while True:
		c, addr = s.accept()
		print("Connection from: " + str(addr))
		_thread.start_new_thread(on_new_client,(c,addr))
		# c=input()
		# if c=='q':
		# 	break
	c.close()
if __name__== '__main__':
	Main()