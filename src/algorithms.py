import heapq
import networkx as nx
from typing import List, Tuple
from .utils import get_mutual_followers

def get_closest_connections(graph_data: dict, username: str, top_n: int = 10) -> List[Tuple[str, int]]:
    """Returns the top N closest connections (highest mutuals) for a user."""
    if username not in graph_data:
        raise ValueError(f"User {username} not found in dataset.")

    results = []
    # Check every person the user follows/is followed by
    neighbors = graph_data.get(username, [])
    
    for neighbor in neighbors:
        m = get_mutual_followers(graph_data, username, neighbor)
        results.append((neighbor, m))

    # Sort descending by mutual count
    results.sort(key=lambda x: -x[1])
    return results[:top_n]

def run_prims_algorithm(input_gexf: str, root_node: str, output_gexf: str):
    """
    Applies Prim's Algorithm to extract the Minimum Spanning Tree (MST).
    """
    G = nx.read_gexf(input_gexf)

    if root_node not in G:
        raise ValueError(f"Root node {root_node} not found in graph.")

    # Prim's Initialization
    visited = {root_node}
    edges_heap = [] # Priority Queue
    MST = nx.Graph()
    MST.add_node(root_node, label=root_node)

    # Add initial edges from root to priority queue
    for neighbor in G[root_node]:
        # NetworkX GEXF stores weights as attributes
        w = G[root_node][neighbor]['weight']
        heapq.heappush(edges_heap, (w, root_node, neighbor))

    # Process Queue
    while edges_heap:
        weight, u, v = heapq.heappop(edges_heap)

        if v in visited:
            continue

        # Add to MST
        visited.add(v)
        MST.add_node(v, label=v)
        MST.add_edge(u, v, weight=weight)

        # Add v's neighbors to queue
        for next_node in G[v]:
            if next_node not in visited:
                new_weight = G[v][next_node]['weight']
                heapq.heappush(edges_heap, (new_weight, v, next_node))

    # Save Result
    nx.write_gexf(MST, output_gexf)
    return MST