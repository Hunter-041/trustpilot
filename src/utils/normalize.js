export function normalizeText(str) {
  return (str || "")
    .replace(/\s+/g, " ")
    .trim()
    .toLowerCase();
}