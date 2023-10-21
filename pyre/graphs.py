import json
import math
from pathlib import Path
from typing import Any, Dict, List, Tuple
import csv
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from pyvis.network import Network
import click
import json
import networkx

def bezier_curve(
    src: np.ndarray, ctrl: List[float], dst: np.ndarray
) -> List[np.ndarray]:
    """
    Generate Bézier curve points.

    Args:
    - src (np.ndarray): The source point.
    - ctrl (List[float]): The control point.
    - dst (np.ndarray): The destination point.

    Returns:
    - List[np.ndarray]: The Bézier curve points.
    """
    curve = []
    for t in np.linspace(0, 1, num=100):
        curve_point = (
            np.outer((1 - t) ** 2, src)
            + 2 * np.outer((1 - t) * t, ctrl)
            + np.outer(t**2, dst)
        )
        curve.append(curve_point[0])
    return curve


def curved_edges(
    G: nx.Graph, pos: Dict[Any, Tuple[float, float]], dist: float = 0.2
) -> None:
    """
    Draw curved edges for nodes on the same level.

    Args:
    - G (Any): The graph object.
    - pos (Dict[Any, Tuple[float, float]]): Dictionary with node positions.
    - dist (float, optional): Distance for curvature. Defaults to 0.2.

    Returns:
    - None
    """
    ax = plt.gca()
    for u, v, data in G.edges(data=True):
        src = np.array(pos[u])
        dst = np.array(pos[v])

        same_level = abs(src[1] - dst[1]) < 0.01

        if same_level:
            control = [(src[0] + dst[0]) / 2, src[1] + dist]
            curve = bezier_curve(src, control, dst)
            arrow = patches.FancyArrowPatch(
                posA=curve[0],  # type: ignore
                posB=curve[-1],  # type: ignore
                connectionstyle=f"arc3,rad=0.2",
                color="gray",
                arrowstyle="-|>",
                mutation_scale=15.0,
                lw=1,
                shrinkA=10,
                shrinkB=10,
            )
            ax.add_patch(arrow)
        else:
            ax.annotate(
                "",
                xy=dst,
                xytext=src,
                arrowprops=dict(
                    arrowstyle="-|>", color="gray", lw=1, shrinkA=10, shrinkB=10
                ),
            )


def tree_layout(graph: nx.DiGraph, root_node: Any) -> Dict[Any, Tuple[float, float]]:
    """Compute positions as a tree layout centered on the root with alternating vertical shifts."""
    bfs_tree = nx.bfs_tree(graph, source=root_node)
    levels = {
        node: depth
        for node, depth in nx.single_source_shortest_path_length(
            bfs_tree, root_node
        ).items()
    }

    pos = {}
    max_depth = max(levels.values())
    level_positions = {i: 0 for i in range(max_depth + 1)}  # type: ignore

    # Count the number of nodes per level to compute the width
    level_count: Any = {}
    for node, level in levels.items():
        level_count[level] = level_count.get(level, 0) + 1

    vertical_offset = (
        0.07  # The amount of vertical shift per node within the same level
    )

    # Assign positions
    for node, level in sorted(levels.items(), key=lambda x: x[1]):
        total_nodes_in_level = level_count[level]
        horizontal_spacing = 1.0 / (total_nodes_in_level + 1)
        pos_x = (
            0.5
            - (total_nodes_in_level - 1) * horizontal_spacing / 2
            + level_positions[level] * horizontal_spacing
        )

        # Alternately shift nodes up and down within the same level
        pos_y = (
            -level
            + (level_positions[level] % 2) * vertical_offset
            - ((level_positions[level] + 1) % 2) * vertical_offset
        )
        pos[node] = (pos_x, pos_y)

        level_positions[level] += 1

    return pos


def graph_spring_layout(
    dag: nx.DiGraph, labels: Dict[Any, str], tree: bool = True
) -> None:
    num_nodes = len(dag.nodes())
    # Setting up the figure and axis
    fig, ax = plt.subplots()
    ax.axis("off")  # Turn off the axis

    base = 3.0

    if num_nodes > 10:
        base /= 1 + math.log(num_nodes)
        font_size = base * 10

    font_size = max(10, base * 10)
    node_size = max(300, base * 1000)

    if tree:
        root_node = [node for node, degree in dag.in_degree() if degree == 0][0]
        pos = tree_layout(dag, root_node)
    else:
        # Adjust k for the spring layout based on node count
        k_value = 3 / math.sqrt(num_nodes)

        pos = nx.spring_layout(dag, k=k_value, iterations=50)

    # Draw nodes and labels
    nx.draw_networkx_nodes(dag, pos, node_color="skyblue", node_size=int(node_size))
    nx.draw_networkx_labels(dag, pos, labels=labels, font_size=int(font_size))

    # Draw curved edges
    curved_edges(dag, pos)  # type: ignore

    plt.tight_layout()
    plt.show()


