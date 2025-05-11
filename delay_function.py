from hashlib import sha256

# complexity
COMPLEXITY = 10
# modulus
N = 11

def delay_function(x: int, t: int):
    y = x
    for i in range(2 ** t):
        y = y * y % N
    return y

def generate_random(market_close_data):
    market_close_data = market_close_data
    hashed_bytes = sha256(market_close_data.encode('utf-8')).digest()
    market_close_data_hashed_int = int.from_bytes(hashed_bytes, byteorder='big')

    random_number = delay_function(market_close_data_hashed_int, COMPLEXITY)
    return random_number

## Attack vector
# before market close we want outcome 5 for example
# now we have to compute all the outcomes that will give us 5
# lets sey we can manipulate last digit by placing the last particular buy
prices = ['134.84','134.85', '134.86', '134.87', '134.88', '134.89', '134.90', '134.91',]

# now we have to calculate outcomes for all the prices
desired_random = 5

# this will take very long
for price in prices:
    random = generate_random(price)
    if random == desired_random:
        print('Big W')
        print('Found that if we manipulate market to ' + price + ' we will get the desired outcome')
        break
