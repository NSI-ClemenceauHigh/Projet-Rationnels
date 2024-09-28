class Rationnel:
    """
    Classe qui représente un nombre rationnel sous la forme numérateur/dénominateur

    ATTRIBUTS:
        num (int): numérateur du rationnel
        den (int): dénominateur du rationnel (non nul)
    """

    def __init__(self, n, d=1):
        """
        Initialize un objet de la classe Rationnel

        ARGUMENTS
            n (int): numérateur
            d (int): dénominateur
        RAISES
            AssertionError: Si d égal à 0
        """
        assert d != 0, "Le dénominateur ne peut pas être égal à 0"
        self.num = n
        self.den = d
        self.simplifier()
    
    def __str__(self):
        """
        Définit la représentation sous forme de string d'un objet Rationnel

        RENVOIE
            str: représentation du rationnel sous forme de string
        """
        return "{}/{}".format(self.num, self.den)
    
    ############################################################################
    #############################    OPERATIONS    #############################
    ############################################################################
    
    def __mul__(self, r2):
        """
        Multiplie deux rationnels

        ARGUMENTS
            r2 (Rationnel): Le rationnel a multiplier
        RENVOIE
            Rationnel: Le produit des deux rationnels
        """
        return (Rationnel(self.num * r2.num, self.den * r2.den))

    def __add__(self, r2):
        """
        Additionne deux rationnels

        ARGUMENTS
            r2 (Rationnel): Le rationnel à additionner
        RENVOIE
            Rationnel: La somme des deux rationnels
        """
        return(Rationnel(self.num * r2.den + r2.num * self.den, self.den * r2.den))

    def __sub__(self, r2):
        """
        Soustrait deux rationnels

        ARGUMENTS
            r2 (Rationnel): Le rationnel à soustraire
        RENVOIE
            RENVOIE: La différence des deux rationnels
        """
        return(Rationnel(self.num * r2.den - r2.num * self.den, self.den * r2.den))

    def __truediv__(self, r2):
        """
        Divise deux rationnels

        ARGUMENTS
            r2 (Rationnel): Le rationnel par lequel diviser
        RENVOIE
            Rationnel: Le quotient des deux rationnels
        """
        return (Rationnel(self.num * r2.den, self.den * r2.num))

    ############################################################################
    ############################    COMPARAISONS    ############################
    ############################################################################
    
    def __eq__(self, r2):
        """
        Vérifie l'égalité entre deux rationnels

        ARGUMENTS
            r2 (Rationnel): Le rationnel à comparer
        RENVOIE
            bool: True si les rationnels sont égaux, False sinon
        """
        return self.num * r2.den == r2.num * self.den
        
    def __ne__(self, r2):
        """
        Vérifie l'inégalité entre deux rationnels

        ARGUMENTS
            r2 (Rationnel): Le rationnel à comparer
        RENVOIE
            bool: True si les deux rationnels ne sont pas égaux, False sinon
        """
        return not self.__eq__(r2)

    def __ge__(self, r2):
        """
        Vérifie si le rationnel actuel est supérieur ou égal à un autre

        ARGUMENTS
            r2 (Rationnel): Le rationnel à comparer
        RENVOIE
            bool: True si le rationnel actuel est supérieur ou égal, False sinon
        """
        return self.num * r2.den >= r2.num * self.den

    def __le__(self, r2):
        """
        Vérifie si le rationnel actuel est inférieur ou égal à un autre

        ARGUMENTS
            r2 (Rationnel): Le rationnel à comparer
        RENVOIE
            bool: True si le rationnel actuel est inférieur ou égal, False sinon
        """

        return self.num * r2.den <= r2.num * self.den
    
    def __gt__(self, r2):
        """
        Vérifie si le rationnel actuel est supérieur à un autre

        ARGUMENTS
            r2 (Rationnel): Le rationnel à comparer
        RENVOIE
            bool: True si le rationnel actuel est supérieur, False sinon
        """

        return self.num * r2.den > r2.num * self.den

    def __lt__(self, r2):
        """
        Vérifie si le rationnel actuel est inférieur un autre

        ARGUMENTS
            r2 (Rationnel): Le rationnel à comparer
        RENVOIE
            bool: True si le rationnel actuel est inférieur, False sinon
        """

        return self.num * r2.den < r2.num * self.den

    ############################################################################
    ################################    PGCD    ################################
    ############################################################################

    def pgcd(self):
        """
        Calcule le PGCD du numérateur et dénominateur

        RENVOIE:
            int: PGCD de self.num et self.den
        """
        return self.__pgcd(self.num, self.den)

    # '__' pour indiquer que la méthode est privée et ne devrait donc pas être utilisé en dehors de la classe
    def __pgcd(self, a, b):
        """
        Calcule le PGCD de deux nombres

        A
        """
        if a == 0:
            return abs(b)
        else:
            return self.__pgcd(b % a, a)

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

    @staticmethod
    def moyenne(tabRationnels):
        """
        Calcule la moyenne d'une liste d'objets Rationnel

        ARGUMENTS
            tabRationnels (list): Liste d'objets Rationnel
        RENVOIE
            Rationnel: un objet Rationnel qui représente la moyenne des éléments de la liste
        """
        if len(tabRationnels) == 0:
            raise ValueError("La liste ne doit pas être vide")

        # on calcule la somme de tous les rationnels
        somme = Rationnel(0)
        for rationnel in tabRationnels:
            somme += rationnel

        nbElements = len(tabRationnels)
        moyenne = somme / Rationnel(nbElements)

        return moyenne

############################################################################
###############################    TESTS    ################################
############################################################################

#Les tests sont enfermés dans des parentheses ou des appels à str() car dû à la
#comparaioson, python les convertirait en strings ou en booléens et causerait des erreurs

#test normal 
rat = Rationnel(36, 12)
assert str(rat) == "3/1" 

# test avec paramètre unique
rat1 = Rationnel(5)
assert str(rat1) == "5/1"

rat2 = Rationnel(42, 7)
assert str(rat * rat2) == "18/1"
assert str(rat + rat2) == "9/1"
assert str(rat - rat2) == "-3/1"
assert str(rat / rat2) == "1/2"
assert (Rationnel(1, 2) == Rationnel(2, 4)) == True
assert (Rationnel(4, 3) == Rationnel(7, 9)) == False
assert (Rationnel(6, 2) != Rationnel(8, 9)) == True
assert (Rationnel(3, 4) != Rationnel(6, 8)) == False
assert (Rationnel(8, 2) >= Rationnel(3, 5)) == True
assert (Rationnel(8, 2) >= Rationnel(9)) == False
assert (Rationnel(3, 6) <= Rationnel(747, 5)) == True
assert (Rationnel(63, 4) <= Rationnel(2, 27)) == False
assert (Rationnel(409, 12) > Rationnel(93, 30)) == True
assert (Rationnel(23/7) > Rationnel(73, 4)) == False
assert (Rationnel(63, 42) < Rationnel(93, 6)) == True
assert (Rationnel(34, 2) < Rationnel(2, 45)) == False

# test de la méthode moyenne
rat3 = Rationnel(1, 2)
rat4 = Rationnel(2, 3)
rat5 = Rationnel(3, 4)
moy = Rationnel.moyenne([rat3, rat4, rat5])
assert str(moy) == "23/36"
print(f"Test moyenne: {moy}")
