def add_five(x):
    return x+5

list_nums=list(range(101))

print(list(map(add_five,list_nums)))

print()

def even(x):
    return x%2==0

print(list(filter(even,list_nums)))
# the same thing using lambda we don't need to create any function
print(list(filter((lambda x:(x%2==0)),list_nums)))