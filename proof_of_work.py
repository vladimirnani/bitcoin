from hashlib import sha256

message = b"Bob sends 100BTC to Vladimir"
sha_ = sha256(message)

hexdigest = sha_.hexdigest()
print(hexdigest)

search_term = '00000'


def proof_of_work() -> (int, str):
    nonce = 0
    while True:
        search_for = f'{nonce}{message}'
        attempt = sha256(str(search_for).encode('utf-8')).hexdigest()
        if attempt.startswith(search_term):
            print('took long but found that random plus message is this')
            print(attempt)
            return nonce, attempt
        nonce += 1

# miner
# miner find a hash that starts with 0000 which is also a hash of message
miners_nonce, miners_hash = proof_of_work()

# verifier
# verifier has the message but wants to verify that indeed work of finding nonce was found
verification = f'{miners_nonce}{message}'.encode('utf-8')
verifiers_hash = sha256(verification).hexdigest()
print('Verifier:')
print(verifiers_hash)
