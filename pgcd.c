#include <stdlib.h>

int pgcd(int a, int b) {
  if (b == 0) return abs(a); // si b == 0, alors le pgcd est |a|
  return pgcd(b, a % b); //appel récursif
}
