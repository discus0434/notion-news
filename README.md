# notion-news

## Installation

1. このリポジトリを`clone`し、プロジェクトルート下に`.env`ファイルを作成

2. Notionで新しいデータベースをページで作成し、データベースのIDを`DATABASE_ID`として`.env`に記入する

3. Notionで[インテグレーション](https://www.notion.so/my-integrations)を作成してデータベースに`コネクト`し、インテグレーションのアクセストークンを`NOTION_ACCESS_TOKEN`として`.env`に記入する

4. Twitterで新しい[Development App](https://developer.twitter.com/en/portal/dashboard)を作成し、以下を`.env`に記入する
  `TWITTER_API_KEY`, `TWITTER_API_SECRET`: "API Key and Secret"で生成できるキー
  `TWITTER_BEARER_TOKEN`: "Bearer Token"で生成できるトークン
  `TWITTER_ACCESS_TOKEN`, `TWITTER_TOKEN_SECRET`: "Access Token and Secret"で生成できるトークン
 
5. 実行環境を作成する
  * Docker
    1. `docker build notion-news/. -t notion-news`
    2. `chmod +x ./docker_run.sh && ./docker_run.sh`
  * 素の環境
    1. `python -m venv venv`
    2. `source venv/bin/activate`
    3. `npm install`
    4. `automation.sh`の1行目のパスを、リポジトリをクローンした位置に書き換える
    5. `chmod +x ./automation.sh`
 
6. 任意のスケジューラに毎日`automation.sh`を実行させる
