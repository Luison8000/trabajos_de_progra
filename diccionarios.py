import sys
import time

# Función para imprimir con animación
def imprimir_animado(texto, retraso=0.05):
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(retraso)
    print()

# Diccionario inicial
futbolistas = {
    1: "Casillas", 
    15: "Ramos",
    3: "Pique", 
    5: "Puyol",
    11: "Capdevila", 
    14: "Xabi Alonso",
    16: "Busquets", 
    8: "Xavi Hernandez",
    18: "Pedrito", 
    6: "Iniesta",
    7: "Villa"
}

imprimir_animado("\nRecorrer un diccionario, imprimiendo su llave-valor")
for k, v in futbolistas.items():
    imprimir_animado(f"{k} {v}")

imprimir_animado("\nVemos cuántos elementos tiene nuestro diccionario")
numElem = len(futbolistas)
imprimir_animado(f"Número de elementos del diccionario: {numElem}")

imprimir_animado("\nImprimir una lista con las claves del diccionario")
llaves = futbolistas.keys()
imprimir_animado(f"Llaves del diccionario: {list(llaves)}")

imprimir_animado("\nImprimir una lista con los valores del diccionario")
valores = futbolistas.values()
imprimir_animado(f"Valores del diccionario: {list(valores)}")

imprimir_animado("\nObtener un valor a partir de su clave")
num = int(input("Dame el numero del futbolista: "))
elem = futbolistas.get(num)
imprimir_animado(f"El futbolista con número {num} es: {elem}")

# añadir un nuevo elemento al diccionario
imprimir_animado("\nAñadir un nuevo elemento al diccionario")
nombre = input("Dame el nombre del futbolista: ")
futbolistas[22] = nombre
imprimir_animado(f"Diccionario actualizado: {futbolistas}")

imprimir_animado("\nEliminar un elemento del diccionario dada su clave")
futbolistas.pop(22)
imprimir_animado(f"Diccionario actualizado: {futbolistas}")

imprimir_animado("\nHacemos una copia del diccionario")
futbolistas_copia = futbolistas.copy()
imprimir_animado(f"Copia del diccionario: {futbolistas_copia}")

imprimir_animado("\nLimpiamos el diccionario original")
futbolistas.clear()
imprimir_animado(f"Diccionario original: {futbolistas}")


