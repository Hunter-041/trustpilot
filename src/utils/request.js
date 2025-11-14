import axios from "axios";

export async function get(url, headers = {}) {
try {
const res = await axios.get(url, { headers });
return res.data;
} catch (err) {
console.error("Request error:", err.message);
throw err;
}
}

export async function post(url, body = {}, headers = {}) {
try {
const res = await axios.post(url, body, { headers });
return res.data;
} catch (err) {
console.error("Request error:", err.message);
throw err;
}
}