# Book App - バグ入りバージョン

このディレクトリには、チャプター03のデバッグ演習用に意図的にバグを含んだ書籍コレクションアプリが含まれています。

**これらのバグを直接修正しないでください。** 学習者がGitHub Copilot CLIを使って問題を特定しデバッグする練習をするために存在しています。

---

## 意図的なバグ

### books_buggy.py

| # | バグ | 症状 |
|---|------|------|
| 1 | `find_book_by_title()` が完全一致を使用 | "the hobbit"で検索しても"The Hobbit"が存在するにもかかわらず何も返さない |
| 2 | `save_books()` がコンテキストマネージャーを使用していない | ファイルハンドルリーク、権限問題のエラーハンドリングなし |
| 3 | `add_book()` に年のバリデーションがない | 負の年、0年、遠い未来の年を受け入れる |
| 4 | `remove_book()` が `in` 部分文字列チェックを使用 | "Dune"を削除すると"Dune Messiah"も一致して削除される |
| 5 | `mark_as_read()` がすべての本を既読にする | ループ変数のバグ - 一致したものだけでなくすべての本を反復処理する |
| 6 | `find_by_author()` が完全一致を要求 | "Tolkien"では"J.R.R. Tolkien"が見つからない（部分一致なし） |

### book_app_buggy.py

| # | バグ | 症状 |
|---|------|------|
| 7 | `show_books()` の番号が0から始まる | 本が"0. ..."、"1. ..."と表示される（"1. ..."、"2. ..."ではなく） |
| 8 | `handle_add()` が空のタイトル/著者を受け入れる | 空白のタイトルと著者で本を追加できる |
| 9 | `handle_remove()` が常に成功を表示 | 本が見つからなくても"Book removed"と表示する |

---

## チャプター03での使い方

```bash
copilot

> @samples/book-app-buggy/books_buggy.py Users report that searching for
> "The Hobbit" returns no results even though it's in the data. Debug why.

> @samples/book-app-buggy/book_app_buggy.py When I remove a book that
> doesn't exist, the app says it was removed. Help me find why.
```
