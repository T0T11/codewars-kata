import re


def to_camel_case(text):
    if not text:
        return ""
    palabras_separadas = re.split("[-_]", text)
    palabras_no_capitalizadas = palabras_separadas[0]
    palabras_capitalizadas = []
    for p in palabras_separadas[1:]:
        palabras_capitalizadas.append(p[:1].upper() + p[1:])
    final = palabras_no_capitalizadas + "".join(palabras_capitalizadas)
    return final