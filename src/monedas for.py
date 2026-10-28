#Define un prodecimiento, euros, que toma como entrada un entero positivo en euros
# y devuelve el número de monedas de 5 céntimos, de 2 cénts. y de 1 cénts. requeridos 
# para formar ese valor. El valor retornado debe ser una lista de tres números:
# el número de monedas de 5 cénts, de 2 cénts. y de 1 cénts. necesarias.
#
# Tu respuesta debe usar el menor número posible usandp primero cuantas más monedas
# de 5 cénts posible, luego de 2 y finalmente de 1 (para sumar el total)

def cambioMonedas(centimos):
    monedas = [0, 0, 0] 
    valores = [5, 2, 1]  # valores de las monedas en céntimos

    for i in valores:
        monedas[valores.index(i)] = centimos // i  # calcula cuántas monedas de ese valor se pueden usar
        centimos %= i  # actualiza el valor restante después de usar esas monedas

    return tuple(monedas)
    

print(cambioMonedas(8))
#>>> (1, 1, 1)  # una de 5 cénts, una de 2 cénts y una de 1 cént.
print(cambioMonedas(5))
#>>> (1, 0, 0)  # una 5 cénts, ninguna de 2 cénts y ninguna de 1 cént.
print(cambioMonedas(29))
#>>> (5, 2, 0)  # cinco de 5 cénts, dos de 2 cénts y ninguna de 1 cént.
print(cambioMonedas(0))
#>>> (0, 0, 0) # ninguna de 5 cénts, ninguna de 2 cénts y 1 de cénts.