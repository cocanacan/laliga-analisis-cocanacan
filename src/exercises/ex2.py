"""
Módulo con las funciones del ejercicio 2 de la PEC4.
"""

import pandas as pd
import matplotlib.pyplot as plt
import config

def total_matches(data: pd.DataFrame) -> pd.DataFrame:
    """
    Función que devuelve un dataframe con el número 
    de partidos jugados por cada equipo.
    """

    # Usamos value_counts para contar la frecuencia de cada valor

    # Partidos como local
    home_matches = data["HomeTeam"].value_counts()

    # Partidos como visitante
    away_matches = data["AwayTeam"].value_counts()

    # Con home_matches.add(away_matches, fill_value=0) sumamos los partidos
    # local + visitante, con fill_value evitamos los datos NaN.
    # Usamos astype(int) para asegurarnos enteros
    # usamos sort_values para ordenarlos de manera descendente
    # con rename llamamos a la columna total_matches
    # con to_frame convertimos la Serie a Data_Frame

    matches_team_total = (home_matches
                          .add(away_matches, fill_value=0)
                          .astype(int)
                          .sort_values(ascending=False)
                          .rename('total_matches')
                          .to_frame())

    # Con name damos nombre al índice de la columna de equipos
    matches_team_total.index.name = 'Team'

    return matches_team_total


def plot_matches_team_total(matches_team_total: pd.DataFrame) -> None:
    """
    Función que muestra un gráfico de barras con el número de partidos jugados por cada equipo.
    """

    # Creamos una figura con dimensión 10x6
    _, ax= plt.subplots(figsize=(10,6))
    ax.grid()


    # Utilizaremos un gráfico de barras cuyo eje x tendrá los equipos y el
    # eje y tendrá el número de partidos jugados
    ax.bar(matches_team_total.index, matches_team_total['total_matches'], color='orchid')
    ax.set_xlabel('Equipos')
    ax.set_ylabel('Número de partidos jugados')
    ax.set_title('Total de partidos jugados por equipo (1995-2025)')

    # Si ejecutamos aquí la imagen, se sobrepondrán los nombres de los equipos
    # uno con otro, por ello vamos a usar las funciones: ax.ticks_params para
    # rotar las etiquetas
    ax.tick_params(axis='x', rotation=90)
    plt.savefig(f"img/grafica_ex2_{config.nom_alumne}_{config.date_time}.png")
    plt.show()
