import logging
import time
import random

class APIProcessor:
    """
    Simulated API processor.
    In a real implementation, this would call internal endpoints or Trustpilot APIs.
    """

    def fetch_reviews(self, domain: str):
        logging.info(f"[API] Fetching reviews for {domain}")
        time.sleep(0.6)

        # Mocked review set
        fake_reviews = [
            {
                "id": "rev_api_1",
                "title": "Great service",
                "text": "Loved the fast delivery!",
                "rating": 5,
            },
            {
                "id": "rev_api_2",
                "title": "Bad quality",
                "text": "Product broke after a week.",
                "rating": 1,
            },
        ]

        random.shuffle(fake_reviews)
        return fake_reviews