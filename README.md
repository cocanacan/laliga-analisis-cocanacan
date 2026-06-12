# Análisis de La Liga 1995-2025
## Autoría: Cecilia Ocaña Cano
## Asignatura: Programación para la Ciencia de Datos
## Master Ciencia de Datos. Univeristat Oberta de Catalunya (UOC)

## Descripción del proyecto.

Este proyecto realiza un análisis de los resultados de La Liga entre los años 1995 y 2025.
Los datos provienen del ficher CSV LaLiga_Matches.csv

El proyecto incluye análisis de goles, clasificaciones históricas, recuento de puntos,
distribución de resultados y visualizaciones gráficas de los resultados organizado en
un proyecto Python modular, que incluye documentación, test y control de calidad del código.

## Funcionalidades
- Carga y análisis del dataset (LaLiga_Matches.csv)
- Visualización de la distribución de los goles marcados por equipos locales y visitantes
- Análisis y visualización del número de partidos jugados en La Liga por todos los equipos
- Análisis de la distribución del número de goles marcados por equipos locales y visitantes
- Análisis y visualización del número de partidos ganados por equipos locales y visitantes
- Análisis de puntos de los equipos de La Liga
- Acumulación de puntos de los equipos de La Liga desde 1995
- Visualización del equipo con más puntos históricos
- Grafo de conexiones entre los 5 primeros equipos con más puntos

## Funciones ejercicios

### Ejercicio 1
- load_and_eda: carga el dataset y lo limpia
- plot_home_away_goals: gráfica de distribuciones de goles marcados de equipos locales y visitantes

### Ejercicio 2
- total_matches: devuelve el número de partidos totales jugados por cada equipo
- plot_matches_team_total: gráfico de barras que muestra el número de partidos totales jugados por cada equipo

### Ejercicio 3
- goals_distribution: devuelve dos dataframes con la distribución de goles marcados por equipos locales y visitantes
- plot_goals_distribution: representación de la distribución de goles marcados por equipos locales y visitantes

### Ejercicio 4
- FTR: devuelve un dataframe con el número de partidos ganados, perdidos y empatados por los equipos locales y visitantes
- plot_FTR: gráfico de barras con el número de partidos ganados, perdidos y empatados por los equipos locales y visitantes

### Ejercicio 5
- add_points: añade al dataset los puntos conseguidos como local y como visitante
- fun_total_points: devuelve un dataframe con el número de puntos totales de cada equipo
- all_time_winner: devuelve el ganador de la liga histórica y acumulada

### Ejercicio 6
- fun_total_goals: devuelve una tupla de tres números enteros:(home_goals, away_goals, total_goals)
- fun_total_goals_by_team: devuelve una tupla de tres dataframes: goles por equipo local, visitante y total
- fun_summary_1996_2025: crea un DataFrame con un sumario de goles y puntos por equipo
- podium: crea un diagrama de barras con el podium de la liga

### Ejercicio 7
- graf: genera un grafo de conexiones entre los 5 equipos con mejor puntuación

## INPUT FORMAT
El programa analiza el fichero LaLiga_Matches.csv, compuesto por las columanas:
- FTHG - Number of goals scored by Home Team.
- FTAG - Number of goals scored by Away Team.
- FTR - Full time result.
- HTHG - Number of goals scored by Home Team at Half time.
- HTAG - Number of goals scored by Away Team at Half time.
- HTR - Half time result.
- H - Home Team.
- A - Away Team.
- D - Draw.

El programa también acepta el argumento -ex para indicar hasta qué ejercicio ejecutar: ej: -ex 7

## STEPS TO RUN main.py
1. git clone https://github.com/cocanacan/laliga-analisis-cocanacan.git
2. cd laliga-analisis-cocanacan
3. python -m venv .venv && source .venv/bin/activate
4. pip install -r requirements.txt
5. python src/main.py -ex 7

## LINTING, TEST Y DOCUMENTACIÓN
1. pylint src/
2. pdoc --html --output-dir doc src/exercises/
3. python -m unittest tests/tests_ex6.py -v

## OUTPUT PROGRAM
El programa genera por ejercicio sus resultados (tablas, estadísticas, etc) y gráficos que se guardarán en la carpeta img/ con el nombre del alumno y el timestamp.
