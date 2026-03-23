# サンプルソースコード（レガシー - オプション参考資料）

> **注意**: このコースの主要サンプルは`../book-app-project/`の**Python書籍コレクションアプリ**です。これらのJS/Reactファイルはコースの以前のバージョンからのもので、JSの例を求める学習者のためのオプションの追加参考資料として保持されています。

このフォルダにはサンプルソースファイルが含まれています。これらはサンプルのみであり、完全に動作するアプリケーションを意図していません。

## 構造

```
src/
├── api/           # APIルートハンドラー
│   ├── auth.js    # 認証エンドポイント
│   └── users.js   # ユーザーCRUDエンドポイント
├── auth/          # クライアントサイド認証ハンドラー
│   ├── login.js   # ログインフォームロジック
│   └── register.js # 登録フォームロジック
├── components/    # Reactコンポーネント
│   ├── Button.jsx # 再利用可能なボタン
│   └── Header.jsx # ナビ付きアプリヘッダー
├── models/        # データモデル
│   └── User.js    # Userモデル
├── services/      # ビジネスロジック
│   ├── productService.js
│   └── userService.js
├── utils/         # ヘルパー関数
│   └── helpers.js
├── index.js       # アプリエントリーポイント
└── refactor-me.js # 初心者リファクタリング練習（チャプター03）
```

## 使い方

これらのファイルはコース例で`@`構文を使って参照されます：

```bash
copilot

> Explain what @samples/src/utils/helpers.js does
> Review @samples/src/api/ for security issues
> Compare @samples/src/auth/login.js and @samples/src/auth/register.js
```

## リファクタリング練習

`refactor-me.js`ファイルはチャプター03のリファクタリング演習用に特別に設計されています：

```bash
copilot

> @samples/src/refactor-me.js Rename the variable 'x' to something more descriptive
> @samples/src/refactor-me.js This function is too long. Split it into smaller functions.
> @samples/src/refactor-me.js Remove any unused variables
```

## 注意

- ファイルにはCopilotがレビュー中に見つけるための意図的なTODOと軽微な問題が含まれている
- これはデモコードで、実際に実行するようには設計されていない。本番環境用ではない
- `@`ファイル参照構文の学習に使用
