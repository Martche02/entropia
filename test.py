import numpy as np
from scipy import integrate
import time

# Define os pontos
A = np.array([0.1, 0.2, 0.6])
B = np.array([0.2, 0.3, 0.4])
C = np.array([0.3, 0.4, 0.5])
def hyperVolumeBehind(A,B,C):
    return integrate.nquad(lambda a,b: 1/np.linalg.norm(a*A+b*B+(1-a-b)*C), [lambda b: [0,1-b], lambda: [0, 1]])
start_time = time.time()
result, error = hyperVolumeBehind(A,B,C)
end_time = time.time()

print("Resultado da integral:", result, error)
print("Tempo de execução:", end_time - start_time)
