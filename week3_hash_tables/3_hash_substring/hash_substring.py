# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def _hash_func(s, prime, multiplier):
        ans = 0
        for c in reversed(s):
            ans = (ans * multiplier + ord(c)) % prime
        return ans

def precomputeHash(text, len_pattern, prime, multiplier):
    # H is an array of hashes, size is len_text - len_pattern + 1
    # S is initialised to the last substring of size len_pattern
    # H[-1] is the hash value of S
    # compute iteratively the hash values from the (second) last to first substring
    
    # Beware of taking negative numbers (mod 𝑝). In many programming languages,
    # (−2) % 5 = 3 % 5. Thus you can compute the same hash values for two strings, 
    # but when you compare them, they appear to be different. To avoid this issue, 
    # you can use such construct in the code: 𝑥 = ((𝑎 % 𝑝) + 𝑝) % 𝑝 instead of just
    # 𝑥 = 𝑎 % 𝑝

    H = [None for i in range(len(text) - len_pattern + 1)]
    S = text[len(text) - len_pattern:]
    H[-1] = _hash_func(S, prime, multiplier)

    y = 1
    for i in range(len_pattern):
        y = (y * multiplier) % prime

    for i in range(len(H) - 2, -1, -1):
        H[i] = (multiplier * H[i+1] + ord(text[i]) - y * ord(text[i+len_pattern])) % prime
        
    return H

def get_occurrences(pattern, text, prime, multiplier):
    # Use operator == in Python instead of implementing your own function
    # AreEqual for strings, because built-in operator == will work much faster.
    result = []
    pattern_hash = _hash_func(pattern, prime, multiplier)
    H = precomputeHash(text, len(pattern), prime, multiplier)

    for i in range(len(text) - len(pattern) + 1): 
        if H[i] != pattern_hash:
            continue
        if text[i:i + len(pattern)] == pattern:
            result.append(i)
    return result
    

if __name__ == '__main__':
    pattern, text = read_input()
    prime = 10000000019
    multiplier = 263
    print_occurrences(get_occurrences(pattern, text, prime, multiplier))

