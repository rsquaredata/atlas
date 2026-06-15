import networkx as nx

from atlas.schemas import ExtractionResult


class GraphBuilder:

    def build(
        self,
        result: ExtractionResult
    ) -> nx.DiGraph:

        graph = nx.DiGraph()

        for entity in result.entities:

            graph.add_node(
                entity.name,
                entity_type=entity.type
            )

        for relationship in result.relationships:

            graph.add_edge(
                relationship.source,
                relationship.target,
                relation=relationship.relation
            )

        return graph
    
    def save_graphml(
            self,
            graph,
            path: str
    ):
        nx.write_graphml(
            graph,
            path
        )