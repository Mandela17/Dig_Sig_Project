from Cryptodome.Math.Numbers import Integer
from Cryptodome.Math import Primality
import random

import random
import math
import timeit


def powmod(x,c,n):
	c = '{0:b}'.format(c)
	z = 1
	l = len(c)
	for i in range(0, l):
		z = (z**2)%n
		if (c[i] == "1"):
			z = (z*x) % n
	return z;



def power(x, y, p) :
	res = 1 
	x = x % p 
	while (y > 0) :

		if ((y & 1) == 1) :
			res = (res * x) % p

		y = y >> 1
		x = (x * x) % p
		 
	return res

def is_prime_4(n):
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
		x = powmod(a, s, n)
		if x == 1 or x == n - 1:
			continue
		for _ in range(r - 1):
			x = powmod(x, 2, n)
			if x == n - 1:
				break
		else:
			return False
	return True


def generate_p_q_g():
	p = Integer(4)
	while p.size_in_bits() != 1024 or Primality.test_probable_prime(p) != Primality.PROBABLY_PRIME:
		q=random.randrange(1 << 159, 1 << 160)
		if(is_prime_4(q)):
			z = Integer.random(exact_bits=1024-160)
			p = z * q + 1

	h = Integer(2)
	g = 1
	while g == 1:
		g = powmod(int(h), int(z), int(p))
		h += 1
	return (p, q, g)
	# return(p,q)
if __name__ == '__main__':
	start=timeit.default_timer()
	p,q,g=generate_p_q_g()
	stop=timeit.default_timer()
	print("Time Reqiued: "+str(stop-start))
	# p,q = generate_p_q_g()
	with open("par_lib.txt",'a') as out:
		print("P: "+str(p))
		out.write(str(p)+'\n')
		print("Q: "+str(q))
		out.write(str(q)+'\n')
		print("G: "+str(g))
		out.write(str(g)+'\n')
	if((p-1) % q == 0 and powmod(int(g),int(q),int(p)) == 1 and g > 1):
		print("mfdsfghj")

	# if((p-1) % q) == 0:
	# 	print("mandela")