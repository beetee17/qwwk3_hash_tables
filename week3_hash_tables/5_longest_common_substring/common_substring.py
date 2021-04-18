# python3

import sys
from collections import namedtuple
# python3

import sys

Answer = namedtuple('answer_type', 'i j len')

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
	def __init__(self, s, t, prime1, prime2, multiplier):
		self.s = s
		self.t = t
		self.multiplier = multiplier
		self.prime1 = prime1
		self.prime2 = prime2

		self.h1_s, self.h2_s = precomputeHash(s, 
										  prime1, 
										  prime2, 
										  multiplier)
		self.h1_t, self.h2_t = precomputeHash(t, 
										  prime1, 
										  prime2, 
										  multiplier)

		self.lo = 1
		self.hi = min(len(s), len(t))
		self.ans = [Answer(0,0,0)]
		
	def computeSubHash(self, s, t, l):
		
		#  (a + b) mod n = [(a mod n) + (b mod n)] mod n
		# however h[i] was already modded so you can ignore the 1st mod
		# therefore, e.g. hash_a1 = (h1[a + l] - (x^length % m1 ) * h1[a]) % m
		# built in pow(x,y,z) which computes x^y % z is much faster than x**y iteratively due to modular exponentiation

		hash_1s = {}
		
		hash_2s = {}
		
		
		hash_1t = {}
		
		hash_2t = {}

		for a in range(len(s)-l+1):
		
			hash_a1 =  safe_mod(self.h1_s[a+l] - (pow(self.multiplier, l, self.prime1) * self.h1_s[a]), self.prime1)

			hash_a2 = safe_mod(self.h2_s[a+l] - (pow(self.multiplier, l, self.prime2) * self.h2_s[a]), self.prime2)

			hash_1s.update({hash_a1 : a})
			hash_2s.update({a : hash_a2})

		for b in range(len(t)-l+1):
			
			hash_b1 = safe_mod(self.h1_t[b+l] - (pow(self.multiplier, l, self.prime1) * self.h1_t[b]), self.prime1)

			hash_b2 = safe_mod(self.h2_t[b+l] - (pow(self.multiplier, l, self.prime2) * self.h2_t[b]), self.prime2)

			hash_1t.update({hash_b1 : b})
			hash_2t.update({b : hash_b2})
		
		
		return hash_1s, hash_1t, hash_2s, hash_2t

	def longest_common_substring(self):
		# print(self.lo, self.hi)
		if self.lo > self.hi:
			return self.ans
		
		mid = self.hi // self.lo

		hash_1s, hash_1t, hash_2s, hash_2t = self.computeSubHash(self.s, self.t, mid)

		found_substring = False

		for k, v in hash_1s.items():
			if k in hash_1t:
				i = v
				j = hash_1t[k]
				if hash_2s[i] == hash_2t[j]:
					found_substring = True
					self.ans.append(Answer(i, j, mid))


		if found_substring:

			self.lo = mid + 1
						
		else:
			
			self.hi = mid - 1

		return self.longest_common_substring()

def solve(s, t):
	ans = Answer(0, 0, 0)
	for i in range(len(s)):
		for j in range(len(t)):
			for l in range(min(len(s) - i, len(t) - j) + 1):
				if (l > ans.len) and (s[i:i+l] == t[j:j+l]):
					ans = Answer(i, j, l)
	return ans


def fast_solve(s, t):
	solver = Solver(s, t, 10**9 + 7, 10**9 + 9, 107)
	ans = solver.longest_common_substring()
	# ans = solver.lcs(3)
	# print(ans)
	ans = sorted(ans, key=lambda x: x.len)
	return ans[-1]

for line in sys.stdin.readlines():
	s, t = line.split()
	# ans = solve(s, t)
	ans =fast_solve(s, t)
	print(ans.i, ans.j, ans.len)
