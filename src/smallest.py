def first_n_smallest(arr, n):
    lista_smallest = sorted(arr)[:n]
    lista = []
    for n in arr:
        if n in lista_smallest:
            lista.append(n)
            lista_smallest.remove(n) #uso remove para que me vuelva a agregar ej: [1,2,1]
    return lista