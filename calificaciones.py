
#programa que nos permita guardar nombres de los alumnos
#y las notas que han obtenido
#cada alumno puede tener varias notas
#pedira el numero de alumnos que queremos guardar

def main():
    alumnos = {}
    num_alumnos = int(input("¿Cuántos alumnos quieres guardar? "))

    for _ in range(num_alumnos):
        nombre = input("Introduce el nombre del alumno: ")
        notas = []
        while True:
            nota = input(f"Introduce una nota para {nombre} (o 'fin' para terminar): ")
            if nota.lower() == 'fin':
                break
            try:
                notas.append(float(nota))
            except ValueError:
                print("Por favor, introduce un número válido o 'fin' para terminar.")
        alumnos[nombre] = notas

    print("\nAlumnos y sus notas:")
    for nombre, notas in alumnos.items():
        print(f"{nombre}: {notas}")

if __name__ == "__main__":
    main()

