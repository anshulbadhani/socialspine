import typer
from src import parser, graph_builder, algorithms

app = typer.Typer(help="Instagram Graph Analysis Tool - Discrete Math Project")

# --- COMMANDS ---

@app.command()
def extract(
    username: str = typer.Option(..., help="Username associated with the HAR file"),
    har_path: str = typer.Option(..., help="Path to the .har file"),
    json_path: str = typer.Option("adjacency.json", help="Master adjacency list file")
):
    """Step 1: Parse HAR file and update JSON database."""
    try:
        typer.echo(f"Processing HAR for {username}...")
        followers = parser.parse_har_file(har_path, username)
        parser.update_adjacency_list(json_path, username, followers)
        typer.echo(f"✅ Extracted {len(followers)} followers. Updated {json_path}")
    except Exception as e:
        typer.echo(f"Error: {e}")

@app.command()
def build(
    input_json: str = typer.Option("adjacency.json", help="Input JSON file"),
    output_gexf: str = typer.Option("graph.gexf", help="Output GEXF file")
):
    """Step 2: Convert JSON to Weighted Undirected GEXF Graph."""
    try:
        G = graph_builder.build_weighted_graph(input_json, output_gexf)
        typer.echo(f"✅ Graph built: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges.")
        typer.echo(f"Saved to {output_gexf}")
    except Exception as e:
        typer.echo(f"Error: {e}")

@app.command()
def best_friends(
    username: str = typer.Option(..., help="User to analyze"),
    input_json: str = typer.Option("adjacency.json", help="Input JSON file"),
    top: int = 10
):
    """Step 3a: Find 'Best Friends' (Closest connections by mutuals)."""
    try:
        data = graph_builder.load_adjacency_json(input_json)
        friends = algorithms.get_closest_connections(data, username, top)
        
        typer.echo(f"\n🌟 Best Friends for {username}:")
        for rank, (name, count) in enumerate(friends, 1):
            typer.echo(f"{rank}. {name} ({count} mutuals)")
    except Exception as e:
        typer.echo(f"Error: {e}")

@app.command()
def mst(
    root: str = typer.Option(..., help="Root node for Prim's Algorithm"),
    input_gexf: str = typer.Option("graph.gexf", help="Input Full Graph"),
    output_gexf: str = typer.Option("mst.gexf", help="Output MST Graph")
):
    """Step 3b: Generate Minimum Spanning Tree using Prim's Algorithm."""
    try:
        T = algorithms.run_prims_algorithm(input_gexf, root, output_gexf)
        typer.echo(f"✅ MST Generated with {T.number_of_nodes()} nodes.")
        typer.echo(f"Saved to {output_gexf}")
    except Exception as e:
        typer.echo(f"Error: {e}")

if __name__ == "__main__":
    app()