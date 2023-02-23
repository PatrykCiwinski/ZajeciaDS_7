from functools import reduce

list_nums=list(range(2,1000))
primes = lambda x: all(map(lambda s: x % s, range(2, x)))
print(list(filter(primes,list_nums)))


nums=range(1,101)
print(reduce(lambda x,y:x+y,nums))

def fun(a,b):
    return a+b
#to jest to samo, muszę wcześniej stworzyć funkcję
print(reduce(fun,nums))