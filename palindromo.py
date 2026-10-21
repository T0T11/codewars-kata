#!/usr/bin/env python3


def permute_a_palindrome(input):
    conteo_letras = {}
    for letra in input:
        conteo_letras[letra] = conteo_letras.get(letra, 0) + 1 

    impar_total = sum(1 for valor in conteo_letras.values() if valor % 2 != 0) # suma 1 si el valor es impar
    return impar_total <= 1