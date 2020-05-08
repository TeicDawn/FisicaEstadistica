import numpy as np
import matplotlib.pyplot as plt  
from matplotlib import colors
import random as r

N = 20          # Nombre de dipols per costat del quadrat.
R = 200000      # Nombre d'iteracions.

D = np.zeros((N,N))
T = 0.1         # Temperatura adimensionalitzada.
M = 0           # Magnetització del sistema.
H = 0           # Energia del sistema.

file = open("DADES.txt", "w")   # Document on s'hi guarden les M i H.


# DIPOLS A t = 0

for j in range(0, N):
    for i in range(0, N):
        D[j][i] = r.randint(0,1)
        if D[j][i] == 0:
            D[j][i] = -1
        
        M += D[j][i]

# ENERGIA A t = 0

def dE(i, j):
    xs = (i+1)%N
    xi = (i-1)%N
    ys = (j+1)%N
    yi = (j-1)%N
    return -2*D[j][i]*(D[ys][i]+D[yi][i]+D[j][xs]+D[j][xi])

# HEM DEFINIT AQUESTS x/y SUPERIOR (s) I INFERIOR (i) PER A PODER
# APLICAR LES CONDICIONS DE CONTORN PERIÒDIQUES AMB ELS MOD (%)

for j in range(0, N):
    for i in range(0, N):
        H += dE(i, j)

H *= 1/4

file.write(str(H) + ' ' + str(M/400) + '\n')

# ELS dE SÓN PER A CALCULAR LES PROBABILITATS, PERÒ TAMBÉ SERVEIXEN PER A FER
# EL CÀLCUL DE L'ENERGIA INICIAL.


# EVOLUCIÓ TEMPORAL

def P(i, j):
    p = np.exp(dE(i, j)/T)
    return p

for b in range(1,R):
    for t in range(1,150):
        i = r.randint(0,N-1)
        j = r.randint(0,N-1)
        if P(i,j) > r.uniform(0,1):
            M += -D[j][i]
            D[j][i] *= -1
            M += D[j][i]
            H += dE(i, j)
    
    file.write(str(H) + ' ' + str(M/400) + '\n')

# GENERADOR D'IMATGES DEL SISTEMA

cmap = colors.ListedColormap(['black', 'white'])
bounds = np.linspace(start=-1, stop=1, num=2)
plt.imshow(D, cmap = cmap)
plt.xlabel('x (m)', fontsize = 12)
plt.ylabel('y (m)', fontsize = 12)
plt.show()

print("Energy = ", H)
print("Magnetization = ", M/400)

# PER A QUE GUARDI LA IMATGE AUTOMÀTICAMENT
# ES FA SERVIR plt.savefig("<direcció>\\<nom>")
    
file.close()