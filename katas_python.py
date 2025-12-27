"""
Archivo que contiene la resolución progresiva de las katas de Python del Proyecto 3.
Cada ejercicio está implementado como una función independiente y acompañado de
comentarios explicativos para demostrar la comprensión del código en NOTAS.md

Ejecución:
Este archivo puede ejecutarse directamente para probar algunas katas desde el bloque
if __name__ == "__main__"  en la parte final de esta hoja.
"""




#-----------------------------------------------------------
# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario
# con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencias_letras(texto: str) -> dict:
    frecuencias = {}

    for ch in texto:
        if ch == " ":
            continue

        frecuencias[ch] = frecuencias.get(ch, 0) + 1

    return frecuencias


#-----------------------------------------------------------
# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor.
# Usa la función map().

def doble_lista(valores: list) -> list:
    return list(map(lambda x: x * 2, valores))


#-----------------------------------------------------------
# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros.
# La función debe devolver una lista con todas las palabras de la lista original
# que contengan la palabra objetivo.

def palabras_que_contienen(palabras: list, objetivo: str) -> list:
    return [p for p in palabras if objetivo in p]


#-----------------------------------------------------------
# 4. Genera una función que calcule la diferencia entre los valores de dos listas.
# Usa la función map().

def diferencia_listas(lista1: list, lista2: list) -> list:
    return list(map(lambda par: par[0] - par[1], zip(lista1, lista2)))


#-----------------------------------------------------------
# 5. Escribe una función que tome una lista de números y un valor opcional nota_aprobado (por defecto 5).
# La función devuelve una tupla con la media y el estado ("aprobado" o "suspenso").

def media_y_estado(notas: list, nota_aprobado: float = 5) -> tuple:
    media = sum(notas) / len(notas)

    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"

    return media, estado


#-----------------------------------------------------------
# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


#-----------------------------------------------------------
# 7. Genera una función que convierta una lista de tuplas a una lista de strings.
# Usa la función map().

def tuplas_a_strings(tuplas: list) -> list:
    return list(map(str, tuplas))


#-----------------------------------------------------------
# 8. Escribe un programa que pida al usuario dos números e intente dividirlos.
# Maneja errores si no son números o si se intenta dividir por cero.

def dividir_numeros():
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        resultado = num1 / num2
    except ValueError:
        print("Error: debes introducir números válidos.")
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")
    else:
        print(f"La división se ha realizado correctamente. Resultado: {resultado}")


#-----------------------------------------------------------
# 9. Escribe una función que devuelva una lista de mascotas permitidas en España,
# excluyendo las mascotas prohibidas usando filter().

def filtrar_mascotas(mascotas: list) -> list:
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda m: m not in prohibidas, mascotas))


#-----------------------------------------------------------
# 10. Escribe una función que calcule el promedio de una lista de números.
# Si la lista está vacía, lanza una excepción personalizada.

class ListaVaciaError(Exception):
    pass


def calcular_promedio(numeros: list) -> float:
    if len(numeros) == 0:
        raise ListaVaciaError("No se puede calcular el promedio de una lista vacía")

    return sum(numeros) / len(numeros)


#-----------------------------------------------------------
# 11. Escribe un programa que pida al usuario introducir su edad y valide el dato.

def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))

        if edad < 0 or edad > 120:
            raise ValueError("La edad está fuera del rango válido")

    except ValueError:
        print("Error: introduce una edad válida entre 0 y 120.")
    else:
        print(f"Edad aceptada: {edad}")


#-----------------------------------------------------------
# 12. Genera una función que, al recibir una frase,
# devuelva una lista con la longitud de cada palabra usando map().

def longitudes_palabras(frase: str) -> list:
    palabras = frase.split()
    return list(map(len, palabras))


#-----------------------------------------------------------
# 13. Devuelve una lista de tuplas (MAYUS, minus) sin letras repetidas usando map().

def mayus_minus_sin_repetir(caracteres: str) -> list:
    letras_unicas = sorted(set(caracteres))
    return list(map(lambda c: (c.upper(), c.lower()), letras_unicas))


#-----------------------------------------------------------
# 14. Retorna palabras que empiezan por una letra usando filter().

def palabras_empiezan_por(palabras: list, letra: str) -> list:
    return list(filter(lambda p: p.startswith(letra), palabras))


#-----------------------------------------------------------
# 15. Lambda que suma 3 a cada número de una lista.

sumar_3 = lambda lista: list(map(lambda x: x + 3, lista))


#-----------------------------------------------------------
# 16. Devuelve palabras más largas que n usando filter().

def palabras_mas_largas_que(texto: str, n: int) -> list:
    return list(filter(lambda w: len(w) > n, texto.split()))


#-----------------------------------------------------------
# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente.
# Usa la función reduce().

from functools import reduce

def digitos_a_numero(digitos: list) -> int:
    return reduce(lambda acc, d: acc * 10 + d, digitos)


#-----------------------------------------------------------
# 18. Crea una lista de diccionarios con información de estudiantes y filtra
# los que tengan una calificación mayor o igual a 90 usando filter().

def estudiantes_destacados(estudiantes: list) -> list:
    return list(filter(lambda e: e["calificacion"] >= 90, estudiantes))


#-----------------------------------------------------------
# 19. Crea una función lambda que filtre los números impares de una lista dada.

filtrar_impares = lambda numeros: list(filter(lambda x: x % 2 != 0, numeros))


#-----------------------------------------------------------
# 20. Para una lista con elementos integer y string, devuelve solo los valores int.
# Usa la función filter().

