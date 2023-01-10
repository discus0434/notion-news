import fs from "fs";
import matter from "gray-matter";
import { markdownToBlocks } from "@tryfabric/martian";

const markdown = process.argv[2];

// parse the article content with gray-matter
const matterResult = matter(markdown);
// convert the article content to Notion blocks
const blocks = markdownToBlocks(matterResult.content, {
  strictImageUrls: false,
});

// write the article content, markdown and blocks to a file
fs.writeFileSync(process.argv[3], JSON.stringify(blocks));
