# Book Collection App

*（このREADMEは意図的に粗削りです。GitHub Copilot CLIで改善してみましょう）*

読みたい本や持っている本を管理するPythonアプリです。
本の追加、削除、一覧表示ができます。また、既読マークも付けられます。

---

## 現在の機能

* JSONファイルから本を読み込む（データベースとして使用）
* 一部のエリアで入力チェックが弱い
* テストは存在するが、おそらく十分ではない

---

## ファイル

* `book_app.py` - メインCLIエントリーポイント
* `books.py` - BookCollectionクラス（データロジック）
* `utils.py` - UI・入力用ヘルパー関数
* `data.json` - サンプル書籍データ
* `tests/test_books.py` - 初期pytestテスト

---

## アプリの実行

```bash
python book_app.py list
python book_app.py add
python book_app.py find
python book_app.py remove
python book_app.py help
```

## テストの実行

```bash
python -m pytest tests/
```

---

## 注意

* 本番環境用ではない（当然ながら）
* コードの改善の余地がある
* 後でコマンドを追加できる
