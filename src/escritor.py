from random import randint

f = open('archivo.in','w')

nCajas = 0
f.write(nCajas)
vMaleta = randint(2,200)
pMaleta = randint(2,200)
f.write(vMaleta+" "+pMaleta)
for i in range(nCajas):
	nCaja = i
	vCaja = randint(1,vMaleta))
	pCaja = randint(1,pMaleta))
	f.write(nCaja+" "+vCaja+" "+pCaja)
f.close()
