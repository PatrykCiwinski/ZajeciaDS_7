
list_nums=list(range(2,1000))
primes = lambda x: all(map(lambda s: x % s, range(2, x)))
print(list(filter(primes,list_nums)))