"""
Módulo con las funciones del ejercicio 4 de la PEC4.
"""

import pandas as pd
import matplotlib.pyplot as plt
import config

def FTR(data: pd.DataFrame) -> pd.DataFrame:
    """
    Función que devuelve un dataframe con el número de 
    partidos ganados, perdidos y empatados
    por los equipos locales y visitantes
    """
    ftr = data['FTR'].value_counts().to_frame()
    ftr.index.name = 'Results'
    ftr.columns = ['Number of Matches']

    return ftr


def plot_FTR(ftr: pd.DataFrame) -> None:
    """
    Función que representa un gráfico de barras con el número de partidos 
    ganados, perdidos y empatados
    por los equipos locales y visitantes
    """
    _, ax = plt.subplots(figsize=(6,6))
    ax.bar(ftr.index, ftr['Number of Matches'], color='olive')
    ax.set_xlabel('Results')
    ax.set_ylabel('Number of Matches')
    ax.set_title('Partidos ganados por local y visitante y empatados (1995-2025)')
    plt.savefig(f"img/grafica_ex4_{config.nom_alumne}_{config.date_time}.png")
    plt.show()
