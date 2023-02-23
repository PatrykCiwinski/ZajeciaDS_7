products = ['soap','sponge','brush','shower_gel','rubber_duck','shampoo']

purchase=[]

def buying(products, purchase):
    while products:
        stuff=products.pop()
        print(f"buying {stuff}")
        purchase.append(stuff)


def show_purchase(purchase):
    print(f"You bought: ",end="")
    for p in purchase:
        print(p,end=",")


buying(products,purchase)
print("_________________")
show_purchase(purchase)
