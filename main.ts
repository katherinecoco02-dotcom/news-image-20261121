// News-image entry for 21 November 2026 (Node 22, standard library only).
// Entry: six verified stories from Saturday 21 November 2026, drawn as a
// newspaper front page. The picture lives in this repository as entry.png;
// this program just copies it to the output path the grader expects, so
// both runs of the program write exactly the same bytes. No network is used.
//
// Local test: mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
const source = new URL("./entry.png", import.meta.url);
copyFileSync(source, join(outDir, "entry.png"));
