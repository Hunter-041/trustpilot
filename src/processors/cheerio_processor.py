import logging
import requests
from bs4 import BeautifulSoup

class CheerioProcessor:
    """
    HTML-based processor using BeautifulSoup.
    """

    BASE_URL = "https://www.trustpilot.com/review/"

    def fetch_reviews(self, domain: str):
        logging.info(f"[Cheerio] Scraping Trustpilot HTML for {domain}")

        url = f"{self.BASE_URL}{domain}"
        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        reviews = []
        cards = soup.select("[data-review-id]")

        for card in cards[:5]:  # limit sample for demo
            review_id = card.get("data-review-id")
            title_el = card.select_one("h2")
            text_el = card.select_one("p")
            rating_el = card.select_one("[data-service-review-rating]")

            reviews.append(
                {
                    "id": review_id,
                    "title": title_el.get_text(strip=True) if title_el else "",
                    "text": text_el.get_text(strip=True) if text_el else "",
                    "rating": int(rating_el["data-service-review-rating"]) if rating_el else 0,
                }
            )

        return reviews