lass SentimentAnalyzer:
    """
    Basic sentiment classifier using keyword heuristics.
    """

    def classify(self, text: str):
        lowered = text.lower()
        positive_words = ["great", "good", "excellent", "awesome", "love", "fast"]
        negative_words = ["bad", "terrible", "slow", "broke", "awful"]

        if any(w in lowered for w in positive_words):
            return "Positive"
        if any(w in lowered for w in negative_words):
            return "Negative"
        return "Neutral"