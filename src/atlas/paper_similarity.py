from atlas.comparison import (
    semantic_common_nodes
)


def paper_similarity(
    graph_a,
    graph_b
):
    matches = semantic_common_nodes(
        graph_a,
        graph_b
    )

    if not matches:
        return {
            "num_matches": 0,
            "avg_score": 0.0,
            "max_score": 0.0
        }

    scores = [
        match[2]
        for match in matches
    ]

    return {
        "num_matches": len(matches),
        "avg_score": sum(scores) / len(scores),
        "max_score": max(scores)
    }