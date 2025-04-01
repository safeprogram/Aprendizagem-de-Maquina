import pandas as pd
from sklearn.linear_model import LogisticRegression

dado = pd.read_csv('dado.csv')

X = dado[['imc']]
y = dado['obeso']

model = LogisticRegression()
model.fit(X, y)

new_bmi = 32.5 
prediction = model.predict([[new_bmi]])
probability = model.predict_proba([[new_bmi]])

print(f"\nAnálise para IMC {new_bmi}:")
print(f"Classificação: {'Obeso' if prediction[0] else 'Não obeso'}")
print(f"Probabilidade de obesidade: {probability[0][1]:.2%}")