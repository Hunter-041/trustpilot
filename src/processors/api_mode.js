import axios from "axios";

export default async function apiModeProcessor(domain, settings) {
console.log("Fetching reviews from Trustpilot API mock...");

// Mock API response for runnable demonstration
const limit = settings.limit || 5;

const reviews = [];
for (let i = 0; i < limit; i++) {
reviews.push({
id: `api_${i}`,
title: `API Review ${i}`,
text: `This is a sample API-based review ${i} for ${domain}.`,
rating: Math.floor(Math.random() * 5) + 1,
consumer: { name: "API User" },
dates: { published: new Date().toISOString() }
});
}

return reviews;
}