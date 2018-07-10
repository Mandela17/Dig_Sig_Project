import socket
from random import getrandbits
from math import sqrt
from sys import exit
import math
import random
import hashlib
from Cryptodome.Math.Numbers import Integer
from Cryptodome.Math import Primality


q = 11
p = 23
g = 4
x = 7
y = 8

msg=b'mandela'

# def signing(p,q,g,msg,x, y):
def signing():
	global p,q,g,msg,x, y
	k,k_ = number_gen(p,q,g)
	r = powmod(g,k,p) % q
	if r==0:
		signing(p,q,g,msg,x, y)
	m=hashlib.sha1()
	m.update(msg)
	z = int("0x" + m.hexdigest(), 0)
	s = (k_*(z+x*r)) % q
	if s==0:
		signing(p,q,g,msg,x, y)
	return (r, s)


def number_gen(p,q,g):
	k = random.randrange(1,q)
	try:
		k_ = inverse(k,q)
		return (k,k_) 
	except 'Inverse Error':
		return number_gen(p,q,g)

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

	s = socket.socket()
	s.connect((host,port))

	# message = input("->")

	p,q = signing()
	# print(r)
	message=str(p)+" "+str(q)
	# print(message)
	# message=mes+str(r)
	# print(message)
	
	# s.send(message.encode('utf-8'))

	while message != 'q' :
	# while (1):
		print("Signing is Successful ")
		s.send(message.encode())
		# s.send(message)
		data = s.recv(1024).decode()
		print("Recieved from server:"+data)
		message = input("->")
	s.close()
if __name__ == '__main__':
	Main()