from lpsolve55 import *
def resolver(matriz, numMochilas, numObjetos, numProblema, sol):
    posicionOperador = len(matriz[1])-2
    lp = lpsolve('make_lp', 0, posicionOperador)
    lpsolve('set_verbose', lp, IMPORTANT)
    ret = lpsolve('set_obj_fn', lp, matriz[0])
    for i in range(1, len(matriz)):
        if matriz[i][posicionOperador] == "<=":
            ret = lpsolve('add_constraint', lp, matriz[i][:posicionOperador], LE, matriz[i][posicionOperador + 1])
        else:
            ret = lpsolve('add_constraint', lp, matriz[i][:posicionOperador], EQ, matriz[i][posicionOperador + 1])
    for i in range(1, posicionOperador + 1):
        lpsolve('set_binary', lp, i, True)
    ret = lpsolve('write_lp', lp, 'LP/' + numProblema)
    lpsolve('solve', lp)
    numeroMochilas = lpsolve('get_objective', lp)
    print("Objetivo: ", )
    variables = lpsolve('get_variables', lp)[0]
    print("Varibles: ", variables)
    for i in range(numMochilas * numObjetos):
        if variables[i] != 0:
            print("El objeto ", i % numObjetos, " ira en la maleta ", int(i / numObjetos))
    #guardarSalida(variables, numMochilas, numObjetos, numProblema)
    sol.procesarPrimeraSolucion(variables,numMochilas, numObjetos, numProblema, 0,numeroMochilas)
    return sol

def resolverParte2(matriz, numMochilas, numObjetos, numProblema, varAbs,sol):
    posicionOperador = len(matriz[1])-2
    lp = lpsolve('make_lp', 0, posicionOperador)
    lpsolve('set_verbose', lp, IMPORTANT)
    ret = lpsolve('set_obj_fn', lp, matriz[0])
    for i in range(1, len(matriz)):
        if matriz[i][posicionOperador] == "<=":
            ret = lpsolve('add_constraint', lp, matriz[i][:posicionOperador], LE, matriz[i][posicionOperador + 1])
        else:
            ret = lpsolve('add_constraint', lp, matriz[i][:posicionOperador], EQ, matriz[i][posicionOperador + 1])
    for i in range(1, posicionOperador -varAbs+1):
        lpsolve('set_binary', lp, i, True)
    for i in range(posicionOperador-varAbs, posicionOperador + 1):
        lpsolve('set_int', lp, i, True)
    ret = lpsolve('write_lp', lp, 'lp/' + numProblema)
    lpsolve('solve', lp)
    print("VarABS: ", varAbs)
    solucion = lpsolve('get_objective', lp)
    print("Objetivo: ", solucion)
    variables = lpsolve('get_variables', lp)[0]
    print("Varibles: ", variables)
    for i in range(numMochilas * numObjetos):
        if variables[i] != 0:
            print("El objeto ", i % numObjetos, " ira en la maleta ", int(i / numObjetos))
    #guardarSalida(variables, numMochilas, numObjetos, numProblema)
    sol.procesarSegundaSolucion(variables,numMochilas, numObjetos, numProblema, varAbs)
    return sol
