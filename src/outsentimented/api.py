from typing import Literal, Protocol, TypedDict

SentimentLabel = Literal["positive", "neutral", "negative"]


class SentimentPrediction(TypedDict):
    label: SentimentLabel
    confidence: float


class FinancialSentimentClassifier(Protocol):
    def __call__(self, sentence: str) -> SentimentPrediction: ...

