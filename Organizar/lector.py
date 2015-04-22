from Item import Item
from Mochila import Mochila
from os import listdir
from os.path import isfile, join

def leerArchivo(entrada):
	archivos = sorted([ f for f in listdir("entrada") if isfile(join("entrada",f)) ])
	nombre = (str(entrada) if entrada >= 0 else archivos[-1])
	f=open("entrada/"+nombre,'r')
	i=0
	nCajas=0
	cajas=[]
	maleta = None
	for line in f:
		if i==0:
			nCajas=int(line)
		elif i==1:
			datos = line.split()
			maleta=Mochila(int(datos[0]),int(datos[1]))
		else :
			datos=line.split()
			nCaja=datos[0]
			vCaja=datos[1]
			pCaja=datos[2]
			cajas.append(Item(int(vCaja),int(pCaja)))
		i+=1
	return [maleta, cajas,nombre]

