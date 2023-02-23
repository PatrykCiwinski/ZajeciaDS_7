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

print()
def get_data(number, discipline, **info):
    table ={}
    table["nr"]=number
    table["disc"]=discipline

    for k,v in info.items():
        table[k]=v

    return table


summary1=get_data(23,'basketball', team='Chicago Bulls',
                  name="Michael", surname="Jordan", height=1.98)
print()
print(summary1)