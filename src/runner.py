import json
import logging
from pathlib import Path

from processors.api_processor import APIProcessor
from processors.cheerio_processor import CheerioProcessor
from extractors.review_parser import ReviewParser
from extractors.sentiment_analyzer import SentimentAnalyzer
from outputs.exporter import Exporter

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def load_input():
    path = Path(__file__).resolve().parents[1] / "data" / "input.sample.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    config = load_input()

    domain = config.get("domain")
    mode = config.get("mode", "api")

    if not domain:
        raise ValueError("Missing domain in input.sample.json")

    logging.info(f"Running Trustpilot scraper for domain: {domain} (mode={mode})")

    if mode == "api":
        processor = APIProcessor()
    else:
        processor = CheerioProcessor()

    raw_reviews = processor.fetch_reviews(domain)

    parser = ReviewParser()
    analyzer = SentimentAnalyzer()

    parsed_reviews = []
    for r in raw_reviews:
        parsed = parser.parse_review(r)
        parsed["sentiment"] = analyzer.classify(parsed["text"])
        parsed_reviews.append(parsed)

    Exporter.export(parsed_reviews)

    logging.info("Scraping completed successfully.")

if __name__ == "__main__":
    main()