def factorial(numero):
    if numero < 0:
        return "El factorial no está definido para números negativos."
    elif numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado
numero_a_calcular_factorial = 5
resultado_factorial = factorial(numero_a_calcular_factorial)
print(f"El factorial de {numero_a_calcular_factorial} es: {resultado_factorial}")