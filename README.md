# Projet-Rationnels

## Classe `Rationnel`

### Description

La classe `Rationnel` permet de représenter et faire des opérations sur des nombres rationnels sous la forme numérateur/dénominateur. 

#### Fonctionnalités

- support des opérations de base (addition, soustraction, multiplication, division)

- support des opérateurs de comparaison

- simplification des rationnels (automatique) et calcul de moyenne

- peut être importé et utilisé comme un module

### Utilisation

#### Création d'objets

> rationnel = Rationnel(numérateur, dénominateur)
```py
# e.g
rat = Rationnel(36/12)
print(rat) # Affiche '3/1'
```

#### Opérations

> rationnel1 (__+__, __-__, __*__, __/__) rationnel2

```py
# e.g
rat1 = Rationnel(1, 2)
rat2 = Rationnel(2, 3)

print(rat1 + rat2) # Affiche "7/6"
print(rat1 * rat2) # Affiche "1/3"
```

#### Comparaisons

> rationnel1 (__==__, __!=__, __>=__, __<=__, __>__, __<__) rationnel2

```py
# e.g
print(rat1 == Rationnel(2, 4)) # Affiche True
print(rat1 > rat2) # Affiche False
```

#### Moyenne

> moyenne = Rationnel.moyenne([rationnel1, rationnel2, rationnel3])

```py
moyenne = Rationnel.moyenne([rat1, rat2])
print(moyenne) # Affiche "7/12"
``` 
#### Import

> import nom_fichier_classe.py

```py
# e.g
from rationnels import Rationnel
rat1 = Rationnel(3, 4)
rat2 = Rationnel(7, 3)
print(rat1 == rat2) # Affiche False
print(rat1 + rat2) # Affiche "37/12"
```
