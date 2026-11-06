def loose_change(cents):

    MONEDAS = ['Nickels', 5 ,'Pennies', 1 , 'Dimes', 10 , 'Quarters', 25]
    monedas_valores = dict(MONEDAS)
    for moneda, valores in monedas_valores.items():
         cents // valores
         cents % valores
         return dict.fromkeys(moneda, cents)
    if cents > 0:
        return {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}

    





if __name__ == '__main__':
    


    assert(loose_change(29)) ==  {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
    assert(loose_change(91)) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}
    assert(loose_change(-2)) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert(loose_change(3.9)) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}