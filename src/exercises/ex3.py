"""
Módulo con las funciones del ejercicio 3 de la PEC4.
"""

import pandas as pd
import matplotlib.pyplot as plt
import config

def goals_distribution(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Función que devuelve dos dataframes con la distribución 
    de goles marcados por los equipos de casa y de fuera.
    """

    # Con value_counts contamos la frecuencia con la que se repite los goles
    # con sort_index ordenamos por orden numérico y no por frecuencia
    # rename_axis da el nombre de 'Goals'
    # reset_index() saca el índice da el nombre de matches
    # y convierte la serie en DataFrame
    # Con set_index vuelve a establecer el índice de goals
    distr_goals_home = (data['FTHG'].value_counts()
                        .sort_index().rename_axis('Goals')
                        .reset_index(name='Matches')
                        .set_index('Goals'))
    distr_goals_away = (data['FTAG'].value_counts()
                        .sort_index()
                        .rename_axis('Goals')
                        .reset_index(name='Matches')
                        .set_index('Goals'))
    return distr_goals_home, distr_goals_away


def plot_goals_distribution(distr_goals_home: pd.DataFrame, distr_goals_away: pd.DataFrame) -> None:
    """
    Representa la distribución de goles de los equipos locales y visitantes
    """
    # De nuevo, en una figura vamos a poner dos imágenes en 1 fila y 2 columnas
    _, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,6))

    # Figura 1:
    ax1.bar(distr_goals_home.index, distr_goals_home['Matches'], color='plum')
    ax1.set_xlabel('Goles')
    ax1.set_ylabel('Número de partidos')
    ax1.set_title('Distribución de goles en casa (1995-2025)')
    ax1.set_xticks(distr_goals_home.index)

    # Figura 2:
    ax2.bar(distr_goals_away.index, distr_goals_away['Matches'], color='cadetblue')
    ax2.set_xlabel('Goles')
    ax2.set_ylabel('Número de partidos')
    ax2.set_title('Distribución de goles visitante (1995-2025)')
    ax1.set_xticks(distr_goals_away.index)
    plt.savefig(f"img/grafica_ex3_{config.nom_alumne}_{config.date_time}.png")
    plt.show()
