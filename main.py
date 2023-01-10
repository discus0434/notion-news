import tweepy
from notion_client import Client

from config import (
    ARXIV_CATEGORIES,
    DATABASE_ID,
    NOTION_ACCESS_TOKEN,
    TWITTER_ACCESS_TOKEN,
    TWITTER_API_KEY,
    TWITTER_API_SECRET,
    TWITTER_BEARER_TOKEN,
    TWITTER_TOKEN_SECRET,
)
from lib import (
    make_arxiv_translated_abstracts,
    make_weather_forecast,
    post_to_notion,
    remove_all_blocks_in_database,
)


def main():
    notion_client = Client(auth=NOTION_ACCESS_TOKEN)
    twitter_client = tweepy.Client(
        consumer_key=TWITTER_API_KEY,
        consumer_secret=TWITTER_API_SECRET,
        access_token=TWITTER_ACCESS_TOKEN,
        access_token_secret=TWITTER_TOKEN_SECRET,
        bearer_token=TWITTER_BEARER_TOKEN,
    )

    remove_all_blocks_in_database(client=notion_client, database_id=DATABASE_ID)

    weather_content = make_weather_forecast()
    arxiv_contents = make_arxiv_translated_abstracts(
        client=twitter_client, arxiv_categories=ARXIV_CATEGORIES
    )

    contents = [weather_content] + arxiv_contents

    post_to_notion(
        client=notion_client,
        database_id=DATABASE_ID,
        contents=contents,
    )


if __name__ == "__main__":
    main()
