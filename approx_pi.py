import os
import ctypes
from src.RationnelMod import RationnelMod 

# on importe la librairie dynamique selon l'OS
if os.name == "nt": #Windows
    libpgcd = ctypes.CDLL("./libs/pgcd.dll")
else: #linux
    libpgcd = ctypes.CDLL("./libs/libpgcd.so")

# déclaration des types d'args et return
libpgcd.pgcd.argtypes = [ctypes.c_int, ctypes.c_int]
libpgcd.pgcd.restype = ctypes.c_int

def approx_pi(n):
    """
    Donne la valeur approximée de pi au bout de n itérations d'après la formule: pi = 4 * ( ((-1)^n) / (2n + 1))

    ARGUMENTS
        n (int): nombre d'itérations sohuaité
    RENVOIE
        RationnelMod: La valeur approximée de pi au bout de n itérations sous forme de rationnel
    """
    somme = RationnelMod(0)
    for i in range(n+1):
        # on additionne chaque terme d'après la formule
        terme = RationnelMod((-1) ** i, 2 * i + 1)
        somme += terme
    return somme * RationnelMod(4)


"""
ATTENTION:

BON A SAVOIR: comme pas de limite de récursion (en théorie) peut potentiellement causer un peu de lag/utiliser toute la RAM. testé sans soucis jusqu'a 20000.
"""
if __name__ == "__main__":
    n = 1000
    approximation_pi = approx_pi(n)
    # N.B. ce print marche pour peu d'itérations (e.g. 1000) mais va causer une erreur car trop de chiffres au bout d'un certain n. Le deuxième print est donc favorable
    print(f"Approximation de pi avec {n} itérations: {approximation_pi}") # sous forme de fraction
    # pour un résultat plus lisible par un humain
    print(f"\r\n\r\n\r\nApproximation de pi avec {n} itérations: {approximation_pi.num / approximation_pi.den}")
