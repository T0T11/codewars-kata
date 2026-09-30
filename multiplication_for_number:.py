def multiTable(multiplicando):
    rango_multiplicador = range(1, 11)
    return "\n".join(f"{i} * {multiplicando} = {i * multiplicando}" for i in rango_multiplicador) 
# el join une con el salto de linea cada elemento de la lista generada por la comprensión de listas.


multiTable(5)