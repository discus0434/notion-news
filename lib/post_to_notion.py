from notion_client import Client
from tqdm import tqdm

from lib import NotionContent


def post_to_notion(
    client: Client, database_id: str, contents: list[NotionContent]
) -> None:
    """Post content to Notion.

    Parameters
    ----------
    client : Client
        notion client.
    database_id : str
        database id of the notion. this is given by environment variable.
    contents : list[NotionContent]
        list of contents to post to notion.
    """

    for content in tqdm(contents):
        db = client.pages.create(
            **{
                "parent": {
                    "type": "database_id",
                    "database_id": database_id,
                },
                "icon": {"emoji": content.icon},
                "properties": {
                    "Name": {"title": [{"text": {"content": content.title}}]},
                    "Tags": {"multi_select": [{"name": tag} for tag in content.tags]},
                    "URL": {"url": content.url},
                },
            }
        )

        for block in tqdm(
            content.content_body,
            total=len(content.content_body),
            desc="Uploading blocks to notion...",
        ):
            client.blocks.children.append(block_id=db["id"], children=[block])
