numeros = []  
contador_pares = 0
contador_impares = 0

while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").upper()

    if respuesta == "SI":
        try:
            numero = int(input("Ingrese el número: "))
            numeros.append(numero)
            if numero % 2 == 0:
                contador_pares += 1
            else:
                contador_impares += 1
        except ValueError:
            print("Por favor, ingrese un número válido.")
    elif respuesta == "NO":
        break
    else:
        print("Respuesta no válida. Por favor, ingrese SI o NO.")

print("Números ingresados:", numeros)
print("Cantidad de números pares:", contador_pares)
print("Cantidad de números impares:", contador_impares)