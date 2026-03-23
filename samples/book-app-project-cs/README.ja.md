# Book Collection App

*（このREADMEは意図的に粗削りです。GitHub Copilot CLIで改善してみましょう）*

読みたい本や持っている本を管理するC#コンソールアプリです。
本の追加、削除、一覧表示ができます。また、既読マークも付けられます。

---

## 現在の機能

* JSONファイルから本を読み込む（データベースとして使用）
* 一部のエリアで入力チェックが弱い
* テストは存在するが、おそらく十分ではない

---

## ファイル

* `Program.cs` - メインCLIエントリーポイント
* `Models/Book.cs` - Bookモデルクラス
* `Services/BookCollection.cs` - BookCollectionクラス（データロジック）
* `data.json` - サンプル書籍データ
* `Tests/BookCollectionTests.cs` - xUnitテスト

---

## アプリの実行

```bash
dotnet run -- list
dotnet run -- add
dotnet run -- find
dotnet run -- remove
dotnet run -- help
```

## テストの実行

```bash
cd Tests
dotnet test
```

---

## 注意

* 本番環境用ではない（当然ながら）
* コードの改善の余地がある
* 後でコマンドを追加できる
