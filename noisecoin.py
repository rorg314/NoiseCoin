


# Noise token class
class NoiseToken():
    def __init__(self, totalSupply=1e9):
        # Total available supply
        self.totalSupply = totalSupply


# Initialise a new address
class Address():
    def __init__(self, name):
        self.name = name
        self.balance = 0