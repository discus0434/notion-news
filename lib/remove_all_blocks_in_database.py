from notion_client import Client


def remove_all_blocks_in_database(client: Client, database_id: str) -> None:
    """Remove all blocks in database.

    Parameters
    ----------
    client : Client
        notion client.
    database_id : str
        database id.
    """
    blocks = client.databases.query(**{"database_id": database_id})

    for page in blocks["results"]:
        client.blocks.delete(**{"block_id": page["id"]})
