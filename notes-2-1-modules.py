#modules
#author: tim
# 11 march 2024

import random

#demonstrate some parts of the random module
#ram.random() -> (0,1.0] 0.999999

def coin_flip():
    #return either heads, tails, or others?
    #Heads -- (0,0.5)
    #Tails -- (0.5, 0.99999999]
    #other -- the rest
    results = random.random()
    if results<0.5:
        return "heads"
    elif results<0.999999999:
        return "tails"
    else:
        return "other"
    

def main():
    # repeat the coin flip 1000 times
    #keep track of heas, tail, and others
    heads=0
    tails=0
    other=0
    for x in range(100000000):
        results= coin_flip()

        if results == "heads":
            heads= heads+1
        elif results == "tails":
            tails+= 1
        elif results=="other":
            other+=1
    print(f"heads: {heads}")
    print(f"tails: {tails}")
    print(f"others: {other}")

main()

 