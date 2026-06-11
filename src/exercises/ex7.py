"""
Módulo con las funciones del ejercicio 7 de la PEC4.
"""

import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import config

def graf(data: pd.DataFrame, selected_teams: list) -> None:
    """
    Genera un grafo de conexiones entre los 5 equipos con mejor puntuación
    """
    # Filtramos filas donde visitante y local estén en selected_teams
    filtered = data['HomeTeam'].isin(selected_teams) & data['AwayTeam'].isin(selected_teams)
    filtered_data = data[filtered]

    # Necesitamos que la selección los equipos que juegan esten en
    # selected_teams. Por ello, desde filtered_data vamos a filtrar
    # para que ambos equipos que juegen estén en selected_teams

    teams = {}
    for _, row in filtered_data.iterrows():
        pair = tuple(sorted([row['HomeTeam'], row['AwayTeam']]))
        if pair in teams:
            teams[pair] += 1
        else:
            teams[pair] = 1

    graph = nx.Graph()
    graph.add_nodes_from(selected_teams)
    for (team_a, team_b), c in teams.items():
        graph.add_edge(team_a, team_b, weight = c)

    _, ax = plt.subplots(figsize=(10,6))
    pos = nx.circular_layout(graph)
    nx.draw_networkx_nodes(graph, pos, node_size=2000, node_color='violet', ax=ax)
    nx.draw_networkx_labels(graph, pos, font_size=9, font_color='black', font_weight='bold', ax=ax)
    nx.draw_networkx_edges(graph, pos, width=2, edge_color='olive', ax=ax)

    # Etiquetas de peso (nº de conexiones) en las aristas
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=10, ax=ax)

    ax.set_title('Grafo de conexiones entre los 5 equipos con mejor puntuación', fontsize=13)
    ax.axis('off')
    plt.savefig(f"img/grafica_ex7_{config.nom_alumne}_{config.date_time}.png")
    plt.show()