def rgb_to_hex(rgb: Tuple[float, float, float]) -> str:
    return "#{:02x}{:02x}{:02x}".format(
        int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)
    )


def get_category_colors(categories: Dict[Any, str]) -> Dict[str, str]:
    unique_categories = set(categories.values())
    colormap = plt.cm.get_cmap("tab10", len(unique_categories))  # type: ignore
    return {
        category: rgb_to_hex(colormap(i)[:3])
        for i, category in enumerate(unique_categories)
    }


def graph_interactive_network(
    dag: nx.DiGraph,
    labels: Dict[Any, Dict[str, Any]],
    html_graph_path: str = "",
) -> None:

    # now lets split
    # nx.
    #largest_components = sorted(nx.connected_components(dag), key=len, reverse=True)[:n]
    size = 10
    dag = dag.to_undirected()
    #largest_components = sorted(nx.strongly_connected_components(dag), key=len, reverse=True)[:size]
    largest_components = sorted(nx.connected_components(dag), key=len, reverse=True)[:size]
    for index in range(size):
        name= f'Component{index}'
        component=dag.subgraph(largest_components[index])
        nt = Network(notebook=True, width="100%", height="800px",
                     #directed=True
                     )
        for edge in component.edges():
            source_id_str = edge[0]
            target_id_str = edge[1]
            edge_id_str = (
                f"{source_id_str}_to_{target_id_str}"  # Construct a unique edge id
            )
            nt.add_node(source_id_str)
            nt.add_node(target_id_str)
            nt.add_edge(source_id_str, target_id_str, id=edge_id_str)
        hierarchical_options = {
            "enabled": True,
            #"levelSeparation": 200,  # Increased vertical spacing between levels
            #"nodeSpacing": 250,  # Increased spacing between nodes on the same level
            #"treeSpacing": 250,  # Increased spacing between different trees (for forest)
            "blockShifting": True,
           # "edgeMinimization": True,
            "parentCentralization": True,
            #"direction": "UD",
            "sortMethod": "directed",
        }
        physics_options = {
            "stabilization": {
                "enabled": True,
                "iterations": 1000,  # Default is often around 100
            },
            "hierarchicalRepulsion": {
                "centralGravity": 0.0,
                "springLength": 700,  # Increased edge length
                "springConstant": 0.01,
                "nodeDistance": 750,  # Increased minimum distance between nodes
                "damping": 0.09,
            },
            "solver": "hierarchicalRepulsion",
            "timestep": 0.5,
        }
        nt.options = {
            "nodes": {
                "font": {
                    "size": 12,  # Increased font size for labels
                    "color": "black",  # Set a readable font color
                },
                "shapeProperties": {"useBorderWithImage": True},
            },
            "edges": {
                "length": 1050,  # Increased edge length
            },
            "physics": physics_options,
            "layout": {"hierarchical": hierarchical_options},
        }
        graph_data = {"nodes": nt.nodes, "edges": nt.edges}
        json_graph = json.dumps(graph_data)
        with open(f"graphs/graph{name}.json", "w") as f:
            f.write(json_graph)
        nt.show(f"graphs/graph{name}.html")


@click.command()
@click.argument('infile', type=click.File('r'))
def main(infile):
    ind = csv.DictReader(infile)
    dag = networkx.DiGraph()
    for r in ind:
        #(caller,callee) =
        parts = r["name"].split("-")
        caller = parts[0]
        callee = parts[1]
        count = int(r["count"])
        #print(caller, callee, count)
        dag.add_edge(caller,callee, weight=count)
    #with input ",name,count"

    #dag.add_nodes_from(self.items)
    # for item in self.items:
    #     nodeid = clean_nodeid(item.nodeid)
    #     for dependency in self.dependencies[nodeid].dependencies:
    #         dag.add_edge(self.nodeid_to_item[dependency], item)

    labels = {}
    graph_interactive_network(dag, labels, html_graph_path="")
if __name__ == "__main__":
    main()
