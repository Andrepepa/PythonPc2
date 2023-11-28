alumnos = []
n = int(input("Ingrese la cantidad de alumnos: "))
for i in range(n):
    alumno = {}
    nombre = input("Ingrese el nombre del alumno: ")
    alumno["Alumno"] = nombre
    calificaciones = []
    for j in range(3):
        calificacion = float(input(f"Ingrese la calificación {j+1} del alumno: "))
        calificaciones.append(calificacion)
    alumno["Notas"] = calificaciones
    alumnos.append(alumno)
for alumno in alumnos:
    print(alumno)
