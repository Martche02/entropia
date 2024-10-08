import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.integrate import nquad
from numba import jit

@jit(nopython=True)
def dis(p, q):
    return 1/(np.linalg.norm(p-q))
    return np.exp(-0.5*np.sum((p - q)**2))*(2*np.pi)**(-0.5)

@jit(nopython=True)
def calculate_density(points, pontos):
    d = np.zeros(points.shape[0])
    for idx, point in enumerate(points):
        for i in pontos:
            d[idx] += dis(point, i)
    return d #/(len(pontos)*(2*np.pi)**(-0.5))

class distribuicao:
    media = 0
    desvioPadrao = 1
    def __init__(self, quantidade=0, dimensao=3):
        self.pontos = self.rPontos(quantidade, dimensao)

    def addPonto(self, dimensao, *proj):
        self.pontos.append(self.rArr(dimensao) if len(proj) == 0 else proj)

    def norma(self, arr):
        return np.linalg.norm(arr)

    def distancia_entre_pontos(self, a, b):
        a, b = (a, b) if len(a)>len(b) else (b, a)
        return np.array(a)-np.append(b,np.zeros(len(a)-len(b)))

    def desvio_padrao(self): 
        return np.std(self.distancias())

    def distancias(self):
        distancias = []
        for i in range(len(self.pontos)):
            for j in range(len(self.pontos)):
                if i < j:
                    distancias.append(self.norma(self.distancia_entre_pontos(self.pontos[i],self.pontos[j])))
        return distancias

    def rArr(self, dimensao=3):
        return np.random.rand(dimensao).tolist()

    def rPontos(self, quantidade, dimensao=3):
        pontos = []
        for i in range(quantidade):
            pontos.append(self.rArr(dimensao))
        return pontos
    
    def area(self, dist):
        return -1/dist
        return norm.cdf(dist, loc=media, scale=desvioPadrao)

    def hiperVolume(self, a, b, e):
        Vab = np.array([np.sin(b)*np.cos(a), np.sin(b)*np.sin(a), np.cos(b)])
        v = np.array([np.append(ve, np.zeros(3-len(ve))) for ve in e])
        p = self.norma(Vab) * self.norma(v, axis=1)**2 / (v @ Vab)
        p = p[p > 0]
        return self.area(min(p))-1/2 if len(p) > 0 else 1/2
    
    def hyperVolumeBehind(A,B,C):
        return nquad(lambda a,b: 1/np.linalg.norm(a*A+b*B+(1-a-b)*C), [lambda b: [0,1-b], lambda: [0, 1]])

    def gaussianas(self): 
        n_points = len(self.pontos)
        hV = 0
        for i in range(n_points):
            r = self.pontos[:i] + self.pontos[i+1:]
            borda = [self.distancia_entre_pontos(self.pontos[i],j) for j in r]
            hV += nquad(self.hiperVolume, [[0, np.pi],[0, 2*np.pi]], args=(borda,))[0]
        hV /= n_points*2*np.pi**2
        hV -= 2*hV-1
        hV **= -1
        print(hV)
        return hV

    def plot(self, n=10, t=1):
        X = np.linspace(-1.5, 1.5, n)
        Y = np.linspace(-1.5, 1.5, n)
        Z = np.linspace(-1.5, 1.5, n)
        X, Y, Z = np.meshgrid(X, Y, Z)
        points = np.column_stack((X.flatten(), Y.flatten(), Z.flatten()))
        dens = calculate_density(points, np.array(self.pontos))
        colors = (dens - dens.min()) / (dens.max() - dens.min())
        colors **= t
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for i in range(points.shape[0]):
            ax.scatter(points[i, 0], points[i, 1], points[i, 2], color=(0.1, 0.2, 0.5, colors[i]))
        ax.set_title('Ambiente de Simulação', fontsize=18)
        ax.set_xlabel('Eixo X', fontsize=15)
        ax.set_ylabel('Eixo Y', fontsize=15)
        ax.set_zlabel('Eixo Z', fontsize=15)
        plt.show()