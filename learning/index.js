import init from "./pkg/learning.js";

async function main() {
  await init();
}

main().catch((error) => {
  console.error("Failed to initialize wasm app:", error);
});
