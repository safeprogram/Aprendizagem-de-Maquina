import pandas as pd
import seaborn as sns
import numpy as np

def carregar_dados_titanic():
    """Carrega o dataset Titanic a partir do Seaborn.

    Returns:
        pd.DataFrame: DataFrame do Titanic.
    """
    df = sns.load_dataset('titanic')
    print("Dataset Titanic carregado com sucesso via Seaborn.")
    print(f"Shape do DataFrame: {df.shape}")
    return df

def limpar_dados_titanic(df):
    """Limpa o DataFrame do Titanic tratando valores ausentes.

    Args:
        df (pd.DataFrame): DataFrame original do Titanic.

    Returns:
        pd.DataFrame: DataFrame limpo.
    """
    print("\nIniciando limpeza dos dados...")
    print("Valores nulos ANTES da limpeza:\n", df.isnull().sum())

    # Tratar 'age' com a mediana
    mediana_idade = df['age'].median()
    df['age'].fillna(mediana_idade, inplace=True)
    print(f"\n>> 'age' preenchido com mediana: {mediana_idade}")

    # Tratar 'embarked' com a moda
    # Nota: 'embark_town' também tem nulos e geralmente corresponde a 'embarked'.
    # Vamos preencher ambos com a moda de 'embarked'.
    moda_embarked = df['embarked'].mode()[0]
    df['embarked'].fillna(moda_embarked, inplace=True)
    df['embark_town'].fillna(df[df['embarked'] == moda_embarked]['embark_town'].mode()[0], inplace=True)
    print(f">> 'embarked' preenchido com moda: {moda_embarked}")
    print(f">> 'embark_town' preenchido com valor correspondente à moda de 'embarked'.")

    # Remover 'deck' e 'cabin'
    colunas_para_remover = []
    if 'deck' in df.columns:
        colunas_para_remover.append('deck')
    if 'cabin' in df.columns:
         colunas_para_remover.append('cabin')

    if colunas_para_remover:
        df.drop(columns=colunas_para_remover, inplace=True)
        print(f">> Colunas {colunas_para_remover} removidas.")
    else:
        print(">> Colunas 'deck' e 'cabin' não encontradas para remoção.")


    print("\nValores nulos APÓS a limpeza:\n", df.isnull().sum())
    if df.isnull().sum().sum() == 0:
        print("\n>> Todos os valores nulos tratados com sucesso!")
    else:
        print("\n>> Atenção: Ainda existem valores nulos!")

    print("Limpeza concluída.")
    return df

# --- Execução ---
titanic_df_original = carregar_dados_titanic()
titanic_df_limpo = limpar_dados_titanic(titanic_df_original.copy()) # Usar cópia!

print("\nPrimeiras 5 linhas do DataFrame limpo:")
print(titanic_df_limpo.head())