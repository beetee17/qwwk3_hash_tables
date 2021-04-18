# python3

import sys


def _hash_func(s, prime, multiplier):
        ans = 0
        for c in reversed(s):
            ans = (ans * multiplier + ord(c)) % prime
        return ans

def safe_mod(x, m):
	return ((x % m) + m) % m

def precomputeHash(s, prime1, prime2, multiplier):
    
    # Beware of taking negative numbers (mod 𝑝). In many programming languages,
    # (−2) % 5 = 3 % 5. Thus you can compute the same hash values for two strings, 
    # but when you compare them, they appear to be different. To avoid this issue, 
    # you can use such construct in the code: 𝑥 = ((𝑎 % 𝑝) + 𝑝) % 𝑝 instead of just
    # 𝑥 = 𝑎 % 𝑝
	
	h1 = [None for i in range(len(s)+1)]
	h1[0] = 0

	for i in range(1, len(s)+1):
		h1[i] = safe_mod((multiplier * h1[i-1] + ord(s[i-1])), prime1)

	h2 = [None for i in range(len(s)+1)]
	h2[0] = 0

	for i in range(1, len(s)+1):
		h2[i] = safe_mod((multiplier * h2[i-1] + ord(s[i-1])), prime2)
		
			
	return h1, h2



class Solver:
	def __init__(self, s, prime1, prime2, multiplier):
		self.s = s
		self.multiplier = multiplier
		self.prime1 = prime1
		self.prime2 = prime2
		self.h1, self.h2 = precomputeHash(s, 
										  prime1, 
										  prime2, 
										  multiplier)
		
	def ask(self, a, b, l):
		
		#  (a + b) mod n = [(a mod n) + (b mod n)] mod n
		# however h[i] was already modded so you can ignore the 1st mod
		# therefore, e.g. hash_a1 = (h1[a + l] - (x^length % m1 ) * h1[a]) % m
		# built in pow(x,y,z) which computes x^y % z is much faster than x**y iteratively due to modular exponentiation
		hash_a1 =  safe_mod(self.h1[a+l] - (pow(self.multiplier, l, self.prime1) * self.h1[a]), self.prime1)

		hash_b1 = safe_mod(self.h1[b+l] - (pow(self.multiplier, l, self.prime1) * self.h1[b]), self.prime1)

		
		if hash_a1 == hash_b1:

			hash_a2 = safe_mod(self.h2[a+l] - (pow(self.multiplier, l, self.prime2) * self.h2[a]), self.prime2)

			hash_b2 = safe_mod(self.h2[b+l] - (pow(self.multiplier, l, self.prime2) * self.h2[b]), self.prime2)
			
			if hash_a2 == hash_b2:

				return True

		return False

s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s, 10**9 + 7, 10**9 + 9, 31)



for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(a, b, l) else "No")
