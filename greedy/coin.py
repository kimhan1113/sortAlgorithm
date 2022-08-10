

from numpy import array


n = 1260

arrays = [500, 100, 50, 10]
count = 0

for coin in arrays:
    count += n // coin
    n %= coin

print(count)    