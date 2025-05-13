from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def comparar_estimadores_iris(test_size=0.25, random_state=42):
    """Carrega Iris, treina KNN e SVC, e salva resultados em TXT.

    Args:
        test_size (float): Proporção para o conjunto de teste.
        random_state (int): Seed para reprodutibilidade.

    Returns:
        dict: Dicionário com as acurácias de cada modelo.
    """
    print("\n--- Exercício 3: Comparando Estimadores no Iris ---")
    # 1. Carregar dados
    iris = load_iris()
    X_iris, y_iris = iris.data, iris.target
    print(">> Dataset Iris carregado.")
    print(f">> Features: {iris.feature_names}")
    print(f">> Classes: {iris.target_names}")

    # 2. Dividir dados
    X_train, X_test, y_train, y_test = train_test_split(X_iris, y_iris, test_size=test_size, random_state=random_state)
    print(f">> Dados divididos: {len(X_train)} treino, {len(X_test)} teste.")

    resultados = {}

    # 3. Treinar e Avaliar KNN
    print("\nTreinando K-Nearest Neighbors (KNN)...")
    knn = KNeighborsClassifier(n_neighbors=3) # Exemplo com k=3
    knn.fit(X_train, y_train)
    y_pred_knn = knn.predict(X_test)
    acc_knn = accuracy_score(y_test, y_pred_knn)
    resultados['KNN'] = acc_knn
    print(f">> Acurácia KNN: {acc_knn:.4f}")

    # 4. Treinar e Avaliar SVC
    print("\nTreinando Support Vector Classifier (SVC)...")
    svc = SVC() # Usando parâmetros default
    svc.fit(X_train, y_train)
    y_pred_svc = svc.predict(X_test)
    acc_svc = accuracy_score(y_test, y_pred_svc)
    resultados['SVC'] = acc_svc
    print(f">> Acurácia SVC: {acc_svc:.4f}")

    # 5. Salvar resultados em TXT
    nome_arquivo = 'resultados_iris.txt'
    try:
        with open(nome_arquivo, 'w') as f:
            f.write("Resultados da Comparação de Modelos no Dataset Iris\n")
            f.write("="*50 + "\n")
            for modelo, acuracia in resultados.items():
                f.write(f"Modelo: {modelo}\n")
                f.write(f"Acurácia no conjunto de teste: {acuracia:.4f}\n")
                f.write("-" * 20 + "\n")
        print(f"\n>> Resultados salvos em '{nome_arquivo}'. Verifique no painel 'Arquivos' do Colab.")
    except Exception as e:
        print(f"\n>> Erro ao salvar arquivo '{nome_arquivo}': {e}")

    return resultados

# --- Execução ---
resultados_comparacao = comparar_estimadores_iris()