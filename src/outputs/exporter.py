import json
from pathlib import Path
import logging

class Exporter:
    @staticmethod
    def export(reviews):
        out_path = Path(__file__).resolve().parents[2] / "data" / "sample_output.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(reviews, f, indent=2)
        logging.info(f"Exported {len(reviews)} reviews → data/sample_output.json")