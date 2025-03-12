import random

lstNumeros = [random.randint(1, 100) for _ in range(10)]

maior_numero = max(lstNumeros)

print("Lista de números:", lstNumeros)
print("Maior número:", maior_numero)