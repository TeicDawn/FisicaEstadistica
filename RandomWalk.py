import numpy as np
import random

p = 0.5
q = 1 - p
L = 1
N = 100
R = 20

# p és la probabilitat d'anar cap a dalt,
# q és la d'anar cap avall.
# N és el número total de passos.
# L és la longitud dels passos.
# R és el número de walks.

B = np.zeros((R))

######################################################
######################################################

for i in range(R):
  A = np.zeros((N+1))
  y = 0
  m = 0
  s2 = 0

  # Bucle del RW
  for n in range(N):
    if random.uniform(0,1) >= p:
      y += L
    else: y += -L
    A[n+1] = y

  #print(A)

  j = i
  B[j] = A[N-1]
  
#print(B)
