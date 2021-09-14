import random


# Noise token class
class NoiseToken():
    def __init__(self, totalSupply=1e9, coinValue=1):
        # Total available supply
        self.totalSupply = totalSupply
        # Coin value
        self.coinValue = coinValue
        # Maximum fraction of total supply that may be minted/burnt 
        self.maxFraction = 0.01
        # Bank address to store unminted tokens
        self.bank = Address("bank")
        # Eater address to store burned tokens
        self.eater = Address("eater")


# Initialise a new address
class Address():
    def __init__(self, name):
        self.name = name
        self.balance = 0


# ======================================================== #
# ==================== ERC-20 PROTOCOL =================== #
# ======================================================== #


def Transfer(sender:Address, receiver:Address, amount:int):
    sender.balance -= amount
    receiver.balance += amount



# ======================================================== #
# ================= TOKEN BURNING/MINTING ================ #
# ======================================================== #

def GetNoiseValue():
    return random.random()


def ProcessNoiseValue(noiseValue):
    if(noiseValue >= 0.5):
        BurnTokens()
    if(noiseValue < 0.5):
        MintTokens()


def BurnTokens(token:NoiseToken, amount):
    maxAmount = token.totalSupply * token.maxFraction
    amount = maxAmount * GetNoiseValue()
    token.totalSupply -= amount
    Transfer(token.bank, token.eater, amount) 

def MintTokens(token:NoiseToken, amount):
    maxAmount = token.totalSupply * token.maxFraction
    amount = maxAmount * GetNoiseValue()
    token.totalSupply += amount


