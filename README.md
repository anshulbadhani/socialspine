# SocialSpine: Instagram Network Analyzer

**A Discrete Mathematical Structures Project**

SocialSpine is a CLI tool that applies Graph Theory to analyze social connections on Instagram. By modeling followers as a weighted undirected graph, it uses **Prim's Algorithm** to filter out noise and identify the "Social Backbone"—the Minimum Spanning Tree (MST) that keeps a friend group connected using the strongest possible bonds.

## 📖 Project Overview

Social media networks are often dense and noisy. This project aims to extract meaningful structural insights from a user's follower list using discrete mathematical concepts.

**Key Objectives:**
1.  **Ethical Data Collection:** Parsing HTTP Archive (HAR) files from manual browsing sessions (no automated scraping).
2.  **Graph Construction:** Converting raw follower lists into a weighted undirected graph.
3.  **Algorithmic Analysis:**
    * **Weight Function:** $w = \frac{1}{1+m}$ (Inverse of mutual followers).
    * **Prim's Algorithm:** Computing the Minimum Spanning Tree (MST).
    * **Centrality:** Identifying "Best Friends" and central nodes.

## 🧮 Mathematical Model

The project relies on the following discrete structures:

* **Graph:** $G = (V, E)$ where $V$ is the set of users and $E$ represents follower relationships.
* **Weights:** We define the "distance" between two users based on mutual connections.
    $$w(u, v) = \frac{1}{1 + \text{mutuals}(u, v)}$$
    * *High Mutuals* $\rightarrow$ *Low Weight* $\rightarrow$ *Close Connection*.
* **MST:** A subgraph that connects all vertices with the minimum possible total edge weight, revealing the core structure of the social group without cycles.

## ⚡ Features

* **HAR Parser:** Extracts username data securely from browser network logs.
* **Adjacency Builder:** Maintains a JSON-based adjacency list of the network.
* **GEXF Export:** Generates `.gexf` files compatible with **Gephi** for professional visualization.
* **CLI Interface:** Easy-to-use command line tools for every step of the process.

## 📂 Project Structure

```text
instagram_graph_project/
│
├── data/                   # Store your .har and .json files here
├── src/                    # Source code
│   ├── __init__.py
│   ├── utils.py            # Math logic (Weights, Mutuals)
│   ├── parser.py           # HAR file processing
│   ├── graph_builder.py    # NetworkX graph generation
│   └── algorithms.py       # Prim's and Best Friends logic
├── main.py                 # Entry point for the CLI
└── requirements.txt        # Python dependencies
```
## 🚀 Installation

    Clone the repository:
```Bash

git clone [https://github.com/anshulbadhani/socialspine.git](https://github.com/yourusername/socialspine.git)
cd socialspine
```
*Note: You must have `astra-uv` installed.*
## 🛠️ Usage Guide

Step 1: Data Extraction

Download a `.har` file from Instagram (via Firefox/Chrome DevTools) and extract the followers.
```Bash

uv run main.py extract --username <target_user> --har-path ./data/username.har
```
Step 2: Build the Graph

Convert the raw JSON data into a weighted GEXF graph file.
```Bash

uv run main.py build --input-json adjacency.json --output-gexf full_graph.gexf
```
Step 3: Analyze "Best Friends"

Find the closest connections for a specific user based on mutual follower counts.
```Bash

uv run main.py best-friends --username <target_user> --top 10
```
Step 4: Generate the Social Backbone (MST)

Run Prim's Algorithm to generate the Minimum Spanning Tree file.
```Bash

uv run main.py mst --root <root_user> --input-gexf full_graph.gexf --output-gexf mst.gexf
```
Note: The resulting .gexf files can be opened in Gephi for visualization.

## 📊 Visualizations

This project enables the transformation of noisy data into structured graphs:

    Full Graph: A dense, hairball-like structure representing all connections.

    MST: A clean, tree-like structure highlighting the most critical relationships.

## 🤝 Author

    Anshul Badhani

Developed as a term project for the Discrete Mathematical Structures course.

## 📜 License

This project is open-source and available under the MIT License.