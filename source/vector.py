class Vector:
    def __init__(self) -> None:
        pass

    @staticmethod
    def scalar_product(question_tf_idf: dict[str, float], document_tf_idf: dict[str, float]) -> float:
        result = 0
        for word in document_tf_idf:
            result += document_tf_idf[word] * question_tf_idf[word]

        return result

    @staticmethod
    def norm(vector: dict[str, float]) -> float:
        result = 0
        for word in vector:
            result += vector[word] ** 2
        return result ** 0.5

    def similarity(self, question_tf_idf: dict[str, float], document_tf_idf: dict[str, float]) -> float:
        score = self.scalar_product(document_tf_idf, question_tf_idf) / (
                self.norm(document_tf_idf) * self.norm(question_tf_idf))
        return score
