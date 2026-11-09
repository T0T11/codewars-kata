def loose_change(cents):
    if cents <= 0:
        return {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}

    cents = int(cents) 

    MONEDAS = {
        'Quarters' : 25, 
        'Dimes' : 10,
        'Nickels' : 5,
        'Pennies' : 1
        }

    resultado = {}

    for moneda, valor in MONEDAS.items():
        change = cents // valor
        cents %= valor
        resultado[moneda] = change
    print(resultado)
    return resultado



if __name__ == '__main__':
    

# ver el caso de prueba 29, 91, -2 y 3.9, el orden esta al reves, pero no importa, el resultado es el mismo
    assert(loose_change(29)) ==  {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
    assert(loose_change(91)) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}
    assert(loose_change(-2)) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert(loose_change(3.9)) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}