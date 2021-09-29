
from math import floor
from matplotlib import pyplot as plt
from random import randrange
from noisecoin import *

def main():
    print("Main")

    # Create coin instance - bank starts with total supply
    coin = NoiseCoin()

    # Create N addresses
    
    N = 1000
    for i in range(N):
        coin.addressNumberDict[i] = Address(coin, str(i))
    
    # Amount (1/number) to initially distribute 
    distributeProportion = 2

    # Transfer a random amount to each address - from distribution amount
    distribute = coin.totalSupply/distributeProportion
    reserves = coin.bank.balance - distribute
    # Max amount that could be distributed evenly to all addresses
    maxStart = distribute/N
    # Minimum amount
    minStart = 1

    # Transfer initial amounts as random number between minStart, maxStart
    for i in range(N):
        amount = randrange(minStart, maxStart)
        Transfer(coin.bank, coin.addressNumberDict[i], amount)
        coin.addressNumberBalance[i] = amount
    
    remaining = coin.bank.balance - reserves
    # Pick a random address and amount until none left to distribute
    transferred = []
    untransferred = [x for x in range(N)]
    
    while(remaining>0):
        # Pick random amount
        remainingMax = floor(remaining/N)

        amount = randrange(0, remainingMax+1)
        
        # Pick random index of untransferred addresses
        index = randrange(0, len(untransferred))
        while(untransferred[index-1] in transferred):
            # Check if all addresses have been transferred
            if(len(untransferred) == 0):
                # Reset
                transferred = 0
                untransferred = [x for x in range(N)]
            # Pick another index
            index = randrange(0, len(untransferred))
        
        # Remove this addressInt from untransferred
        transferred.append(untransferred[index-1]) 
        untransferred.remove(untransferred[index-1])
        
        # Transfer random amount to this address
        addressInt = untransferred[index-1]
        Transfer(coin.bank, coin.addressNumberDict[addressInt], amount)
        coin.addressNumberBalance[addressInt] += amount
        # Calculate remaining available to distribute
        remaining = coin.bank.balance - reserves
    
    sortedBalances = sorted(coin.addressNumberBalance.values(), reverse=True)
    fig, axs = plt.subplots()
    axs.plot(sortedBalances)
    plt.show()

    
    print("Richest person: " + str(max(coin.addressNumberBalance.values())))
    print("Poorest person: " + str(min(coin.addressNumberBalance.values())))
    print("Remaining available to distribute: " + f"{coin.bank.balance - reserves:,}")
    print("hi")
    
    


    


if(__name__ == "__main__"):
    main()