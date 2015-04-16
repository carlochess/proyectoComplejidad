from lpsolve55 import *
def resolver(matriz):
    posicionOperador = len(matriz[1])-2
    lp = lpsolve('make_lp', 0, posicionOperador)
    lpsolve('set_verbose', lp, IMPORTANT)
    ret = lpsolve('set_obj_fn', lp, matriz[0])
    for i in range(1, len(matriz)):
        if matriz[i][posicionOperador] == "<=" :
            ret = lpsolve('add_constraint', lp,matriz[i][:posicionOperador], LE, matriz[i][posicionOperador+1])
        else:
            ret = lpsolve('add_constraint', lp,matriz[i][:posicionOperador], E, matriz[i][posicionOperador+1])
    ret = lpsolve('write_lp', lp, 'a.lp')
    print lpsolve('get_mat', lp, 1, 2) ## 78.26
    lpsolve('solve', lp)
    print lpsolve('get_objective', lp)
    print lpsolve('get_variables', lp)[0] ## [28.600000000000001, 0.0, 0.0, 31.827586206896552]
    print lpsolve('get_constraints', lp)[0] ## [92.299999999999997, 6.863999999999999, 391.2928275862069]