import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # Usaremos seaborn para facilitar alguns plots
import kagglehub # Para carregar o arquivo direto do site.
from kagglehub import KaggleDatasetAdapter

def carregar_dados_alunos(nomeArquivo='Students_Grading_Dataset.csv'):
    """Carrega o dataset de notas de alunos do arquivo CSV.

    Args:
        nomeArquivo (str): Caminho para o arquivo CSV no ambiente Colab.

    Returns:
        pd.DataFrame: DataFrame com os dados dos alunos.
    """
    try:
        df = pd.read_csv(nomeArquivo)
        print(f"Dataset de alunos carregado de '{nomeArquivo}'.")
        print(f"Shape do DataFrame: {df.shape}")
        # Verificar nomes das colunas (importante!)
        print("Colunas:", df.columns.tolist())
        return df
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nomeArquivo}' não encontrado.")
        print("Fazendo download diretamente do site.")
        try:
          # Download diretamente do site
          # "\" serve para quebrar a
          # linha e deixar o código mais legível
          # Verifique se este é o nome correto do arquivo no dataset
          path = kagglehub.dataset_download("mahmoudelhemaly/students-grading-dataset")
          caminho_completo_csv = os.path.join(path, nomeArquivo)
          print(f"Tentando carregar o arquivo: {caminho_completo_csv}")

          # Verificar se o arquivo existe antes de tentar carregar
          if os.path.exists(caminho_completo_csv):
          # Usar pandas para carregar o arquivo CSV para um DataFrame
             df = pd.read_csv(caminho_completo_csv)
             return df
          else:
            raise Exception (f"Arquivo não encontrado {caminho_completo_csv}")
        except Exception as e:
          print(f"Erro ao fazer download do dataset: {e}")
          return None
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return None


def visualizar_dados_alunos(df):
    """Gera 3 tipos de gráficos para explorar o dataset de alunos.

    Args:
        df (pd.DataFrame): DataFrame dos alunos.
    """
    if df is None:
        print("DataFrame não carregado. Não é possível gerar gráficos.")
        return

    print("\n--- Exercício 4: Visualizando Dados dos Alunos ---")
    plt.style.use('seaborn-v0_8-whitegrid') # Estilo visual

    # Gráfico 1: Histograma das Notas Finais
    plt.figure(figsize=(10, 5))
    sns.histplot(df['Final_Score'], kde=True, bins=10)
    plt.title('Distribuição das Notas Finais (final_grade)')
    plt.xlabel('Nota Final')
    plt.ylabel('Frequência')
    plt.show()
    print(">> Gráfico 1: Histograma de 'final_grade' gerado.")

    # Gráfico 2: Dispersão (Study Hours vs Final Grade)
    plt.figure(figsize=(10, 5))
    sns.scatterplot(x='Study_Hours_per_Week', y='Final_Score', data=df, alpha=0.6)
    plt.title('Relação entre Horas de Estudo e Nota Final')
    plt.xlabel('Horas de Estudo (Study_Hours_per_Week)')
    plt.ylabel('Nota Final (Final_Score)')
    plt.show()
    print(">> Gráfico 2: Scatter plot de 'Study_Hours_per_Week' vs 'Final_Score' gerado.")

    # Gráfico 3: Box Plot (Final Grade por Parent Education)
    # Ordenar as categorias de educação para melhor visualização
    ordem_educacao = sorted(df['Parent_Education_Level'].unique(), key=lambda x: str(x)) # Ordem simples
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Parent_Education_Level', y='Final_Score', data=df, order=ordem_educacao)
    plt.title('Distribuição da Nota Final por Educação dos Pais')
    plt.xlabel('Educação dos Pais (Parent_Education_Level)')
    plt.ylabel('Nota Final (Final_Score)')
    plt.xticks(rotation=45, ha='right') # Rotacionar labels se forem muitos
    plt.tight_layout() # Ajustar layout
    plt.show()
    print(">> Gráfico 3: Box plot de 'Final_Score' por 'Parent_Education_Level' gerado.")

# --- Execução ---
# Certifique-se que o nome do arquivo corresponde ao que você fez upload
alunos_df = carregar_dados_alunos('Students_Grading_Dataset.csv')
if alunos_df is not None:
    visualizar_dados_alunos(alunos_df)