def solo_enteros(valores: list) -> list:
    return list(filter(lambda x: isinstance(x, int), valores))


#-----------------------------------------------------------
# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda.

cubo = lambda x: x ** 3


#-----------------------------------------------------------
# 22. Dada una lista numérica, obtén el producto total de los valores.
# Usa la función reduce().

def producto_total(numeros: list) -> int:
    return reduce(lambda acc, x: acc * x, numeros)


#-----------------------------------------------------------
# 23. Concatena una lista de palabras.
# Usa la función reduce().

def concatenar_palabras(palabras: list) -> str:
    return reduce(lambda acc, p: acc + p, palabras)


#-----------------------------------------------------------
# 24. Calcula la diferencia total en los valores de una lista.
# Usa la función reduce().

def diferencia_total(numeros: list) -> int:
    return reduce(lambda acc, x: acc - x, numeros)


#-----------------------------------------------------------

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(texto: str) -> int:
    return len(texto)


#-----------------------------------------------------------

# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

resto_division = lambda a, b: a % b


#-----------------------------------------------------------

# 27. Crea una función que calcule el promedio de una lista de números.

def promedio_lista(numeros: list) -> float:
    return sum(numeros) / len(numeros)


#-----------------------------------------------------------

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista: list):
    vistos = set()

    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)

    return None


#-----------------------------------------------------------

# 29. Crea una función que convierta una variable en una cadena de texto y enmascare
# todos los caracteres con el carácter '#' excepto los últimos cuatro.

def enmascarar_ultimos_4(valor) -> str:
    texto = str(valor)

    if len(texto) <= 4:
        return texto

    return "#" * (len(texto) - 4) + texto[-4:]


#-----------------------------------------------------------

# 30. Crea una función que determine si dos palabras son anagramas,
# es decir, si están formadas por las mismas letras pero en diferente orden.

def son_anagramas(palabra1: str, palabra2: str) -> bool:
    p1 = palabra1.replace(" ", "").lower()
    p2 = palabra2.replace(" ", "").lower()

    return sorted(p1) == sorted(p2)





























#===========================================================
# MAIN – Pruebas de las katas
#===========================================================

if __name__ == "__main__":

    # Kata 1
    print("Kata 1:", frecuencias_letras("hola hola"))

    # Kata 2
    print("Kata 2:", doble_lista([1, 2, 3, 4]))

    # Kata 3
    print("Kata 3:", palabras_que_contienen(
        ["casa", "caseta", "perro", "gato", "casual"],
        "casa"
    ))

    # Kata 4
    print("Kata 4:", diferencia_listas([10, 20, 30], [1, 5, 10]))

    # Kata 5
    print("Kata 5:", media_y_estado([6, 7, 5, 8]))

    # Kata 6
    print("Kata 6:", factorial(5))

    # Kata 7
    print("Kata 7:", tuplas_a_strings([(1, 2), ("a", "b"), (3, 4, 5)]))

    # Kata 8 
    print("Kata 8:")
    dividir_numeros()

    # Kata 9
    print("Kata 9:", filtrar_mascotas(["Perro", "Gato", "Mapache", "Loro", "Oso"]))

    # Kata 10
    print("Kata 10:")
    try:
        print(calcular_promedio([5, 7, 9]))
        print(calcular_promedio([]))
    except ListaVaciaError as e:
        print(f"Error controlado: {e}")
    
    # Kata 11
    print("Kata 11:")
    pedir_edad()

    # Kata 12
    print("Kata 12:", longitudes_palabras("hola mundo desde python"))

    # Kata 13
    print("Kata 13:", mayus_minus_sin_repetir("aAbBcCa"))

    # Kata 14
    print("Kata 14:", palabras_empiezan_por(["casa", "coche", "perro", "cama"], "c"))

    # Kata 15
    print("Kata 15:", sumar_3([1, 2, 3]))

    # Kata 16
    print("Kata 16:", palabras_mas_largas_que("esto es una frase de ejemplo", 3))

    # Kata 17
    print("Kata 17:", digitos_a_numero([5, 7, 2]))

    # Kata 18
    estudiantes = [
        {"nombre": "Ana", "edad": 20, "calificacion": 95},
        {"nombre": "Luis", "edad": 22, "calificacion": 88},
        {"nombre": "Marta", "edad": 21, "calificacion": 92}
    ]
    print("Kata 18:", estudiantes_destacados(estudiantes))

    # Kata 19
    print("Kata 19:", filtrar_impares([1, 2, 3, 4, 5, 6]))

    # Kata 20
    print("Kata 20:", solo_enteros([1, "a", 3, "hola", 5]))

    # Kata 21
    print("Kata 21:", cubo(3))

    # Kata 22
    print("Kata 22:", producto_total([2, 3, 4]))

    # Kata 23
    print("Kata 23:", concatenar_palabras(["Hola", " ", "Python"]))

    # Kata 24
    print("Kata 24:", diferencia_total([20, 5, 3]))

        # Kata 25
    print("Kata 25:", contar_caracteres("Hola Python"))

    # Kata 26
    print("Kata 26:", resto_division(10, 3))

    # Kata 27
    print("Kata 27:", promedio_lista([5, 7, 9]))

    # Kata 28
    print("Kata 28:", primer_duplicado([1, 2, 3, 2, 5]))

    # Kata 29
    print("Kata 29:", enmascarar_ultimos_4("123456789"))

    # Kata 30
    print("Kata 30:", son_anagramas("Roma", "Amor"))















