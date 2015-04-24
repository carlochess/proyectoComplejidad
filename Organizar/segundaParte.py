from __future__ import print_function
from lector import *
from lpSolv import *
import sys
import math

def generarRestriccionesTipo(matriz, tipo):
    numeroRestricciones = (n* (n-1)) / 2
    
    if tipo == 0 or tipo == 1:
		
        for j in range(0, n):
            restriccionCanecaI = []
            
            for k in range(0, i * n):
				
                if k >= i * j and k < i * j + i:
                    objPos = k % i
                    
                    if tipo == 0:
                        restriccionCanecaI.append(items[objPos].getPeso())
                    elif tipo == 1:
                        restriccionCanecaI.append(items[objPos].getVolumen())
					else:
						restriccionCanecaI.append(0)
					#END if
				#END if
			#END for
            if tipo == 0:
				
                for k in range(0, numeroRestricciones):
                    restriccionCanecaI.append(0)
                #END for
                restriccionCanecaI.append("<=")
                restriccionCanecaI.append(caneca.getPeso())
             
            elif tipo == 1:
				
                for k in range(0, numeroRestricciones):
                    restriccionCanecaI.append(0)
                #END for
                restriccionCanecaI.append("<=")
                restriccionCanecaI.append(caneca.getVolumen())
            #END if
            matriz.append(restriccionCanecaI)
		#END for
    elif tipo == 2:
		
        for j in range(0, i):
            restriccionCanecaI = []
            
            for k in range(0, i * n + numeroRestricciones):
				
                if (k % i) -j == 0 and k < i * n:
                    restriccionCanecaI.append(1)
                else:
                    restriccionCanecaI.append(0)
                #END if
            #END for
            restriccionCanecaI.append("=")
            restriccionCanecaI.append(1)
            matriz.append(restriccionCanecaI)
        #END for
    elif tipo == 3:
        r = 0
        
        for u in range(0, n):
			
            for v in range(u + 1, n):
                mult = 1
                
                for numEq in range(0, 2):
                    restriccionCanecaI = []
                    for k in range(0, i * n):
                        if k >= u * i and k < u * i + i:
                            restriccionCanecaI.append(mult * items[k % i].getPeso())
                        elif k >= v * i and k < v * i + i:
                            restriccionCanecaI.append(-mult * items[k % i].getPeso())
                        else:
                            restriccionCanecaI.append(0)
                        #END if
                    #END for
                    for k in range(0, numeroRestricciones):
                        if k == r:
                            restriccionCanecaI.append(-1)
                        else:
                            restriccionCanecaI.append(0)
                        #END if
                    #END for
                    restriccionCanecaI.append("<=")
                    restriccionCanecaI.append(0)
                    matriz.append(restriccionCanecaI)
                    mult = mult * -1
                #END for
            	r += 1
            #END for
        #END for
	#END if
#END generarRestriccionesTipo()

def generarFuncObj(matriz):
    restriccionCanecaI = []
    numeroRestricciones = (n* (n-1)) / 2
    
    for k in range(0, i * n):
        restriccionCanecaI.append(0)
    #END for
    for k in range(0, numeroRestricciones):
        restriccionCanecaI.append(1)
    #END for
    matriz.append(restriccionCanecaI)
#END generarFuncObj()

def generarRestricciones():
    generarRestriccionesTipo(primeraRestriccion, 1)
    generarRestriccionesTipo(segundaRestriccion, 0)
    generarRestriccionesTipo(terceraRestriccion, 2)
    generarRestriccionesTipo(cuartaRestriccion, 3)
#END generarRestricciones()

def generarFuncionObjetivo():
    generarFuncObj(funcObj)
#END generarFuncionesObjetivo()

def printMatrix(testMatrix):
	
    for i in range(len(testMatrix)):
        for j in range(len(testMatrix[i])):
            print(testMatrix[i][j], end=" ")
        #END for
        print(" : ",len(testMatrix[i]))
    #END for
    print()
#END printMatrix()

def hallarN():
    sumaPesos = 0
    sumaVolumenes = 0
    
    for i in range(len(items)):
        sumaPesos += items[i].getPeso()
    #END for
    for i in range(len(items)):
        sumaVolumenes += items[i].getVolumen()
    #END for
    pesos = math.ceil(sumaPesos / float(caneca.getPeso()))
    volumenes = math.ceil(sumaVolumenes / float(caneca.getVolumen()))
    
    if(pesos >= volumenes):
        return pesos
    else:
        return volumenes
	#END if
#END hallarN()

param = (sys.argv[1] if len(sys.argv) > 1 else -1)
o = leerArchivo(param)
caneca = o[0]
items = o[1]
numeroProblema = o[2] + "_2.lp"
n = int(hallarN())
i = len(items)
funcObj = []
primeraRestriccion = []
segundaRestriccion = []
terceraRestriccion = []
cuartaRestriccion = []
matriz = []
numeroRestricciones=(n* (n-1)) / 2
generarRestricciones()
generarFuncionObjetivo()

for e in funcObj:
    matriz.append(e)
#END for
for e in primeraRestriccion:
    matriz.append(e)
#END for
for e in segundaRestriccion:
    matriz.append(e)
#END for
for e in terceraRestriccion:
    matriz.append(e)
#END for
for e in cuartaRestriccion:
    matriz.append(e)
#END for
print("Items ", items)
print("Caneca ", caneca)
printMatrix(matriz)
resolverParte2(matriz,n,i,numeroProblema,numeroRestricciones)

