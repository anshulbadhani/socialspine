from typing import Dict, List, Set

def get_mutual_followers(graph: Dict[str, List[str]], u: str, v: str) -> int:
    """Calculates number of mutual followers between two users."""
    neighbors_u = set(graph.get(u, []))
    neighbors_v = set(graph.get(v, []))
    return len(neighbors_u & neighbors_v)

def calculate_weight(graph: Dict[str, List[str]], u: str, v: str) -> float:
    """
    Calculates edge weight based on the formula:
    w = 1 / (1 + mutual_followers)
    
    Lower weight implies a stronger connection (closer distance).
    """
    m = get_mutual_followers(graph, u, v)
    return 1 / (1 + m)