from random import getrandbits
from math import sqrt
from sys import exit
import math
import random
import hashlib
from sys import stdin
L = 1024
N = 160
#z=x^c mod n
#Square and Multiply Algorithm
def powmod(x,c,n):
	c = '{0:b}'.format(c)
	z = 1
	l = len(c)
	for i in range(0, l):
		# z = (math.pow(z, 2)) % n
		z = (z**2)%n
		if (c[i] == "1"):
			z = (z*x) % n
	# print ("\nz = %d" % z)
	return z;
#Miller-Rabin Algorithm for primality test
def is_prime(n):
	k=40
	if n == 2:
		return True

	if n % 2 == 0:
		return False
	r, s = 0, n - 1
	while s % 2 == 0:
		r += 1
		s //= 2
	for _ in range(k):
		a = random.randrange(2, n - 1)
		x = pow(a, s, n)
		if x == 1 or x == n - 1:
			continue
		for _ in range(r - 1):
			x = pow(x, 2, n)
			if x == n - 1:
				break
		else:
			return False
	return True
# z^-1 mod a

'''
def inverse(A, M):
	for i in range(0, M):
		if (A*i) % M == 1:
			return i
	return -1
'''

#Extented Euclidean Algorithm
def inverse(a, m) :
	m0 = m
	y = 0
	x = 1
	if (m == 1) :
		return 0
	while (a > 1) :
		# q is quotient
		q = a // m
		t = m
		# m is remainder now, process
		# same as Euclid's algo
		m = a % m
		a = t
		t = y
		# Update x and y
		y = x - q * y
		x = t
	# Make x positive
	if (x < 0) :
		x = x + m0
	return x
# Per-Message Secret Number generator
def number_gen(p,q,g):
	# c = getrandbits(N+64)
	k = random.randrange(1,q)
	# c = random.randrange(1,q)
	# k = (c % (q-1))+1
	try:
		k_ = inverse(k,q)
		return (k,k_) 
	except 'Inverse Error':
		return number_gen(p,q,g)
# Sign opertation
def sign(p,q,g,msg,x, y):
	# global z

	k,k_ = number_gen(p,q,g)
	# print(k)
	# print(k_)
	r = powmod(g,k,p) % q
	if r==0:
		sign(p,q,g,msg,x, y)
	m=hashlib.sha1()
	m.update(msg)
	z = int("0x" + m.hexdigest(), 0)
	s = (k_*(z+x*r)) % q
	if s==0:
		sign(p,q,g,msg,x, y)
	print("r:"+str(r))
	print("s:"+str(s))

	return (r, s)

# Verify operation
def verify(p,q,g,msg,y,r,s):
	# global z
	if 0 < r and r < q and 0 < s and s < q:
		w = inverse(s, q)
		m=hashlib.sha1()
		m.update(msg)
		z = int("0x" + m.hexdigest(), 0)
		u1 = (z*w) % q
		u2 = (r*w) % q
		v = ((powmod(g,u1,p) * powmod(y,u2,p)) % p) % q
		return v == r
	raise Exception('Verify Error')
'''		
def is_valid(p,q,g):
	return  ( is_prime(p) and is_prime(q)
			and no_bits(p) == 1024 and no_bits(q) == 160
			and (p-1) % q == 0 and powmod(g,q,p) == 1 and g > 1)

'''
def is_valid(p,q,g):
	return  ( is_prime(p) and is_prime(q)
			and (p-1) % q == 0 and powmod(g,q,p) == 1 and g > 1)

# number of bits
def no_bits(p):
	# print(len(bin(p)))
	return (len(bin(p)[2:]))


# Generate a pair of keys
def key_pair_generation(p,q,g):
	# c = getrandbits(N+64)
	# c = random.randrange(1,q)
	x = random.randrange(1,q)
	# x = (c % (q-1)) + 1
	y = powmod(g,x,p)
	return (x,y)

if __name__=='__main__':

	p = int(input())
	q = int(input())
	g = int(input())
	msg=b"Mandela Mahato"

	'''
	print(no_bits(p))
	print(no_bits(q))
	print(no_bits(g))
	if(is_prime(p)):
		print("yes")
	else:
		print("no")
	if(is_prime(q)):
		print("yes")
	else:
		print("no")
	if((p-1) % q == 0 and powmod(g,q,p) == 1 and g > 1):
		print("yes")
	else:
		print("no")
	'''

	
	if not is_valid(p,q,g):
		print ('invalid_group')
		exit(-1)

	print ('valid_group')
	(x,y) = key_pair_generation(p,q,g)
	print ("x=Private: " + str(x))
	print ("y=Public: " + str(y))
	r,s = sign(p,q,g,msg,x,y)
	t=verify (p,q,g,msg,y,r,s)
	print(t)
	