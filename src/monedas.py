

def cambioMonedas(centimos):
    monedas = [0, 0, 0]
    monedas[0] = centimos // 5 
    monedas[1] = (centimos % 5) // 2  
    monedas[2] = (centimos % 5) % 2  
    return tuple(monedas)  



print(cambioMonedas(8))
#>>> (1, 1, 1)  # una de 5 cénts, una de 2 cénts y una de 1 cént.
print(cambioMonedas(5))
#>>> (1, 0, 0)  # una 5 cénts, ninguna de 2 cénts y ninguna de 1 cént.
print(cambioMonedas(29))
#>>> (5, 2, 0)  # cinco de 5 cénts, dos de 2 cénts y ninguna de 1 cént.
print(cambioMonedas(0))
#>>> (0, 0, 0) # ninguna de 5 cénts, ninguna de 2 cénts y 1 de cénts.