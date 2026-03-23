# バグ入りコードサンプル

このフォルダには、GitHub Copilot CLIを使ったコードレビューとデバッグの練習用に意図的にバグを含んだコードが入っています。

## フォルダ構成

```
buggy-code/
├── js/                    # JavaScriptサンプル
│   ├── userService.js     # ユーザー管理（8つのバグ）
│   └── paymentProcessor.js # 支払い処理（8つのバグ）
└── python/                # Pythonサンプル
    ├── user_service.py    # ユーザー管理（10個のバグ）
    └── payment_processor.py # 支払い処理（12個のバグ）
```

## クイックスタート

### JavaScript

```bash
copilot

# セキュリティ監査
> Review @samples/buggy-code/js/userService.js for security issues

# すべてのバグを見つける
> Find all bugs in @samples/buggy-code/js/paymentProcessor.js
```

### Python

```bash
copilot

# セキュリティ監査
> Review @samples/buggy-code/python/user_service.py for security issues

# すべてのバグを見つける
> Find all bugs in @samples/buggy-code/python/payment_processor.py
```

## バグのカテゴリ

### 両言語共通

| バグの種類 | 説明 |
|-----------|------|
| SQLインジェクション | ユーザー入力をSQLクエリに直接使用 |
| ハードコードされた秘密情報 | ソースコード内のAPIキーとパスワード |
| 競合状態 | 適切な同期なしの共有状態 |
| 機密データのログ記録 | ログ内のパスワードとカード番号 |
| 入力バリデーションの欠如 | ユーザー提供データのチェックなし |
| エラーハンドリングなし | try/catchまたはtry/exceptブロックの欠如 |
| 弱いパスワード比較 | プレーンテキストまたはタイミング脆弱な比較 |
| 認可チェックの欠如 | 認可検証なしの操作 |

### Python固有のバグ

| バグの種類 | 説明 |
|-----------|------|
| Pickleデシリアライゼーション | 信頼できないデータに対する`pickle.loads()` |
| eval()インジェクション | ユーザー入力を`eval()`に渡す |
| 安全でないYAML読み込み | セーフローダーなしの`yaml.load()` |
| シェルインジェクション | `os.system()`呼び出しでのユーザー入力 |
| 弱いハッシュ | パスワードハッシュにMD5を使用 |
| 安全でない乱数 | セキュリティ目的で`random`モジュールを使用 |

## 練習問題

1. **セキュリティ監査**：包括的なセキュリティレビューを実行し、重要度別にすべての脆弱性をリスト化する
2. **1つのバグを修正**：重大なバグを1つ選び、Copilotから修正を取得し、なぜそれが機能するか理解する
3. **テストを生成**：デプロイ前にこれらのバグを検出するテストを作成する
4. **安全にリファクタリング**：機能を維持しながらSQLインジェクションのバグを修正する
