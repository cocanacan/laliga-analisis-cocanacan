"""
Módulo con las funciones del ejercicio 6 de la PEC4.
"""

import pandas as pd
import matplotlib.pyplot as plt
import config

# Función 1: goles totales
def fun_total_goals(data: pd.DataFrame) -> tuple[int, int, int]:
    """
    Función que devuelve una tupla de tres números enteros:
    (home_goals, away_goals, total_goals)
    """
    home_goals = int(data['FTHG'].sum())
    away_goals = int(data['FTAG'].sum())
    total_goals = home_goals + away_goals

    return home_goals, away_goals, total_goals


# Función 2: goles totales por equipo local, visitante y total
def fun_total_goals_by_team(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Función que devuelve una tupla de tres dataframes: goles por equipo local,
    visitante y total
    """

    home_goals_by_team = (data.groupby('HomeTeam')['FTHG']
                          .sum().rename('Goals')
                          .to_frame()
                          .sort_values('Goals', ascending = False))
    away_goals_by_team = (data.groupby('AwayTeam')['FTAG']
                          .sum()
                          .rename('Goals')
                          .to_frame()
                          .sort_values('Goals', ascending = False))
    total_goals_by_team = (home_goals_by_team['Goals']
                           .add(away_goals_by_team['Goals'], fill_value=0)
                           .rename('Goals')
                           .to_frame()
                           .sort_values('Goals', ascending = False))

    return home_goals_by_team, away_goals_by_team, total_goals_by_team


# Función 3:
def fun_summary_1996_2025(total_points_by_team: pd.DataFrame,
                          home_goals_by_team: pd.DataFrame,
                          away_goals_by_team: pd.DataFrame,
                          total_goals_by_team: pd.DataFrame) -> pd.DataFrame:
    """
    Crea un DataFrame con un sumario de goles y puntos por equipo
    """
    summary_1996_2026 = pd.concat([total_points_by_team,
                                   home_goals_by_team,
                                   away_goals_by_team,
                                   total_goals_by_team],
                                   axis=1)
    summary_1996_2026.columns = ['Total Points', 'Home Goals', 'Away Goals', 'Total Goals']

    return summary_1996_2026


# Función 4:
def podium(summary_1996_2025: pd.DataFrame) -> None:
    """
    Crea un diagrama de barras con el podium de la liga
    """
    top3 = summary_1996_2025.head(3)
    _ = top3.iloc[0]
    __ = top3.iloc[1]
    ___ = top3.iloc[2]

    orden_top3 = [top3.index[1], top3.index[0], top3.index[2]]
    puntos = [top3['Total Points'].iloc[1],
              top3['Total Points'].iloc[0],
              top3['Total Points'].iloc[2]]
    colors = ['silver', 'gold', 'peru']
    posiciones = [0, 1, 2]

    _, ax = plt.subplots(figsize=(10,6))
    ax.bar(top3.index, puntos, color = colors)
    ax.set_xticks(posiciones)
    ax.set_xticklabels(orden_top3)
    ax.set_xlabel('TOP 3')
    ax.set_ylabel('Points')
    ax.set_title('Partidos ganados por local y visitante y empatados (1995-2025)')
    plt.savefig(f"img/grafica_ex6_{config.nom_alumne}_{config.date_time}.png")
    plt.show()
