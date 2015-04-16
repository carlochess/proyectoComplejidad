f = open('archivo.in', 'r')
i =0
nCajas = 0
maleta = Maleta()
cajas = []
for line in f:
    if i == 0:
		nCajas = int(line)
    elif i == 1:
		maleta = Maleta(int(line.split(" ")[0],int(line.split(" ")[1])
    else:
		nCaja, vCaja, pCaja = line.split(" ")
		cajas.append(int(nCaja),int(vCaja),int(pCaja))
