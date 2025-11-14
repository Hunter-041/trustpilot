onst positiveWords = ["great", "awesome", "amazing", "good", "love"];
const negativeWords = ["bad", "terrible", "poor", "awful", "hate"];

export default function classifySentiment(text) {
  const t = text.toLowerCase();

  let score = 0;
  positiveWords.forEach((w) => (t.includes(w) ? score++ : null));
  negativeWords.forEach((w) => (t.includes(w) ? score-- : null));

  if (score > 0) return "positive";
  if (score < 0) return "negative";
  return "neutral";
}