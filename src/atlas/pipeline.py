from pathlib import Path

from atlas.io import load_text
from atlas.extractors import MistralExtractor
from atlas.graph_builder import GraphBuilder


class AtlasPipeline:

    def __init__(
        self,
        api_key: str
    ):

        self.extractor = MistralExtractor(
            api_key=api_key
        )

        self.builder = GraphBuilder()

    def process_paper(
        self,
        paper_path: str,
        output_dir: str = "data/graphs"
    ):

        paper_file = Path(
            paper_path
        )

        paper_name = paper_file.stem

        text = load_text(
            str(paper_file)
        )

        result = self.extractor.extract(
            text
        )

        print(f"Extracted {len(result.entities)} entities")
        
        print(f"Extracted {len(result.relationships)} relationships")

        graph = self.builder.build(
            result
        )

        output_path = (
            Path(output_dir)
            / f"{paper_name}.graphml"
        )

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.builder.save_graphml(
            graph,
            str(output_path)
        )

        print(
            f"Saved {output_path}"
        )

        return graph

    def process_directory(
        self,
        papers_dir: str,
        output_dir: str = "data/graphs"
    ):

        papers_path = Path(
            papers_dir
        )

        for paper_file in papers_path.glob(
            "*.txt"
        ):

            print(
                f"Processing {paper_file.name}"
            )

            self.process_paper(
                paper_path=str(paper_file),
                output_dir=output_dir
            )