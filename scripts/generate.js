/**
 * generate.js
 * Reads templates/README.template.md, injects dynamic values
 * (currently just a "last updated" timestamp — the LeetCode/GitHub
 * stats cards are already dynamic because they're hosted image APIs
 * that refresh on every page view, so no fetching is needed for those).
 *
 * Output is written to output/README.md, which the workflow then
 * pushes to the Avnish-kaushik/Avnish-kaushik profile repo.
 */

const fs = require("fs");
const path = require("path");

const TEMPLATE_PATH = path.join(__dirname, "..", "templates", "README.template.md");
const OUTPUT_DIR = path.join(__dirname, "..", "output");
const OUTPUT_PATH = path.join(OUTPUT_DIR, "README.md");

function formatTimestamp() {
  const now = new Date();
  // IST (UTC+5:30) since that's your timezone
  const istOffsetMs = 5.5 * 60 * 60 * 1000;
  const ist = new Date(now.getTime() + istOffsetMs);
  return ist.toISOString().replace("T", " ").slice(0, 16) + " UTC+5:30";
}

function main() {
  if (!fs.existsSync(TEMPLATE_PATH)) {
    console.error(`Template not found at ${TEMPLATE_PATH}`);
    process.exit(1);
  }

  let content = fs.readFileSync(TEMPLATE_PATH, "utf8");

  content = content.replace("{{LAST_UPDATED}}", formatTimestamp());

  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  }

  fs.writeFileSync(OUTPUT_PATH, content, "utf8");
  console.log(`README generated at ${OUTPUT_PATH}`);
}

main();
