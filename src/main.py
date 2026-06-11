"""PEC4 - Análisis LaLiga 1995-2025."""

import argparse
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))
from exercises import ex1
from exercises import ex2
from exercises import ex3
from exercises import ex4
from exercises import ex5
from exercises import ex6
from exercises import ex7


# Personal
NOM_ALUMNE = "cecilia_ocana"
date_time = datetime.now().strftime('%Y%m%d_%H%M%S')


# Vamos a utilizar el módulo argparse, diseñado para construir interfaces de línea

def argp():
    '''
    Define y lee argumentos de línea de comandos.
    '''
    parser = argparse.ArgumentParser(description= 'Análisis de los partidos de La Liga 1995-2025')
    parser.add_argument('-ex',
                        type = int,
                        choices = range(1, 8),
                        metavar = 'N',
                        help = 'Ejecuta los ejercicios del 1 al 7')
    return parser.parse_args()

def main():
    '''
    Función que ejecuta los ejercicios mediante el argumento -ex
    '''
    args = argp()

    if args.ex is None:
        print("Uso: python main.py -ex N  (N entre 1 y 7)")
        print("     python main.py -h     (ayuda)")
        sys.exit(0)

    data_path = os.path.join(os.path.dirname(__file__), "data", "LaLiga_Matches.csv")

    if args.ex >= 1:
        print("\n=== Ejercicio 1 ===")
        data = ex1.load_and_eda(data_path)
        ex1.plot_home_away_goals(data)

    if args.ex >= 2:
        print("\n=== Ejercicio 2 ===")
        total = ex2.total_matches(data)
        print(total)
        max_matches = total['total_matches'].max()
        siempre_primera = total[total['total_matches'] == max_matches]
        print(siempre_primera)
        ex2.plot_matches_team_total(total)

    if args.ex >= 3:
        print("\n=== Ejercicio 3 ===")
        distr_home, distr_away = ex3.goals_distribution(data)
        print(distr_home)
        print(distr_away)
        ex3.plot_goals_distribution(distr_home, distr_away)

    if args.ex >= 4:
        print("\n=== Ejercicio 4 ===")
        ftr = ex4.FTR(data)
        print(ftr)
        total = ftr['Number of Matches'].sum()
        prt = ftr.loc['H', 'Number of Matches'] / total * 100
        print(f'Partidos ganados por locales: {prt:.2f}%')
        ex4.plot_FTR(ftr)


    if args.ex >= 5:
        print("\n=== Ejercicio 5 ===")
        print("\n=== Ejercicio 5 ===")
        data = ex5.add_points(data)
        _, total_points_df = ex5.fun_total_points(data)
        winner = ex5.all_time_winner(total_points_df)
        print(f'Ganador histórico: {winner}')

    if args.ex >= 6:
        print("\n=== Ejercicio 6 ===")
        home_goals, away_goals, total_goals = ex6.fun_total_goals(data)
        print(f'Goles local: {home_goals}, visitante: {away_goals}, total: {total_goals}')
        home_g, away_g, total_g = ex6.fun_total_goals_by_team(data)
        summary = ex6.fun_summary_1996_2025(total_points_df, home_g, away_g, total_g)
        print(summary)
        ex6.podium(summary)

    if args.ex >= 7:
        print("\n=== Ejercicio 7 ===")
        print("\n=== Ejercicio 7 ===")
        selected_teams = total_points_df.head(5).index.tolist()
        ex7.graf(data, selected_teams)


if __name__ == "__main__":
    main()
