# Book Collection App

*（このREADMEは意図的に粗削りです。GitHub Copilot CLIで改善してみましょう）*

読みたい本や持っている本を管理するJavaScriptアプリです。
本の追加、削除、一覧表示ができます。また、既読マークも付けられます。

---

## 現在の機能

* JSONファイルから本を読み込む（データベースとして使用）
* 一部のエリアで入力チェックが弱い
* テストは存在するが、おそらく十分ではない

---

## ファイル

* `book_app.js` - メインCLIエントリーポイント
* `books.js` - BookCollectionクラス（データロジック）
* `utils.js` - UI・入力用ヘルパー関数
* `data.json` - サンプル書籍データ
* `tests/test_books.js` - Nodeの組み込みテストランナーを使った初期テスト

---

## アプリの実行

```bash
node book_app.js list
node book_app.js add
node book_app.js find
node book_app.js remove
node book_app.js help
```

## テストの実行

```bash
npm test
```

---

## 注意

* 本番環境用ではない（当然ながら）
* コードの改善の余地がある
* 後でコマンドを追加できる
