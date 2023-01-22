from __future__ import annotations

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
) -> list[NotionContent] | None:
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
    arxiv_urls_dict = get_new_ak_arxiv_urls(client)

    if arxiv_urls_dict is None:
        return None

    model = AutoModelForSeq2SeqLM.from_pretrained("staka/fugumt-en-ja")
    tokenizer = AutoTokenizer.from_pretrained("staka/fugumt-en-ja")

    tokenizer.tgt_lang = "ja"
    tokenizer.src_lang = "en"

    contents = []
    for info, tweet_url in tqdm(
        zip(
            get_arxiv_abstracts(list(arxiv_urls_dict.keys())), arxiv_urls_dict.values()
        ),
        desc="Translating arxiv abstracts...",
        total=len(list(arxiv_urls_dict.keys())),
    ):
        inputs = tokenizer(info.summary, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=512)
        translated = tokenizer.batch_decode(outputs, skip_special_tokens=True)

        subprocess.run(
            ["node", "markdown_to_notion.js", translated[0], "./tmp.json"],
            stdout=subprocess.DEVNULL,
        )
        with open("./tmp.json", "r") as f:
            content_body = json.load(f)
        os.remove("./tmp.json")

        content_body.append(
            {
                "type": "embed",
                "embed": {
                    "caption": [],
                    "url": tweet_url,
                },
            }
        )

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


def get_arxiv_abstracts(arxiv_urls: list[str]) -> list[arxiv.Result] | None:
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


def get_new_ak_arxiv_urls(client: tweepy.Client) -> dict[str, str]:
    """Get new ak tweets and extract arxiv urls.

    Parameters
    ----------
    client : tweepy.Client
        tweepy client.

    Returns
    -------
    dict[str, str]
        dict of new arxiv urls and its original tweet urls.
    """
    tweets = client.get_users_tweets(
        id=2465283662,
        max_results=25,
        exclude=["retweets"],
    )

    arxiv_urls_dict = {}
    for tweet in tweets.data:
        urls = re.findall(
            "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
            tweet.text,
        )
        for url in urls:
            try:
                url = requests.get(url, timeout=(3.0, 7.5)).url
                if url.startswith("https://arxiv.org/"):
                    arxiv_urls_dict[url] = f"https://twitter.com/_akhaliq/status/{tweet.id}"
            except Exception as e:
                print(e)
                continue

    if os.path.exists("arxiv_urls.log"):
        with open("arxiv_urls.log", "r") as f:
            old_arxiv_urls = f.read().splitlines()
    else:
        old_arxiv_urls = []

    arxiv_urls = list(arxiv_urls_dict.keys()) if arxiv_urls_dict else None

    if arxiv_urls:
        with open("arxiv_urls.log", "w") as f:
            f.write("\n".join(arxiv_urls))

        new_arxiv_urls = set(arxiv_urls) - set(old_arxiv_urls)

        return {
            key: val for key, val in arxiv_urls_dict.items() if key in new_arxiv_urls
        }
    else:
        return None
