import argparse
import os

from atlas.pipeline import AtlasPipeline

from dotenv import load_dotenv

def main():

    parser = argparse.ArgumentParser(
        prog="atlas",
        description="ATLAS Literature Processing Pipeline"
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    process_parser = subparsers.add_parser(
        "process",
        help="Process a directory of papers"
    )

    process_parser.add_argument(
        "papers_dir",
        help="Directory containing .txt papers"
    )

    process_parser.add_argument(
        "--output-dir",
        default="data/graphs",
        help="Output directory for GraphML files"
    )

    args = parser.parse_args()

    load_dotenv(override=True)

    api_key = os.getenv(
        "MISTRAL_API_KEY"
    )

    if api_key is None:

        raise ValueError(
            "MISTRAL_API_KEY environment variable is not set."
        )

    pipeline = AtlasPipeline(
        api_key=api_key
    )

    if args.command == "process":

        pipeline.process_directory(
            papers_dir=args.papers_dir,
            output_dir=args.output_dir
        )


if __name__ == "__main__":

    main()