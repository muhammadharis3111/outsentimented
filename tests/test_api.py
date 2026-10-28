from outsentimented import FinancialSentimentClassifier, SentimentPrediction


class ExampleClassifier:
    def __call__(self, sentence: str) -> SentimentPrediction:
        return {"label": "neutral", "confidence": 1.0}


def test_classifier_contract() -> None:
    classifier: FinancialSentimentClassifier = ExampleClassifier()
    prediction = classifier("The company released its annual report.")
    assert prediction == {"label": "neutral", "confidence": 1.0}

