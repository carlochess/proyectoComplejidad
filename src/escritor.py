from random import randint

f = open('archivo.in','w')

nCajas = randint(2,20)
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
