
"""

Archivo que contiene la resolución progresiva de las katas de Python del Proyecto 3.
Cada ejercicio está implementado como una función independiente y acompañado de
comentarios explicativos para demostrar la comprensión del código.

Ejecución:
Este archivo puede ejecutarse directamente para probar algunas katas desde el bloque
if __name__ == "__main__".

"""



# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario
# con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.


def frecuencias_letras(texto: str) -> dict:
    frecuencias = {}

    for ch in texto:
        if ch == " ":
            continue

        frecuencias[ch] = frecuencias.get(ch, 0) + 1

    return frecuencias





#---------------------------------------------------------------------

# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor.
# Usa la función map().

def doble_lista(valores: list) -> list:
    return list(map(lambda x: x * 2, valores))



#------------------------------------------------------------------

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros.
# La función debe devolver una lista con todas las palabras de la lista original
# que contengan la palabra objetivo.

def palabras_que_contienen(palabras: list, objetivo: str) -> list:
    return [p for p in palabras if objetivo in p]




#-------------------------------------------------------------------


# 4 Genera una función que calcule la diferencia entre los valores de dos listas.
# Usa la función map().

def diferencia_listas(lista1: list, lista2: list) -> list:
    return list(map(lambda par: par[0] - par[1], zip(lista1, lista2)))

























#--------------[__main__]-----------------

if __name__ == "__main__":
    print(frecuencias_letras("hola hola"))
    print(doble_lista([1, 2, 3, 4]))
    print(palabras_que_contienen(
        ["casa", "caseta", "perro", "gato", "casual"],
        "casa"
    ))
    print(diferencia_listas([10, 20, 30], [1, 5, 10]))




