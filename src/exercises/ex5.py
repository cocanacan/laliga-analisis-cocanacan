"""
Módulo con las funciones del ejercicio 5 de la PEC4.
"""

import pandas as pd

def add_points(data: pd.DataFrame) -> pd.DataFrame:
    """
    Función que añade al dataset los puntos conseguidos como local y como visitante
    """
    # Realizamos una función por categoría. Con el bucle if establecemos la
    # adjudicación de puntos de cada partido
    def points_home(results: str) -> int:
        """
        Función que devuelve los puntos conseguidos por el equipo local
        """
        if results == 'H':
            return 3
        if results == 'D':
            return 1
        return 0

    def points_away(results: str) -> int:
        """
        Función que devuelve los puntos conseguidos por el equipo visitante
        """
        if results == 'A':
            return 3
        if results == 'D':
            return 1
        return 0

    data['points_home'] = data['FTR'].apply(points_home)
    data['points_away'] = data['FTR'].apply(points_away)

    return data

def fun_total_points(data: pd.DataFrame) -> tuple[pd.Series, pd.DataFrame]:
    """
    Función que devuelve un dataframe con el número de puntos totales de cada equipo
    """
    # Para sumar todos los puntos por cada equipo, usamos groupby que sumará los
    # puntos de aquellos nombres iguales
    home_points = data.groupby('HomeTeam')['points_home'].sum()
    away_points = data.groupby('AwayTeam')['points_away'].sum()
    total_points = home_points.add(away_points, fill_value=0).astype(int).sort_values(ascending=False).rename('total_points')
    total_points.index.name = 'Team'

    total_points_df = total_points.to_frame()

    return total_points, total_points_df

def all_time_winner(df_total_points: pd.DataFrame) -> str:
    """
    Función que devuelve el ganador de la liga histórica y acumulada
    """

    # El máximo de puntos de LaLiga es el ganador. Sacamos el máximo de puntos
    # y el ganador será el equipo cuyo máximo de puntos tenga
    max_points = df_total_points['total_points'].max()
    winner = df_total_points[df_total_points['total_points'] == max_points]
    return winner.index[0]
