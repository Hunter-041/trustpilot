import logging

class ReviewParser:
    """
    Ensures normalized review structure.
    """

    def parse_review(self, raw):
        logging.debug(f"Parsing review {raw.get('id')}")

        return {
            "id": raw.get("id"),
            "title": raw.get("title", "").strip(),
            "text": raw.get("text", "").strip(),
            "rating": raw.get("rating", 0),
            "link": "",
            "consumer": {},
            "reply": None,
            "dates": {},
        }