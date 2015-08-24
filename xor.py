import numpy as np

def sigmoidal(z):
    return 1.0/(1.0 + np.exp(-z))

def sumatorias(x, pesos):
    z = np.dot(x, pesos)
    return sigmoidal(z)

class RedNeuronal:

    def __init__(self, capas):

        self.activacion = sumatorias
        self.pesos = []
        self.resultados = []
        self.solucion_f = []

        l = len(capas)

        for i in range(1, l - 1):
            #valores aleatorios de pesos para
            #la capa de entrada
            #y la capa oculta [2, 2]
            r = np.random.random((capas[i], capas[i]))
            self.pesos.append(r)
        #valores aleatorios para
        #la capa oculta y la salida [2, 1]
        r = np.random.random((capas[l - 2], capas[l-1]))
        self.pesos.append(r)

    def proceso(self, x, y):

        for j in range(x.shape[0]):
            for k in range(0, len(self.pesos[0]) - 1):
                for l in range(len(self.pesos[0])):
                    test = self.activacion(x[j], self.pesos[k][l])
                    test_arr = []
                    test_arr.append(test)
            self.resultados.append(test_arr)
            print 'resultados: ' + str(self.resultados[j])

        self.solucion_f = self.activacion(y, self.resultados)
        print 'Solucion: ' + str(self.solucion_f)

if __name__=='__main__':
    #las capas de la Red Neuronal
    #entrada, capa oculta, salida
    capas = [2,2,1]
    rn = RedNeuronal(capas)
    x = np.array([[0,0],
                  [0,1],
                  [1,0],
                  [1,1]])
    y = np.array([0,1,1,0])
    rn.proceso(x,y)
