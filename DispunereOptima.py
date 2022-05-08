from mailbox import mbox
from urllib import robotparser
from numpy import *
from math import * 
import sys

if (len(sys.argv) < 3): 
    print("Exemplu de utilizare: python3 DispunereOptima.py <masaDrona> <masaTotalaBaterii>")
    exit()

md = (double)(sys.argv[1])
mb = (double)(sys.argv[2])

x1 = md + mb
x2 = 0
x3 = md

masaBaterie1 = 0
masaBaterie2 = 0

coeff = [2, 0, 0, sqrt(pow(x1, 3)), -3*x3*sqrt(pow(x1, 3)), 0]

#print (roots(coeff))

for root in roots(coeff):
    if isreal(root) and root > 0:
        x2 = real(root)

masaBaterie2 = x2 - md
masaBaterie1 = mb - masaBaterie2

print("Masa baterie 1:", masaBaterie1, "\nMasa baterie 2:", masaBaterie2)


# coeff = [160/(243 * pow(a, 15/2)), 0, 4/(9*pow(a, 3)), 160 / (243 * pow(a, 6)), 0, 0, 160 / (243 * pow(a, 9/2)), 0, 4 / (9 * pow(a, 3/2)), 80 / (243 * pow(a, 3)), -1 * (2 * d) / (pow(a, 3/2)), 0, 20 / (243 * pow (a, 3/2)), 0, 1/9, 2/243, -1 * d, 0, 0, 0, 0, 0]

# print (roots(coeff))