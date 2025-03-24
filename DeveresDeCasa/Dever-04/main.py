import pandas as pd

with open('minhas_frutas.txt', 'r') as file:
    lines = file.readlines()

frutas_unicas = set()
dados = {}

for line in lines:
    fruta, quantidade = line.strip().split(': ')
    frutas_unicas.add(fruta)
    
    if fruta in dados:
        dados[fruta] += int(quantidade)
    else:
        dados[fruta] = int(quantidade)

frutas = list(dados.keys())
quantidades = list(dados.values())

df = pd.DataFrame({
    'Fruta': frutas,
    'Quantidade': quantidades
})

print("\nFrutas únicas encontradas:", frutas_unicas)
print("\nDataFrame com as frutas e quantidades:")
print(df.to_string(index=False))