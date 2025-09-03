#un estudiante puede aprobar una materia si en su examen obtien calficacion de 70 minimo y realiza todas sus actividades
#lee la calificacion (entero) de un estudiante y (s/n) si realizó todas sus actividades.
#de salida muestra "Si" si aprueba y "No" si no aprueba

calificacion = int(input("Ingrese la calificación del estudiante: "))
actividades = input("¿el estudiante hizo todas sus actividades? (s/n): ").strip().lower()
if calificacion >= 70 and actividades == 's':
    print("Si")
else:
    print("No")
    


