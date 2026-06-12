from sentence_transformers import SentenceTransformer

from sklearn.metrics.pairwise import cosine_similarity


class EmbeddingModel:

    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2"
    ):
        self.model = SentenceTransformer(
            model_name
        )

    def encode(
        self,
        texts: list[str]
    ):
        return self.model.encode(
            texts,
            convert_to_numpy=True
        )
    
    def similarity(
            self,
            text_a: str,
            text_b: str
    ):
        vectors = self.encode([text_a, text_b])

        return cosine_similarity(
            [vectors[0]],
            [vectors[1]]
        )[0][0]
    