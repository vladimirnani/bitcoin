from hashlib import sha256

# the salt should be random between rounds
# prevents someone detecting if the same number is chosen
party_a_secret = (11, 'salt123')
party_b_secret = (13, 'salt345')
party_c_secret = (101, 'salt678')

# commitment
party_a_commit = sha256((str(party_a_secret[0]) + party_a_secret[1]).encode('utf-8')).hexdigest()
party_b_commit = sha256((str(party_b_secret[0]) + party_b_secret[1]).encode('utf-8')).hexdigest()
party_c_commit = sha256((str(party_c_secret[0]) + party_c_secret[1]).encode('utf-8')).hexdigest()
# shows hashes to everyone (without the secret number reveal)
# everyone saves the hashes

# reveal
# everyone gives the number
print(party_a_secret)
print(party_b_secret)
print(party_c_secret)

# verify
# verifier recomputes the hashes and checks if they are equal to what was commited

# we xor to hide the choices of others
r = party_a_secret[0] ^ party_b_secret[0] ^ party_c_secret[0]
print(r)
