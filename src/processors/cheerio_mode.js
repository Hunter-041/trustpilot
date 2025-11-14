import axios from "axios";
import cheerio from "cheerio";

export default async function cheerioModeProcessor(domain, settings) {
console.log("Fetching HTML page and scraping (mock)...");

// Mock HTML content
const html = `
<html>
<body>
<div class="review">
<h2>Great product!</h2>
<p>Amazing quality and fast shipping.</p>
</div>
<div class="review">
<h2>Not bad</h2>
<p>Decent service, could be better.</p>
</div>
</body>
</html>
`;

const $ = cheerio.load(html);
const reviews = [];

$(".review").each((i, el) => {
const title = $(el).find("h2").text();
const text = $(el).find("p").text();

reviews.push({
id: `cheerio_${i}`,
title,
text,
rating: 4,
consumer: { name: "HTML User" },
dates: { published: new Date().toISOString() }
});
});

return reviews;
}