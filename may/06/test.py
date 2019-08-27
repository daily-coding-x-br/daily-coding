from leo import sol
import numpy as np
import matplotlib.pyplot as plt
from time import time
N=5000
y=[]
x=np.arange(1,N+1)
for t in x:
    print(t)
    aux=np.random.randint(0,int(3/2*t),t)
    start=time()
    _=sol(aux)
    y.append(time()-start)
plt.plot(x,y)
    
