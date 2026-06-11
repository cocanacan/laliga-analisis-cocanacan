"""
Módulo con las funciones del ejercicio 1 de la PEC4.
"""

import pandas as pd
import matplotlib.pyplot as plt
import config

def load_and_eda(file:str) -> pd.DataFrame:
    """
    Carga el dataset denominado LaLiga_Matches;
    elimina las columnas "HTHG", "HTAG", "HTR";
    Muestra los tres primeros y tres últimos valores del dataset (filas),
    y la información más relevante.

    Args:
      File: Ruta al fichero CSV LaLiga_Matches

    Returns:
      Un DataFrame limpio con los datos cargados.

    """

    # Carga del fichero:
    df = pd.read_csv(file)

    # Eliminación de columnas HTHG, HTAG y HTR con .drop
    df = df.drop(columns = ['HTHG', 'HTAG', 'HTR'])


    print(df.head())
    print(df.tail())

    # Para mostrar información general usaremos: info() -> tipos, nulos...
    print(df.info())

    # Estadísticas descriptivas
    print(df.describe())

    return df


def plot_home_away_goals(data: pd.DataFrame) -> None:
    """
    La función muestra una figura con las distribuciones de goles marcados
    por equipos de casa y de fuera.
    """
    # Creamos una figura de dimensiones 10x6 con dos sublplots
    figura, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,6))

    # Goles del equipo local
    ax1.boxplot(data["FTHG"].dropna())
    ax1.set_title("Goles del equipo local")
    ax1.set_ylabel("Número de goles")
    ax1.set_xticklabels(["Local"])

    # Goles del equipo visitante
    ax2.boxplot(data["FTAG"].dropna())
    ax2.set_title("Goles del equipo visitante")
    ax2.set_ylabel("Número de goles")
    ax2.set_xticklabels(["Visitante"])


    figura.suptitle("Distribución de goles: Local vs Visitante (1995-2025)", fontsize=13)
    plt.savefig(f"img/grafica_ex1_{config.nom_alumne}_{config.date_time}.png")
    plt.show()

