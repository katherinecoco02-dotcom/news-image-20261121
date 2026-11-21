// Entry for the 21 November 2026 news image, Node 22, stdlib only.
//
// The six stories from Saturday 21 November 2026 are drawn as a
// newspaper front page in entry.png, which sits beside this file.
// This program copies that picture to the grader's output folder,
// so running it twice writes the same bytes both times. No network.
//
// Try it: mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
// The copy is byte-for-byte, so a second run writes identical bytes.

import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const targetDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(targetDir, { recursive: true });
const picture = new URL("./entry.png", import.meta.url);
copyFileSync(picture, join(targetDir, "entry.png"));
