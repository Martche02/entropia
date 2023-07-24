import numpy as np
import scipy
class distribuicao:
    media = 0
    desvioPadrao = 1
    def __init__(self, quantidade, dimensao=3):
            self.pontos = self.rPontos(quantidade, dimensao)
    def addPonto(self, dimensao, *proj):
        self.pontos.append(self.rArr(dimensao) if len(proj) == 0 else proj)
    def norma(self, arr):
        e = 0
        for i in arr:
            e += i**2
        e **= 1/2
        return e
    def distancia_entre_pontos(self, a,b):
        a,b = (a,b) if len(a)>len(b) else (b,a)
        return np.array(a)-np.append(b,np.zeros(len(a)-len(b)))
    def desvio_padrao(self): #n maior que 0
        d = np.std(self.distancias())
        print(d)
        return d
    def distancias(self):
        distancias = []
        for i in range(len(self.pontos)):
            for j in range(len(self.pontos)):
                distancias.append(self.norma(self.distancia_entre_pontos(self.pontos[i],self.pontos[j]))) if i<j else 0
        return distancias
    def rArr(self, dimensao=3):
        return np.random.rand(dimensao).tolist()
    def rPontos(self, quantidade=20, dimensao=3):
        pontos = []
        for i in range(quantidade):
            pontos.append(self.rArr(dimensao))
        return pontos
    def areaGauss(self, dist:int, m=media, desvio=desvioPadrao):
        return scipy.stats.norm.cdf(dist, loc=m, scale=desvio)
    def hiperVolume(self,a,b,e):
        Vab = [np.sin(b)*np.cos(a), np.sin(b)*np.sin(a), np.cos(b)] #3 dimensoes
        p = []
        for v in e:
            v = list(v)
            v = np.append(v,np.zeros(3-len(v))).tolist()
            p.append(self.norma(Vab)*self.norma(v)**2/(np.array(v)@np.array(Vab)).tolist())
            if p[-1]<=0:
                p.pop()
        return self.areaGauss(min(p))-1/2 if p != [] else 1/2
    def gaussianas(self): #n maior que 0; volume da 3dgaussiana = 2*pi^2
        hV = 0
        for i in range(len(self.pontos)):
            borda = []
            r = list(self.pontos)
            r.remove(r[i])
            for j in r:
                borda.append(self.distancia_entre_pontos(self.pontos[i],j))
            hV += scipy.integrate.nquad(self.hiperVolume, [[0, np.pi],[0, 2*np.pi]], args=(borda,))[0]
        hV  /= len(self.pontos)*2*np.pi**2
        hV  -= 2*hV-1
        hV **= -1
        print(hV)
        return hV

dist = distribuicao(3)
dist.addPonto(3, 1,1,1)
dist.desvio_padrao()
dist.gaussianas()