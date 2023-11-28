def es_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    else:
        limite = int(numero**0.5) + 1
        for i in range(3, limite, 2):
            if numero % i == 0:
                return False
        return True
numero_a_verificar = 13
if es_primo(numero_a_verificar):
    print(f"{numero_a_verificar} es un número primo.")
else:
    print(f"{numero_a_verificar} no es un número primo.")
