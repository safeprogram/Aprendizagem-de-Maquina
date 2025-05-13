from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

def preparar_dados_para_modelo(df):
    """Prepara o DataFrame limpo para o modelo de ML.

    Seleciona features, trata categóricas e define X e y.

    Args:
        df (pd.DataFrame): DataFrame limpo do Titanic.

    Returns:
        tuple: Contendo X (features) e y (target).
    """
    print("\nPreparando dados para o modelo...")
    # Selecionar colunas potenciais (remover as que não usaremos)
    df_modelo = df.drop(columns=['alive', 'who', 'adult_male', 'embark_town', 'alone'])

    # Converter 'sex' para numérico (0 ou 1)
    le = LabelEncoder()
    df_modelo['sex'] = le.fit_transform(df_modelo['sex'])
    print(">> Coluna 'sex' convertida para numérica.")

    # Converter 'embarked' e 'class' usando One-Hot Encoding
    df_modelo = pd.get_dummies(df_modelo, columns=['embarked', 'class'], drop_first=True)
    print(">> Colunas 'embarked' e 'class' convertidas com One-Hot Encoding.")

    # Definir X e y
    X = df_modelo.drop('survived', axis=1)
    y = df_modelo['survived']

    print(">> Features (X) e Target (y) definidos.")
    print("Shape de X:", X.shape)
    print("Shape de y:", y.shape)

    return X, y

def treinar_avaliar_modelo_titanic(X, y, test_size=0.3, random_state=42):
    """Divide os dados, treina Regressão Logística e avalia.

    Args:
        X (pd.DataFrame): Features.
        y (pd.Series): Target.
        test_size (float): Proporção para o conjunto de teste.
        random_state (int): Seed para reprodutibilidade.

    Returns:
        float: Acurácia do modelo no conjunto de teste.
    """
    print("\nDividindo dados em treino e teste...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    print(f">> Dados divididos: {len(X_train)} treino, {len(X_test)} teste.")

    print("\nTreinando modelo de Regressão Logística...")
    modelo = LogisticRegression(max_iter=1000) # Aumentar max_iter pode ser necessário
    modelo.fit(X_train, y_train)
    print(">> Modelo treinado.")

    print("\nFazendo previsões e avaliando...")
    y_pred = modelo.predict(X_test)
    acuracia = accuracy_score(y_test, y_pred)
    print(f">> Acurácia no conjunto de teste: {acuracia:.4f}")

    return acuracia

# --- Execução ---
X_titanic, y_titanic = preparar_dados_para_modelo(titanic_df_limpo.copy())
acuracia_titanic = treinar_avaliar_modelo_titanic(X_titanic, y_titanic)