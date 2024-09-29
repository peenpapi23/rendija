import libnumcplx as lb
#Se realizara una simulacion del experimento, a partir 
# del modelo ya plateado en clase.
# para hacer mas entendible la matriz, se le asignara una letra a cada uno de los numeros diferentes a 0 y 1.
a = 1/(2**(1/2))
b = (-1+1j/(6**(1/2)))
c = (-1-1j/(6**(1/2)))
d = (1-1j/(6**(1/2))) 
M = [
    [0,0,0,0,0,0,0,0],
    [a,0,0,0,0,0,0,0],
    [a,0,0,0,0,0,0,0],
    [0,b,0,1,0,0,0,0],
    [0,c,0,0,1,0,0,0],
    [0,d,b,0,0,1,0,0],
    [0,0,c,0,0,0,1,0],
    [0,0,d,0,0,0,0,1]
    ]

X = [1,0,0,0,0,0,0,0]

#X es el estado 0 del experimento, se hara la multiplicacion entre la matriz M
# y la transpuesta de X con la intencion de encontrar el siguiente estado del experimento.

MX = [1*0, 1*1/(2**(1/2)), 1*1/(2**(1/2)), 1*0, 1*0, 1*0, 1*0, 1*0]

#en dicho estado se evidencia el comportamiento del experimento, puesto que el foton en la mitad
# de los universos pasara por la una de las rendijas y en la otra mitad pasara por la otra rendija.

# Para hallar el siguiente estado del eperimento, se hara la multiplicacion entre M y la transpuesta de MX.
# Con la intencion de facilitar el uso de nuestra libreria y teniendo en cuenta que fue diseñadas para tuplas de numeros complejos,
# se convertiran los numeros ya mencionados en tuplas.
a = (1/(2**(1/2)),0)
b = (-1/(6**(1/2)),(1/(6**(1/2))))
c = (-1/(6**(1/2)),(-1/(6**(1/2))))
d = (1/(6**(1/2)),(-1/(6**(1/2))))

MMX = [ 0 ,
        0 , 
        0 ,
       lb.multiC(a,b),
       lb.multiC(a,c),
       lb.sumaC(lb.multiC(a,d), lb.multiC(a,b)),
       lb.multiC(a,c),
       lb.multiC(a,d),
       ]

# Por ultimo ya teniendo el ultimo estado, debido a que de ahora en adelante es el mismo resultado,
# se hara la impresion del resultado final.(Tener en cuenta que el primer valor de cada tupla es el valor 
# real del numero complejo, mientras que el segundo es el imaginario)

print('| ',MMX[0], ' |')
print('| ',MMX[1], ' |')
print('| ',MMX[2], ' |')
print('| ',MMX[3], ' |')
print('| ',MMX[4], ' |')
print('| ',MMX[5], ' |')
print('| ',MMX[6], ' |')
print('| ',MMX[7], ' |')
