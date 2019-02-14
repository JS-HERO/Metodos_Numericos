import numpy as np
import matplotlib.pylab as plt

def graficar(a,b,c):
    x1 = np.linspace(-1, 1, 20)
    y1 = a*(x1)**2 + b*(x1) + c
    plt.figure(num='Grafica Ecuacion', figsize=(5,5))
    plt.plot(x1, y1,marker="o", color='r')
    plt.xlabel('Abcisas')
    plt.ylabel('Ordenadas')
    plt.title('Ecuacion Diferencial')
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()


