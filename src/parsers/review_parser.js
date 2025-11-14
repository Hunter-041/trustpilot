export default function parseReview(raw) {
  return {
    id: raw.id ?? null,
    title: raw.title ?? "",
    text: raw.text ?? "",
    rating: raw.rating ?? 0,
    consumer: raw.consumer || {},
    dates: raw.dates || {},
    source: raw.source || "unknown"
  };
}