import random
import math
import timeit

def no_bits(p):
	# print(len(bin(p)))
	return (len(bin(p)[2:]))
# naive algorithm
def is_prime_1(n):
	if n <= 1:
		return False
	for i in range(2, n):
		if n % i == 0:
			return False;
	return True
# SieveOfEratosthenes
def is_prime_2(n):
	n=n+1
	prime = [True for i in range(n+1)]
	p = 2
	while (p * p <= n):
		if (prime[p] == True):

			for i in range(p * 2, n+1, p):
				prime[i] = False
		p += 1
	if(prime[n-1]):
		return True
	else:
		return False
# fermats algorithm
def is_prime_3(n):
	k=100
	# Implementation uses the Fermat Primality Test
	
	# If number is even, it's a composite number

	if n == 2:
		return True

	if n % 2 == 0:
		return False

	for i in range(k):
		a = random.randrange(1, n-1)
		# if pow(a, n-1) % n != 1:
		if powmod(a, n-1,n)!=1:
			return False
	return True
# Miller_Rabin algorithm
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
	

#z=x^c mod n

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
def calculate_g(p,q):
	e=int('%i'% ((p-1)/q))
	# e=(p-1)%q;
	# print("E"+str(e))
	# h=2
	# return(powmod(h,e,p))
	while(1):
		h=random.randrange(1,p-1)
		g=pow(h,e,p)
		if(pow(g,q,p) == 1 and g > 1):
			break
	# 	g=powmod(h,e,p)
	# 	print("Temp G"+str(g))
	# 	g=(h**e)%p
	# 	if(pow(g,q,p) == 1 and g > 1):
	# # 	# if((g**q)%p == 1 and g > 1):
	# 		break
	# h=2
	# while(1 and h<p):
	# 	print("h"+str(h))
	# 	g=pow(h,e,p)
	# 	if(pow(g,q,p) == 1 and g > 1):
	# 		break

	# 	h+=1
	# 	g=pow(h,e,p)
	return g




def main():
	q_L=int(input("choose L bit:"))
	p_N=int(input("choose N bit:"))
	while(1):
		print("1:naive\n2:SieveOfEratosthenes\n3:fermats\n4:Miller_Rabin\n")
		w=int(input())
		if w==1:
			start=timeit.default_timer()
			flag=0
			while(1):
				q=random.randrange(1 << q_L-1, 1 << q_L)
				# q=random.getrandbits(q_L)
				if(is_prime_1(q)):
					# print("mandela2")
					# print("mandela2")
					for i in range(1,4096):
						m=random.randrange(1 << p_N-1, 1 << p_N)
						# m=random.getrandbits(p_N)
						mr=m%(2*q)
						p=m-mr+1
						if(is_prime_1(p)):

							# print("mandela111")

							
							# print(p)
							# print(q)
							# g=calculate_g(p,q)
							print("P: "+str(p))
							print("Q: "+str(q))
							# print("G: "+str(g))

							stop=timeit.default_timer()
							print("Time Reqiued: "+str(stop-start))
							# print(g)
							# print(isinstance(l,float))
							# print(g)
							flag=1
							break
					# print(p)
					# print(q)
					# print(no_bits(q))
				if(flag==1):
					break
	
		if w==2:
			start=timeit.default_timer()
			flag=0
			while(1):
				# q=random.getrandbits(q_L)
				q=random.randrange(1 << q_L-1, 1 << q_L)
				if(is_prime_2(q)):
					# print("mandela2")
					# print("mandela2")
					for i in range(1,4096):
						m=random.randrange(1 << p_N-1, 1 << p_N)
						# m=random.getrandbits(p_N)
						mr=m%(2*q)
						p=m-mr+1
						if(is_prime_2(p)):

							# print("mandela111")

							
							# print(p)
							# print(q)
							# g=calculate_g(p,q)
							print("P: "+str(p))
							# l=(p)/q
							print("Q: "+str(q))
							stop=timeit.default_timer()
							print("Time Reqiued: "+str(stop-start))
							# print(g)
							# print(isinstance(l,float))
							# print(g)
							flag=1
							break
					# print(p)
					# print(q)
					# print(no_bits(q))
				if(flag==1):
					break
		if w==3:
			start=timeit.default_timer()
			flag=0
			while(1):
				# q=random.getrandbits(q_L)
				q=random.randrange(1 << q_L-1, 1 << q_L)
				if(is_prime_3(q)):
					# print("mandela2")
					# print("mandela2")
					for i in range(1,4096):
						# m=random.getrandbits(p_N)
						m=random.randrange(1 << p_N-1, 1 << p_N)
						mr=m%(2*q)
						p=m-mr+1
						if(is_prime_3(p)):

							# print("mandela111")

							
							# print(p)
							# print(q)
							# g=calculate_g(p,q)
							print("P: "+str(p))
							# l=(p)/q
							print("Q: "+str(q))
							stop=timeit.default_timer()
							print("Time Reqiued: "+str(stop-start))
							# print(g)
							# print(isinstance(l,float))
							# print(g)
							flag=1
							break
					# print(p)
					# print(q)
					# print(no_bits(q))
				if(flag==1):
					break
		if w==4:
			start=timeit.default_timer()
			flag=0
			while(1):
				# q=random.getrandbits(q_L)
				q=random.randrange(1 << q_L-1, 1 << q_L)
				if(is_prime_4(q)):
					# print("mandela2")
					# print("mandela2")
					for i in range(1,4096):
						# m=random.getrandbits(p_N)
						m=random.randrange(1 << p_N-1, 1 << p_N)
						mr=m%(2*q)
						p=m-mr+1
						if(is_prime_4(p)):

							# print("mandela111")

							
							# print(p)
							# print(q)
							# t=int('%i'% ((p-1)/q))
							# w=(2**t)%p
							# print("t:"+str(t))

							'''
							g=calculate_g(p,q)
							with open("par.txt",'a') as out:
								print("P: "+str(p))
								print("P: "+str(no_bits(p)))
								out.write(str(p)+'\n')
							
								print("Q: "+str(q))
								print("Q: "+str(no_bits(q)))
								out.write(str(q)+'\n')
		
								print("G: "+str(g))
								print("G: "+str(no_bits(g)))
								out.write(str(g)+'\n')

							
 # and powmod(g,q,p) == 1 and g > 1
							if(is_prime_4(p) and is_prime_4(q) and (p-1) % q == 0 and powmod(g,q,p) == 1 and g > 1):
							 	print("Mandela Mahato")

							'''
								
							# print(t)
							
							# "{0:b}".format((p-1)/q)

							print("P: "+str(p))
							# l=(p)/q
							print("Q: "+str(q))

							stop=timeit.default_timer()
							print("Time Reqiued: "+str(stop-start))
							# print(g)
							# print(isinstance(l,float))
							# print(g)
							flag=1
							break
					# print(p)
					# print(q)
					# print(no_bits(q))
				if(flag==1):
					break

main()