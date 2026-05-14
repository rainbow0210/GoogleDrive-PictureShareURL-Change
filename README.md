# Discord_PictureShareURL-Change

## Download
[Click](https://github.com/rainbow0210/PictureShareURL-Change/archive/refs/heads/main.zip)
## Table content

* [English](https://github.com/rainbow0210/PictureShareURL-Change/#English)
* [Japanese](https://github.com/rainbow0210/PictureShareURL-Change/#Japanese)

# English
## Expanation
The bot work discord.

Google drive picture share link change embeddable link. (Use example: html img tag)

## Operating Enviroment
* Python 3.10.10

* py-cord 2.4.0

* python-dotenv

## Command List
* `/change_url <share_url>`: Converts a Google Drive share link into an embeddable direct URL.

	Example (Discord slash command format):

```
/change_url share_url:https://drive.google.com/file/d/FILE_ID/view?usp=sharing
```

	Response: The converted URL is returned as an embed. Example:

```
http://drive.google.com/uc?export=view&id=FILE_ID
```

	Note: Unsupported links return an error response.

## How to use?
1. Install required packages:

```
pip install py-cord python-dotenv
```

2. Create a `.env` file in the project root with your bot token:

```
token=YOUR_BOT_TOKEN
```

3. Run the bot:

```
python bot.py
```

4. In Discord, use the slash command `/change_url` and paste a Google Drive share link to get a direct-download URL.

## LICENCE
MIT LICENCE↓

[https://github.com/rainbow0210/PictureShareURL-Change/blob/main/LICENSE](https://github.com/rainbow0210/PictureShareURL-Change/blob/main/LICENSE)

## Extension library and use data
Sorry, almost japanese site...

* Python:[https://www.python.org/](https://www.python.org/)

* Py-cord:[https://github.com/Pycord-Development/pycord](https://github.com/Pycord-Development/pycord)

* Python-dotenv:[https://pypi.org/project/python-dotenv/](https://pypi.org/project/python-dotenv/)

* 【Python】discord.pyが開発終了ということなのでpycordに乗り換えよう:[https://qiita.com/melonade/items/25c038e8e4e6800aa639](https://qiita.com/melonade/items/25c038e8e4e6800aa639)

* Google Drive に保存した画像を直接呼び出せるURLの取得:[https://qiita.com/codeDiver/items/0394968fa318d9309d33](https://qiita.com/codeDiver/items/0394968fa318d9309d33)

* pythonで環境ファイルを読み込む:[https://zenn.dev/nakashi94/articles/9c93b6a58acdb4](https://zenn.dev/nakashi94/articles/9c93b6a58acdb4)

* Pythonで先頭のn文字を削除する:[https://www.relief.jp/docs/python-remove-first-n-characters-from-string.html](https://www.relief.jp/docs/python-remove-first-n-characters-from-string.html)

* Pythonで末尾のn文字を削除する:[https://www.relief.jp/docs/python-remove-last-n-characters-from-string.html](https://www.relief.jp/docs/python-remove-last-n-characters-from-string.html)

* 【やってみた】Discordのスラッシュコマンド"/hoge"をpythonで自作してみる...!:[https://tektektech.com/discord-custom-slash-command/](https://tektektech.com/discord-custom-slash-command/)

* Discord Embed Generator:[https://cog-creators.github.io/discord-embed-sandbox/](https://cog-creators.github.io/discord-embed-sandbox/)


# Japanese
## 概要
Discord上で動作する、Googleドライブの画像ファイルの共有リンクを、htmlのimgタグ等に埋め込めるリンクに変換するbotです。

## 動作確認済み環境
* Python 3.10.10

* py-cord 2.4.0

* python-dotenv

## コマンド一覧
* `/change_url <share_url>`: Googleドライブの共有リンクを埋め込み可能な直接URLに変換します。

	例（Discordのスラッシュコマンド形式）:

```
/change_url share_url:https://drive.google.com/file/d/FILE_ID/view?usp=sharing
```

	返信: 変換後のURLが埋め込みで返されます（例）:

```
http://drive.google.com/uc?export=view&id=FILE_ID
```

	補足: 非対応のリンクの場合はエラー応答になります。

## 使い方
1. 必要パッケージのインストール:

```
pip install py-cord python-dotenv
```

2. プロジェクトルートに `.env` ファイルを作成し、Botのトークンを記述してください:

```
token=YOUR_BOT_TOKEN
```

3. Botを起動:

```
python bot.py
```

4. Discord内でスラッシュコマンド `/change_url` を実行し、Googleドライブの共有リンクを貼り付けるとダイレクトダウンロード用URLが得られます。

## ライセンス
MIT LICENCE↓

[https://github.com/rainbow0210/PictureShareURL-Change/blob/main/LICENSE](https://github.com/rainbow0210/PictureShareURL-Change/blob/main/LICENSE)

## 利用したもの、参考にしたサイト
* Python：[https://www.python.org/](https://www.python.org/)

* Py-cord：[https://github.com/Pycord-Development/pycord](https://github.com/Pycord-Development/pycord)

* Python-dotenv：[https://pypi.org/project/python-dotenv/](https://pypi.org/project/python-dotenv/)

* 【Python】discord.pyが開発終了ということなのでpycordに乗り換えよう：[https://qiita.com/melonade/items/25c038e8e4e6800aa639](https://qiita.com/melonade/items/25c038e8e4e6800aa639)

* Google Drive に保存した画像を直接呼び出せるURLの取得：[https://qiita.com/codeDiver/items/0394968fa318d9309d33](https://qiita.com/codeDiver/items/0394968fa318d9309d33)

* pythonで環境ファイルを読み込む：[https://zenn.dev/nakashi94/articles/9c93b6a58acdb4](https://zenn.dev/nakashi94/articles/9c93b6a58acdb4)

* Pythonで先頭のn文字を削除する：[https://www.relief.jp/docs/python-remove-first-n-characters-from-string.html](https://www.relief.jp/docs/python-remove-first-n-characters-from-string.html)

* Pythonで末尾のn文字を削除する：[https://www.relief.jp/docs/python-remove-last-n-characters-from-string.html](https://www.relief.jp/docs/python-remove-last-n-characters-from-string.html)

* 【やってみた】Discordのスラッシュコマンド"/hoge"をpythonで自作してみる...!：[https://tektektech.com/discord-custom-slash-command/](https://tektektech.com/discord-custom-slash-command/)

* Discord Embed Generator：[https://cog-creators.github.io/discord-embed-sandbox/](https://cog-creators.github.io/discord-embed-sandbox/)
