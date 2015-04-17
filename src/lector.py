from Item import Item
from Mochila import Mochila


def leerArchivo():
	f=open('archivo.in','r')
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
	return [maleta, cajas]

