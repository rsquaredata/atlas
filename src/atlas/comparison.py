import networkx as nx
from rapidfuzz import fuzz
from atlas.embeddings import EmbeddingModel


def common_nodes(
    graph_a: nx.Graph,
    graph_b: nx.Graph
):
    return set(graph_a.nodes()) & set(graph_b.nodes())


def fuzzy_common_nodes(
    graph_a: nx.Graph,
    graph_b: nx.Graph,
    threshold: int = 70
):
    matches = []

    nodes_a = list(graph_a.nodes())
    nodes_b = list(graph_b.nodes())

    for node_a in nodes_a:

        for node_b in nodes_b:

            score = fuzz.token_sort_ratio(
                node_a.lower(),
                node_b.lower()
            )

            if score >= threshold:

                matches.append(
                    (
                        node_a,
                        node_b,
                        score
                    )
                )

    return sorted(
        matches,
        key=lambda x: x[2],
        reverse=True
    )

def semantic_common_nodes(
    graph_a,
    graph_b,
    threshold=0.55
):

    model = EmbeddingModel()

    matches = []

    for node_a in graph_a.nodes():

        for node_b in graph_b.nodes():

            score = model.similarity(
                node_a,
                node_b
            )

            if score >= threshold:

                matches.append(
                    (
                        node_a,
                        node_b,
                        score
                    )
                )

    return sorted(
        matches,
        key=lambda x: x[2],
        reverse=True
    )