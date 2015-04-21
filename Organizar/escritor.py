from random import randint

from os import listdir
from os.path import isfile, join
archivos = sorted([ f for f in listdir("entrada") if isfile(join("entrada",f)) ])
nombre = int(archivos[-1])+1

f = open("entrada/"+str(nombre),'w')

nCajas = randint(2,6)
f.write(str(nCajas)+"\n")
vMaleta = randint(2,200)
pMaleta = randint(2,200)
f.write(str(vMaleta)+" "+str(pMaleta)+"\n")
for i in range(nCajas):
	nCaja = i
	vCaja = randint(1,vMaleta)
	pCaja = randint(1,pMaleta)
	f.write(str(nCaja)+" "+str(vCaja)+" "+str(pCaja)+"\n")
f.close()
