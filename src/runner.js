import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import apiModeProcessor from "./processors/api_mode.js";
import cheerioModeProcessor from "./processors/cheerio_mode.js";
import parseReview from "./parsers/review_parser.js";
import classifySentiment from "./parsers/sentiment_classifier.js";
import { normalizeText } from "./utils/normalize.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

async function main() {
const configPath = path.join(__dirname, "config", "settings.example.json");
const settings = JSON.parse(fs.readFileSync(configPath, "utf-8"));

const mode = process.argv[2] || "api"; // api | cheerio
const target = settings.target || "www.example.com";

let rawReviews = [];

console.log(`Running in ${mode} mode...`);

if (mode === "api") {
rawReviews = await apiModeProcessor(target, settings);
} else {
rawReviews = await cheerioModeProcessor(target, settings);
}

const parsed = rawReviews.map((r) => {
const review = parseReview(r);
review.sentiment = classifySentiment(normalizeText(review.text));
return review;
});

const outPath = path.join(__dirname, "..", "data", "output.json");
fs.writeFileSync(outPath, JSON.stringify(parsed, null, 2));

console.log(`Scraping complete. Saved ${parsed.length} reviews → data/output.json`);
}

main().catch((err) => {
console.error("Fatal error:", err);
process.exit(1);
});