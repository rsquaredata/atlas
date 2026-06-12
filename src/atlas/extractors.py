from mistralai import Mistral

from atlas.schemas import (
    Entity,
    Relationship,
    ExtractionResult
)

import json


class MistralExtractor:

    def __init__(
        self,
        api_key: str,
        model: str = "mistral-small-latest"
    ):
        self.model = model

        self.client = Mistral(
            api_key=api_key
        )

    def extract(
        self,
        text: str
    ) -> ExtractionResult:

        prompt = f"""
You are an information extraction system specialized in scientific literature.

Extract ONLY meaningful scientific entities and relationships.

Allowed entity types:

- Paper
- Method
- Framework
- Model
- Dataset
- Benchmark
- ResearchTask
- Agent
- Metric
- Organization
- ScientificConcept

ScientificConcept examples:

- Feature Engineering
- Data Cleaning
- Debugging
- Human-in-the-loop
- Multi-Agent System
- Experiment Tracking
- Workflow Orchestration
- Tree Search
- Code Optimization
- Automated Experimentation
- Knowledge Graph
- Reasoning
- Agent Workflow

Good examples:
- AutoKaggle
- MLE-Bench
- Databricks
- MLflow
- AIDE
- GPT-4
- Tree Search
- Code Optimization
- Knowledge Graph
- Automated Experimentation

An entity must be either:

- a named scientific artifact (paper, benchmark, framework, model, dataset, organization)

or

- a central technical concept explicitly discussed in the paper.

Do NOT extract:

- generic concepts
- adjectives
- benefits
- outcomes
- vague business terms
- generic nouns

Examples of entities to ignore:

- productivity
- effectiveness
- practicality
- users

Keep only entities that would be useful in a scientific knowledge graph.

Do not extract generic business outcomes.
Technical concepts, algorithms, optimization strategies, reasoning techniques, search methods and scientific workflows
are valid entities if they are central to the paper.

Favor precision, but do not omit central technical concepts.

Extract relationships using concise technical verbs.

Prefer:

- uses
- evaluates
- automates
- implements
- orchestrates
- integrates
- extends
- benchmarks
- generates

Avoid vague relations such as:

- comprises
- includes
- contains
- consists_of

unless no better relation exists.

Return ONLY valid JSON.

Schema:

{{
  "entities": [
    {{
      "name": "...",
      "type": "..."
    }}
  ],
  "relationships": [
    {{
      "source": "...",
      "relation": "...",
      "target": "..."
    }}
  ]
}}

Text:

{text}
"""

        response = self.client.chat.complete(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        raw_json = response.choices[0].message.content

        clean_json = (
            raw_json
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        data = json.loads(clean_json)

        entities = [
            Entity(**entity)
            for entity in data["entities"]
        ]

        relationships = [
            Relationship(**relationship)
            for relationship in data["relationships"]
        ]

        return ExtractionResult(
            entities=entities,
            relationships=relationships
        )