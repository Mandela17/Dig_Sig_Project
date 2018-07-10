from random import getrandbits
from math import sqrt
from sys import exit
import math
import random
import hashlib
from Cryptodome.Math.Numbers import Integer
from Cryptodome.Math import Primality
import timeit

# generaing parameters p=1024 bits and q=160 bits and g
L_bit = 0
N_bit = 0



def power(x, y, p) :
	res = 1 
	x = x % p 
	while (y > 0) :

		if ((y & 1) == 1) :
			res = (res * x) % p

		y = y >> 1
		x = (x * x) % p
		 
	return res

def generate_p_q_g():
	global L_bit
	global N_bit
	start_1 = timeit.default_timer()
	p = Integer(4)
	while p.size_in_bits() != N_bit or Primality.test_probable_prime(p) != Primality.PROBABLY_PRIME:
		q=random.randrange(1 << L_bit-1, 1 << L_bit)
		if(is_prime(q)):
			z = Integer.random(exact_bits=N_bit-L_bit)
			p = z * q + 1

	stop_1 = timeit.default_timer()
	print("Time Required for P & Q: "+str(stop_1-start_1))
	start_2 = timeit.default_timer()
	h = Integer(2)
	g = 1
	while g == 1:
		g = power(int(h), int(z), int(p))
		h += 1

	stop_2 = timeit.default_timer()
	print("Time Required for G: "+str(stop_2-start_2))
	return (p, q, g)


#z=x^c mod n
#Square and Multiply Algorithm

def powmod(x,c,n):
	c = '{0:b}'.format(c)
	z = 1
	l = len(c)
	for i in range(0, l):
		z = (z**2)%n
		if (c[i] == "1"):
			z = (z*x) % n
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
#Extented Euclidean Algorithm

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



# Per-Message Secret Number generator

def number_gen(p,q,g):
	k = random.randrange(1,q)
	try:
		k_ = inverse(k,q)
		return (k,k_) 
	except 'Inverse Error':
		return number_gen(p,q,g)




# signing opertation

def signing(p,q,g,msg,x, y):
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
	print("r:"+str(r))
	print("s:"+str(s))
	return (r, s)


# verification operation

def verification(p,q,g,msg,y,r,s):
	if 0 < r and r < q and 0 < s and s < q:
		w = inverse(s, q)
		m=hashlib.sha1()
		m.update(msg)
		z = int("0x" + m.hexdigest(), 0)
		u1 = (z*w) % q
		u2 = (r*w) % q
		v = ((powmod(g,u1,p) * powmod(y,u2,p)) % p) % q
		return v == r
	raise Exception('verification Error')	

# Checking validity of parameters 

# def is_valid(p,q,g):
# 	return  ( is_prime(p) and is_prime(q)
# 			and no_bits(p) == 1024 and no_bits(q) == 160
# 			and (p-1) % q == 0 and powmod(g,q,p) == 1 and g > 1)


# number of bits

def no_bits(p):
	return (len(bin(p)[2:]))



# Generate a pair of keys Public key and Private key

def key_pair_generation(p,q,g):
	x = random.randrange(1,q)
	y = power(g,x,p)
	return (x,y)



if __name__=='__main__':

	msg=b"""The exoplanet is reported to be smaller than Saturn but bigger than Neptune. It is 27 times heavier than Earth and six times bigger in size.
It revolves around the star in about 19.5 days.host star is about 600 light years away from the Earth.
Prof Abhijit Chakraborty said that the new planet, which is 600 light years away from Earth, was between the size of Saturn and Neptune."""
	w = int(input("L_bit: "))
	z = int(input("N_bit: "))
	L_bit = w
	N_bit = z
	p,q,g= generate_p_q_g()
	p=int(p)
	q=int(q)
	g=int(g)
	print("P:"+str(p))
	print("Q:"+str(q))
	print("G:"+str(g))

	# if not is_valid(p,q,g):
	# 	print ('invalid_group')
	# 	exit(-1)
	# print ('valid_group')
	start_3 = timeit.default_timer()
	(x,y) = key_pair_generation(p,q,g)
	stop_3 = timeit.default_timer()
	print("Required Time for key_pair_generation :"+str(stop_3-start_3))
	print ("x=Private: " + str(x))
	print ("y=Public: " + str(y))
	r,s = signing(p,q,g,msg,x,y)
	t=verification (p,q,g,msg,y,r,s)
	print(t)
	