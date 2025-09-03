#a partir de los numeros que me da el usuario listar y mostrar en una lista si es par o impar 
#dejar de pedir numeros hasta que escriba un -1
def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
def main():
    numeros = []
    while True:
        try:
            numero = int(input("Introduce un número (-1 para terminar): "))
            if numero == -1:
                break
            numeros.append(numero)
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    resultados = [(num, es_par_o_impar(num)) for num in numeros]
    
    print("\nResultados:")
    for num, tipo in resultados:
        print(f"{num} es {tipo}")
main()



 