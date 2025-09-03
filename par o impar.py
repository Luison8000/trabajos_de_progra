def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

def main():
    numeros = []
    numero = 0  

    while numero != -1:
        numero = int(input("Introduce números hasta que sea -1: "))
        if numero != -1:
            numeros.append(numero)
    
    resultados = [(num, es_par_o_impar(num)) for num in numeros]
    
    for num, tipo in resultados:
        print(f"{num} es {tipo}")

main()



 
