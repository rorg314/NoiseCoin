import random


# Noise coin class
class NoiseCoin():
    def __init__(self, totalSupply=1e6, coinValue=1):
        # Total available supply
        self.totalSupply = totalSupply
        # Coin value
        self.coinValue = coinValue
        # Maximum fraction of total supply that may be minted/burnt 
        self.maxFraction = 0.01
        # Bank address to store unminted tokens
        self.bank = Address(self, "bank", balance=totalSupply)
        # Eater address to store burned tokens
        self.eater = Address(self, "eater")

        # Dict with address number -> address
        self.addressNumberDict = dict()
        # Dict with address number -> address balance
        self.addressNumberBalance = dict()


# Initialise a new address
class Address():
    def __init__(self, coin:NoiseCoin, name:str, balance=0):
        self.coin = coin
        self.name = name
        self.balance = balance


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


def BurnTokens(coin:NoiseCoin, amount):
    maxAmount = coin.totalSupply * coin.maxFraction
    amount = maxAmount * GetNoiseValue()
    coin.totalSupply -= amount
    Transfer(coin.bank, coin.eater, amount) 

def MintTokens(coin:NoiseCoin, amount):
    maxAmount = coin.totalSupply * coin.maxFraction
    amount = maxAmount * GetNoiseValue()
    coin.totalSupply += amount


