class Rationnel:
    def __init__(self, n, d=1):
        assert d != 0, "Le dénominateur ne peut pas être égal à 0"
        self.num = n
        self.den = d
        self.simplifier()

    def __str__(self):
        return "{}/{}".format(self.num, self.den)
    
    def __mul__(self, r2):
        return (Rationnel(self.num * r2.num, self.den * r2.den))

    def __add__(self, r2):
        return(Rationnel(self.num * r2.den + r2.num * self.den, self.den * r2.den))

    def __sub__(self, r2):
        return(Rationnel(self.num * r2.den - r2.num * self.den, self.den * r2.den))

    def __truediv__(self, r2):
        return(Rationnel(self.num * r2.den, self.den * r2.num))

    def pgcd(self):
        return self._pgcd(self.num, self.den)

    def _pgcd(self, a, b):
        if a == 0:
            return abs(b)
        else:
            return self._pgcd(b % a, a)

    def simplifier(self):
        pgcd = self.pgcd()
        self.num //= pgcd # division arrondie pour avoir direct des ints
        self.den //= pgcd
        if self.den < 0: # histoire de simplifier et rendre plus esthetique
            self.num = -self.num
            self.den = -self.den



# test normal 
rat = Rationnel(36, 12)
print(f"Test instanciation: {rat}\n")

# test avec paramètre unique
rat1 = Rationnel(5)
print(f"Test instanciation sans denumerateur: {rat1}\n")

rat2 = Rationnel(42, 7)

print(f"Test multiplication: {rat * rat2}\n")

print(f"Test addition: {rat + rat2}\n")

print(f"Test soustraction: {rat - rat2}\n")

print(f"Test division: {rat / rat2}\n")
