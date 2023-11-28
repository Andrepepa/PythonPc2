def omitir_vocales(cadena):
    vocales = "aeiouAEIOU"
    resultado = ''.join(caracter for caracter in cadena if caracter not in vocales)
    return resultado
texto_usuario = input("Ingrese una cadena de texto: ")
resultado_final = omitir_vocales(texto_usuario)
print("Texto con vocales omitidas:", resultado_final)
