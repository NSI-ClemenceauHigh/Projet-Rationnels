class Rationnel:
    # Inatialization de l'instance
    def __init__(self, n, d=1):
        assert d != 0, "Le dénominateur ne peut pas être égal à 0"
        self.num = n
        self.den = d
        self.simplifier()
    
    # Pour permettre l'utilisation des objets de type Rationnel() en tant que strings (ie. les imprimer)
    def __str__(self):
        return "{}/{}".format(self.num, self.den)
    
    ############################################################################
    #############################    OPERATIONS    #############################
    ############################################################################
    
    def __mul__(self, r2):
        return (Rationnel(self.num * r2.num, self.den * r2.den))

    def __add__(self, r2):
        return(Rationnel(self.num * r2.den + r2.num * self.den, self.den * r2.den))

    def __sub__(self, r2):
        return(Rationnel(self.num * r2.den - r2.num * self.den, self.den * r2.den))

    def __truediv__(self, r2):
        return (Rationnel(self.num * r2.den, self.den * r2.num))

    ############################################################################
    ############################    COMPARAISONS    ############################
    ############################################################################
    
    def __eq__(self, r2):
        return self.num * r2.den == r2.num * self.den
        
    def __ne__(self, r2):
        return not self.__eq__(r2)

    def __ge__(self, r2):
        return self.num * r2.den >= r2.num * self.den

    def __le__(self, r2):
        return self.num * r2.den <= r2.num * self.den
    
    def __gt__(self, r2):
        return self.num * r2.den > r2.num * self.den

    def __lt__(self, r2):
        return self.num * r2.den < r2.num * self.den

    ############################################################################
    ################################    PGCD    ################################
    ############################################################################

    def pgcd(self):
        return self._pgcd(self.num, self.den)

    def _pgcd(self, a, b):
        if a == 0:
            return abs(b)
        else:
            return self._pgcd(b % a, a)

    ############################################################################
    ###############################    AUTRE    ################################
    ############################################################################

    def simplifier(self):
        pgcd = self.pgcd()
        self.num //= pgcd # division arrondie pour avoir direct des ints
        self.den //= pgcd
        if self.den < 0: # histoire de simplifier et rendre plus esthetique
            self.num = -self.num
            self.den = -self.den



#test normal 
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

print(f"Test égal (vrai): {Rationnel(1, 2) == Rationnel(2, 4)}")

print(f"Test égal (faux): {Rationnel(4, 3) == Rationnel(7, 9)}")

print(f"Test n'est pas égal (vrai): {Rationnel(6, 2) != Rationnel(8, 9)}")

print(f"Test n'est pas égal (faux): {Rationnel(3, 4) != Rationnel(6, 8)}")

print(f"Test plus grand ou égal (vrai): {Rationnel(8, 2) >= Rationnel(3, 5)}")

print(f"Test plus grand ou égal (faux): {Rationnel(8, 2) >= Rationnel(9)}")

print(f"Test plus petit ou égal (vrai): {Rationnel(3, 6) <= Rationnel(747, 5)}")

print(f"Test plus petit ou égal (faux): {Rationnel(63, 4) <= Rationnel(2, 27)}")

print(f"Test plus grand (vrai): {Rationnel(409, 12) > Rationnel(93, 30)}")

print(f"Test plus grand (faux): {Rationnel(23/7) > Rationnel(73, 4)}")

print(f"Test plus petit (vrai): {Rationnel(63, 42) < Rationnel(93, 6)}")

print(f"Test plus petit (faux): {Rationnel(34, 2) < Rationnel(2, 45)}")
