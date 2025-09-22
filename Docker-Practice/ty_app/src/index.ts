import express from "express";

const app = express();
const PORT = process.env.PORT || 3000;
const APP_NAME = process.env.APP_NAME || "TS API Demo";

app.use(express.json());

app.get("/", (req, res) => {
  res.json({ message: "Welcome to TS API Demo!" });
});

app.get("/health", (req, res) => {
  res.json({ ok: true, service: APP_NAME });
});

app.get("/api/hello", (req, res) => {
  res.json({ message: "Hello from TypeScript + Express 🚀" });
});

app.post("/api/echo", (req, res) => {
  res.json({ you_sent: req.body });
});

app.listen(Number(PORT), "0.0.0.0", () => {
  console.log(`Server running on port ${PORT}`);
});