ABBREVIATIONS = {
    "LLM": "Large Language Model",
    "LLMs": "Large Language Models",
    "SWE-BENCH": "SWE-bench"
}


def normalize_concept(
    concept: str
) -> str:

    concept = concept.strip()

    return ABBREVIATIONS.get(
        concept,
        concept
    )