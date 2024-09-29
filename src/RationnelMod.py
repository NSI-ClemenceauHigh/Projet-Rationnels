"""
Copie de la classe Rationnel à l'exception de la définition de la méthode __pgcd qui à présent,
est un import d'une librairie dynamique (compilée du C pour permettre d'une part de passer outre la restriction
de récurrence, et d'autre part d'être un peu plus rapide)
"""

import os
import ctypes

# on importe la librairie dynamique selon l'OS
if os.name == "nt": #Windows
    libpgcd = ctypes.CDLL("./libs/pgcd.dll")
else:
    libpgcd = ctypes.CDLL("./libs/libpgcd.so")

# déclaration des types d'args et return
libpgcd.pgcd.argtypes = [ctypes.c_int, ctypes.c_int]
libpgcd.pgcd.restype = ctypes.c_int

class RationnelMod:
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
        return (RationnelMod(self.num * r2.num, self.den * r2.den))

    def __add__(self, r2):
        """
        Additionne deux rationnels

        ARGUMENTS
            r2 (Rationnel): Le rationnel à additionner
        RENVOIE
            Rationnel: La somme des deux rationnels
        """
        return(RationnelMod(self.num * r2.den + r2.num * self.den, self.den * r2.den))

    def __sub__(self, r2):
        """
        Soustrait deux rationnels

        ARGUMENTS
            r2 (Rationnel): Le rationnel à soustraire
        RENVOIE
            Rationnel: La différence des deux rationnels
        """
        return(RationnelMod(self.num * r2.den - r2.num * self.den, self.den * r2.den))

    def __truediv__(self, r2):
        """
        Divise deux rationnels

        ARGUMENTS
            r2 (Rationnel): Le rationnel par lequel diviser
        RENVOIE
            Rationnel: Le quotient des deux rationnels
        """
        return (RationnelMod(self.num * r2.den, self.den * r2.num))

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
        return libpgcd.pgcd(int(self.num), int(self.den))

    ############################################################################
    ###############################    AUTRE    ################################
    ############################################################################

    
    def simplifier(self):
        """
        Simplifie le nombre rationnel
        """
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
        somme = RationnelMod(0)
        for rationnel in tabRationnels:
            somme += rationnel

        nbElements = len(tabRationnels)
        moyenne = somme / RationnelMod(nbElements)

        return moyenne

############################################################################
###############################    TESTS    ################################
############################################################################

#Les tests sont enfermés dans des parentheses ou des appels à str() car dû à la
#comparaioson, python les convertirait en strings ou en booléens et causerait des erreurs

# éxecuter les tests seulement si le fichier est executé en tant que fichier principal
if __name__ == "__main__":

    #test normal 
    rat = RationnelMod(36, 12)
    assert str(rat) == "3/1" 

    # test avec paramètre unique
    rat1 = RationnelMod(5)
    assert str(rat1) == "5/1"

    rat2 = RationnelMod(42, 7)
    assert str(rat * rat2) == "18/1"
    assert str(rat + rat2) == "9/1"
    assert str(rat - rat2) == "-3/1"
    assert str(rat / rat2) == "1/2"
    assert (RationnelMod(1, 2) == RationnelMod(2, 4)) == True
    assert (RationnelMod(4, 3) == RationnelMod(7, 9)) == False
    assert (RationnelMod(6, 2) != RationnelMod(8, 9)) == True
    assert (RationnelMod(3, 4) != RationnelMod(6, 8)) == False
    assert (RationnelMod(8, 2) >= RationnelMod(3, 5)) == True
    assert (RationnelMod(8, 2) >= RationnelMod(9)) == False
    assert (RationnelMod(3, 6) <= RationnelMod(747, 5)) == True
    assert (RationnelMod(63, 4) <= RationnelMod(2, 27)) == False
    assert (RationnelMod(409, 12) > RationnelMod(93, 30)) == True
    assert (RationnelMod(23/7) > RationnelMod(73, 4)) == False
    assert (RationnelMod(63, 42) < RationnelMod(93, 6)) == True
    assert (RationnelMod(34, 2) < RationnelMod(2, 45)) == False

    # test de la méthode moyenne
    rat3 = RationnelMod(1, 2)
    rat4 = RationnelMod(2, 3)
    rat5 = RationnelMod(3, 4)
    moy = RationnelMod.moyenne([rat3, rat4, rat5])
    assert str(moy) == "23/36"

    print("Tests passés")

