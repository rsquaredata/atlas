from google.colab import userdata
from mistralai import Mistral

from atlas.schemas import (
    Entity,
    Relationship,
    ExtractionResult
)

import json


class MistralExtractor:

    def __init__(self):

        api_key = userdata.get("MISTRAL_API_KEY")

        self.client = Mistral(
            api_key=api_key
        )

    def extract(self, text: str) -> ExtractionResult:

        prompt = f"""
Extract entities and relationships from the following text.

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
            model="mistral-small-latest",
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
