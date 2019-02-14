import numpy as np

def mostrar(params):
            print(params)

def xVertice(b,a):
    sol = (-1*b)/(2*a)
    return float(round(sol,2))
    
def yVertice(b,a,c):
    sol = (-1*(b**2) + (4*a*c)) / (4*a)
    return float(round(sol,2))

def opDisc(a,b,c):
    num = ((b**2) - (4*a*c))
    return num

def discriminante_real(opDisc):
    disc = round(np.sqrt(opDisc),2)
    return disc

def discriminante_complejo(opDisc):
    comp = np.absolute(opDisc)
    disc = round(np.sqrt(comp),2)
    return disc

def sol_x1(b,a,data):
    if(data < 0):
        disc = discriminante_complejo(data)
        sol=((-1*b)+disc)/(2*a)
        return str(round(sol,2))+"i"
    elif(data > 0):
        disc = discriminante_real(data)
        sol = ((-1*b)+disc)/(2*a)
        return str(round(sol,2))
    elif(data == 0):
        sol = (-1*b)/(2*a)
        return str(round(sol,2))

def sol_x2(b,a,data):
    if(data < 0):
        disc = discriminante_complejo(data)
        sol=((-1*b)-disc)/(2*a)
        return str(round(sol,2))+"i"
    
    elif(data == 0):
        return 0

    else:
        disc = discriminante_real(data)
        sol = ((-1*b)-disc)/(2*a)
        return str(round(sol,2))