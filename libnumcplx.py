#libreria, operaciones de numeros complejos
import math
def sumaC(a,b):
    real = (a[0]+b[0])
    imag = (a[1]+b[1])
    return (real, imag)

def multiC(a,b):
    real = (a[0]*b[0]) - (a[1]*b[1])
    imag = (a[0]*b[1]) + (a[1]*b[0])
    return (real, imag)

def restaC(a,b):
    real = (a[0]-b[0])
    imag = (a[1]-b[1])
    return (real, imag)

def divisionC(a,b):
    real = ((a[0]*b[0])+(a[1]*b[1]))/((b[0]**2)+(b[1]**2))
    imag = ((b[0]*a[1])-(a[0]*b[1]))/((b[0]**2)+(b[1]**2))
    return (real, imag)

def moduloC(a):
    return ((a[0]**2)+(a[1]**2))**(1/2)

def conjugadoC(a):
    imag = -1*(a[1])
    return (a[0], imag)

def faseC(a):
    fase = math.atan2(a[0],a[1])
    return fase

def converC_P(a):
    modulo = moduloC(a)
    fase = faseC(a)
    return (modulo, fase)

def converP_C(a):
    real = a[0]*math.cos(a[1])
    imag = a[0]*math.sin(a[1])
    return (real, imag)

print(converP_C((2.8, 0.5)))