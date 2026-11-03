def first_n_smallest(arr, num):
    lista_smallest = sorted(arr)[:num]
    lista = []
    for num in arr:
        if num in lista_smallest:
            lista.append(num)
            lista_smallest.remove(num) #uso remove para que me vuelva a agregar ej: [1,2,1]
    return lista