import json
import os
import random
import re
import subprocess
from dataclasses import dataclass

import arxiv
import requests
import tweepy
from tqdm import tqdm
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


@dataclass
class NotionContent:
    title: str
    icon: str
    url: str
    tags: list[str]
    content_body: list[dict]


def make_arxiv_translated_abstracts(
    client: tweepy.Client, arxiv_categories: dict[str, str]
) -> list[NotionContent]:
    """Make notion contents from arxiv abstracts.

    Parameters
    ----------
    client : tweepy.Client
        twitter client.
    arxiv_categories : dict[str, str]
        correspondence between arxiv category and category's name.

    Returns
    -------
    list[NotionContent]
        list of notion contents.
    """
    arxiv_urls = get_new_ak_arxiv_urls(client)

    model = AutoModelForSeq2SeqLM.from_pretrained("staka/fugumt-en-ja")
    tokenizer = AutoTokenizer.from_pretrained("staka/fugumt-en-ja")

    tokenizer.tgt_lang = "ja"
    tokenizer.src_lang = "en"

    contents = []
    for info in tqdm(
        get_arxiv_abstracts(arxiv_urls),
        desc="Translating arxiv abstracts...",
        total=len(arxiv_urls),
    ):
        inputs = tokenizer(info.summary, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=1024)
        translated = tokenizer.batch_decode(outputs, skip_special_tokens=True)

        subprocess.run(
            ["node", "markdown_to_notion.js", translated[0], "./tmp.json"],
            stdout=subprocess.DEVNULL,
        )
        with open("./tmp.json", "r") as f:
            content_body = json.load(f)
        os.remove("./tmp.json")
        contents.append(
            NotionContent(
                title=info.title,
                icon=random.choice(
                    [
                        "📔",
                        "📕",
                        "📗",
                        "📘",
                        "📙",
                        "📚",
                        "📓",
                        "📒",
                        "📃",
                        "📜",
                        "📄",
                        "🗞️",
                        "📑",
                        "🔖",
                        "🏷️",
                        "📎",
                        "🖇️",
                        "📏",
                        "📐",
                        "✂️",
                        "🖊️",
                        "🖋️",
                        "✒️",
                        "🖌️",
                        "🖍️",
                        "📝",
                        "✏️",
                        "🔍",
                        "🔎",
                    ]
                ),
                tags=[
                    arxiv_categories[info.categories[i]]
                    for i in range(len(info.categories))
                ],
                url=info.entry_id,
                content_body=content_body,
            )
        )

    return contents


def get_arxiv_abstracts(arxiv_urls: list[str]) -> list[arxiv.Result]:
    """Get arxiv abstracts.

    Parameters
    ----------
    arxiv_urls : list[str]
        list of arxiv urls.

    Returns
    -------
    yield[arxiv.Result]
        arxiv abstracts.
    """
    arxiv_ids = list(map(lambda url: url.split("/")[-1], arxiv_urls))
    for res in arxiv.Search(id_list=arxiv_ids).results():
        yield res


def get_new_ak_arxiv_urls(client: tweepy.Client) -> list[str]:
    """Get new ak tweets and extract arxiv urls.

    Parameters
    ----------
    client : tweepy.Client
        tweepy client.

    Returns
    -------
    list[tweepy.Tweet]
        list of tweets.
    """
    tweets = client.get_users_tweets(
        id=2465283662,
        max_results=20,
        exclude=["retweets"],
    )

    arxiv_urls = []
    for tweet in tweets.data:
        urls = re.findall(
            "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
            tweet.text,
        )
        for url in urls:
            try:
                url = requests.get(url).url
            except TimeoutError:
                continue
            if url.startswith("https://arxiv.org/"):
                arxiv_urls.append(url)

    with open("arxiv_urls.log", "r") as f:
        old_arxiv_urls = f.read().splitlines()

    with open("arxiv_urls.log", "w") as f:
        f.write("\n".join(arxiv_urls))

    new_arxiv_urls = set(arxiv_urls) - set(old_arxiv_urls)

    return list(new_arxiv_urls)
