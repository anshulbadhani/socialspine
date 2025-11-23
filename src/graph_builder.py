import json
import networkx as nx
from .utils import calculate_weight

def load_adjacency_json(json_path: str) -> dict:
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def build_weighted_graph(json_path: str, output_gexf: str):
    """
    Converts JSON adjacency list to a Weighted Undirected GEXF Graph.
    Nodes = Users
    Edges = Relationships
    Weight = 1 / (1 + Mutuals)
    """
    raw_data = load_adjacency_json(json_path)
    G = nx.Graph()

    # Add all nodes first
    for user in raw_data:
        G.add_node(user, label=user)

    # Add weighted edges
    for u in raw_data:
        for v in raw_data[u]:
            # Calculate weight
            w = calculate_weight(raw_data, u, v)
            
            # Add edge (NetworkX handles duplicates for undirected graphs automatically)
            G.add_edge(u, v, weight=w)

    nx.write_gexf(G, output_gexf)
    return G