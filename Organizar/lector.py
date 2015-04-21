from Item import Item
from Mochila import Mochila
from os import listdir
from os.path import isfile, join

def leerArchivo():
	archivos = sorted([ f for f in listdir("entrada") if isfile(join("entrada",f)) ])
	nombre = int(archivos[-1])
	f=open("entrada/"+str(nombre),'r')
	i=0
	nCajas=0
	cajas=[]
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
	return [maleta, cajas,str(nombre)]

