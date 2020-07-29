import numpy as np
import pandas as pd

#CÓDIGO 1
Z=np.zeros((4,))
print('Z1:',Z)

#CÓDIGO 2
Z=np.zeros((4,))
Z[1]=1.
print('Z2:',Z)

#CÓDIGO 3
Z=np.zeros((4,))
Z[1:]=1.
print('Z3:',Z)

#CÓDIGO 4
Z= np.ones((4,))
Z[-1]=0.
print('Z4:',Z)

Z= np.zeros((4,))
Z[:3]=1.
print('Z5:',Z)

#CÓDIGO 5
X=2*np.ones((2,2))
print(X)

#CÓDIGO 6
X=np.array([[1,2],[3,4]])
Y=X[0,:]
Y[1]=10
print(X)

#CÓDIGO 7
X=np.array([[1,3],[11,10]])
print(np.mean(X[X>np.pi]))