![Chapter 06: MCP Servers](images/chapter-header.png)

> **もし Copilot がターミナルから GitHub の Issue を読んだり、データベースを確認したり、PR を作成したりできたら？**

これまで Copilot は、`@` で参照したファイル、会話の履歴、そして自身の学習データなど、直接渡された情報のみを扱えました。しかし、もし Copilot が自発的に GitHub リポジトリを確認したり、プロジェクトファイルを閲覧したり、ライブラリの最新ドキュメントを調べたりできたらどうでしょう？

それを実現するのが MCP（Model Context Protocol）です。MCP は Copilot を外部サービスに接続し、リアルタイムの実データにアクセスできるようにする仕組みです。Copilot が接続する各サービスは「MCP サーバー」と呼ばれます。この章では、いくつかの接続を設定し、Copilot が劇的に便利になる様子を体験します。

> 💡 **MCP をすでにご存知ですか？** [クイックスタートにジャンプ](#-組み込みの-github-mcp-を使う)して動作を確認し、サーバーの設定を始めましょう。

## 🎯 学習目標

この章を終えると、以下のことができるようになります：

- MCP とは何か、なぜ重要なのかを理解する
- `/mcp` コマンドを使って MCP サーバーを管理する
- GitHub、ファイルシステム、ドキュメント用の MCP サーバーを設定する
- ブックアプリプロジェクトで MCP を活用したワークフローを使う
- カスタム MCP サーバーの構築方法を知る（オプション）

> ⏱️ **所要時間の目安**: 約50分（読み物15分 + ハンズオン35分）

---

## 🧩 実世界のたとえ：ブラウザ拡張機能

<img src="images/browser-extensions-analogy.png" alt="MCP Servers are like Browser Extensions" width="800"/>

MCP サーバーはブラウザの拡張機能のようなものです。ブラウザ単体でも Web ページを表示できますが、拡張機能をインストールすることで追加のサービスに接続できます：

| ブラウザ拡張機能 | 接続先 | MCP の対応例 |
|-------------------|---------------------|----------------|
| パスワードマネージャー | パスワード保管庫 | **GitHub MCP** → リポジトリ、Issue、PR |
| Grammarly | 文章分析サービス | **Context7 MCP** → ライブラリドキュメント |
| ファイルマネージャー | クラウドストレージ | **Filesystem MCP** → ローカルプロジェクトファイル |

拡張機能がなくてもブラウザは便利ですが、拡張機能を入れることで強力なツールになります。MCP サーバーは Copilot に対して同じ役割を果たします。GitHub の Issue を読んだり、ファイルシステムを探索したり、最新のドキュメントを取得したりと、リアルタイムのデータソースに接続できるようになります。

***MCP サーバーは Copilot を外の世界に接続します：GitHub、リポジトリ、ドキュメントなど***

> 💡 **重要なポイント**: MCP がなければ、Copilot は `@` で明示的に共有したファイルしか見ることができません。MCP があれば、Copilot はプロジェクトを自発的に探索し、GitHub リポジトリを確認し、ドキュメントを検索することが、すべて自動的にできるようになります。

---

<img src="images/quick-start-mcp.png" alt="Power cable connecting with bright electrical spark surrounded by floating tech icons representing MCP server connections" width="800"/>

# クイックスタート：30秒で始める MCP

## 組み込みの GitHub MCP サーバーを使ってみよう
何も設定せずに、今すぐ MCP を体験してみましょう。
GitHub MCP サーバーはデフォルトで含まれています。以下を試してみてください：

```bash
copilot
> List the recent commits in this repository
```

Copilot が実際のコミットデータを返してきたら、MCP が動作しているのを確認できたことになります。それは GitHub MCP サーバーがあなたの代わりに GitHub にアクセスしているのです。しかし GitHub は *1つ* のサーバーに過ぎません。この章では、さらにサーバーを追加して（ファイルシステムアクセス、最新ドキュメントなど）、Copilot をもっと活用する方法を学びます。

---

## `/mcp show` コマンド

`/mcp show` を使って、設定されている MCP サーバーとその有効/無効の状態を確認できます：

```bash
copilot

> /mcp show

MCP Servers:
✓ github (enabled) - GitHub integration
✓ filesystem (enabled) - File system access
```

> 💡 **GitHub サーバーしか表示されない？** それは正常です！追加の MCP サーバーをまだ設定していなければ、GitHub だけが表示されます。次のセクションでサーバーを追加していきます。

> 📚 **すべての `/mcp` コマンドを確認したいですか？** サーバーの追加、編集、有効化、削除のための追加コマンドがあります。この章の最後にある[コマンドリファレンス](#-追加の-mcp-コマンド)をご覧ください。

<details>
<summary>🎬 実際の動作を見てみよう！</summary>

![MCP Status Demo](images/mcp-status-demo.gif)

*デモの出力は一例です。使用するモデル、ツール、レスポンスはここに示されているものとは異なる場合があります。*

</details>

---

## MCP で何が変わるのか？

MCP があるとないとで、実際の違いを見てみましょう：

**MCP なしの場合:**
```bash
> What's in GitHub issue #42?

"I don't have access to GitHub. You'll need to copy and paste the issue content."
```

**MCP ありの場合:**
```bash
> What's in GitHub issue #42 of this repository?

Issue #42: Login fails with special characters
Status: Open
Labels: bug, priority-high
Description: Users report that passwords containing...
```

MCP は Copilot にあなたの実際の開発環境を認識させます。

> 📚 **公式ドキュメント**: MCP が GitHub Copilot でどのように機能するかの詳細は [About MCP](https://docs.github.com/copilot/concepts/context/mcp) をご覧ください。

---

# MCP サーバーの設定

<img src="images/configuring-mcp-servers.png" alt="Hands adjusting knobs and sliders on a professional audio mixing board representing MCP server configuration" width="800"/>

MCP の動作を確認できたので、次は追加のサーバーを設定しましょう。このセクションでは設定ファイルの形式と新しいサーバーの追加方法を説明します。

---

## MCP 設定ファイル

MCP サーバーは `~/.copilot/mcp-config.json`（ユーザーレベル、すべてのプロジェクトに適用）または `.vscode/mcp.json`（プロジェクトレベル、現在のワークスペースにのみ適用）で設定します。

```json
{
  "mcpServers": {
    "server-name": {
      "type": "local",
      "command": "npx",
      "args": ["@package/server-name"],
      "tools": ["*"]
    }
  }
}
```

*ほとんどの MCP サーバーは npm パッケージとして配布されており、`npx` コマンドで実行します。*

<details>
<summary>💡 <strong>JSON が初めての方へ</strong> ここをクリックして各フィールドの意味を確認</summary>

| フィールド | 意味 |
|-------|---------------|
| `"mcpServers"` | すべての MCP サーバー設定を格納するコンテナ |
| `"server-name"` | 自分で選ぶ名前（例："github"、"filesystem"） |
| `"type": "local"` | サーバーは自分のマシンで実行される |
| `"command": "npx"` | 実行するプログラム（npx は npm パッケージを実行するツール） |
| `"args": [...]` | コマンドに渡される引数 |
| `"tools": ["*"]` | このサーバーのすべてのツールを許可する |

**JSON の重要なルール:**
- 文字列にはダブルクォート `"` を使用する（シングルクォートではない）
- 最後の項目の後にカンマを付けない
- ファイルは有効な JSON でなければならない（不安な場合は [JSON バリデーター](https://jsonlint.com/) を使用）

</details>

---

## MCP サーバーの追加

GitHub MCP サーバーは組み込みで、設定は不要です。以下は追加できるサーバーです。**興味のあるものを選ぶか、順番に進めてください。**

| やりたいこと | ジャンプ先 |
|---|---|
| Copilot にプロジェクトファイルを閲覧させたい | [Filesystem サーバー](#filesystem-server) |
| 最新のライブラリドキュメントを取得したい | [Context7 サーバー](#context7-server-documentation) |
| オプションの追加機能を試したい（カスタムサーバー、web_fetch） | [さらに先へ](#beyond-the-basics) |

<details>
<summary><strong>Filesystem サーバー</strong> - Copilot にプロジェクトファイルを探索させる</summary>
<a id="filesystem-server"></a>

### Filesystem サーバー

```json
{
  "mcpServers": {
    "filesystem": {
      "type": "local",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."],
      "tools": ["*"]
    }
  }
}
```

> 💡 **`.` パスについて**: `.` は「カレントディレクトリ」を意味します。Copilot は起動した場所を基準にファイルにアクセスできます。Codespace では、ワークスペースのルートになります。必要であれば `/workspaces/copilot-cli-for-beginners` のような絶対パスも使用できます。

これを `~/.copilot/mcp-config.json` に追加し、Copilot を再起動してください。

</details>

<details>
<summary><strong>Context7 サーバー</strong> - 最新のライブラリドキュメントを取得する</summary>
<a id="context7-server-documentation"></a>

### Context7 サーバー（ドキュメント）

Context7 は Copilot に人気のフレームワークやライブラリの最新ドキュメントへのアクセスを提供します。古くなっている可能性のある学習データに頼る代わりに、Copilot が実際の最新ドキュメントを取得します。

```json
{
  "mcpServers": {
    "context7": {
      "type": "local",
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"],
      "tools": ["*"]
    }
  }
}
```

- ✅ **API キー不要**
- ✅ **アカウント不要**
- ✅ **コードはローカルに保持**

これを `~/.copilot/mcp-config.json` に追加し、Copilot を再起動してください。

</details>

<details>
<summary><strong>さらに先へ</strong> - カスタムサーバーと Web アクセス（オプション）</summary>
<a id="beyond-the-basics"></a>

これらは上記のコアサーバーに慣れた後に試せるオプション機能です。

### Microsoft Learn MCP サーバー

これまで見てきた MCP サーバー（Filesystem、Context7）はすべてローカルマシンで実行されます。しかし、MCP サーバーはリモートで実行することもできます。つまり、Copilot CLI に URL を指定するだけで、残りは自動的に処理されます。`npx` や `python` も不要で、ローカルプロセスもなく、インストールする依存関係もありません。

[Microsoft Learn MCP サーバー](https://github.com/microsoftdocs/mcp) はその良い例です。Copilot CLI に Microsoft の公式ドキュメント（Azure、Microsoft Foundry やその他の AI トピック、.NET、Microsoft 365 など）への直接アクセスを提供し、ドキュメントの検索、ページ全体の取得、公式コードサンプルの検索ができるようになります。モデルの学習データに頼る必要がなくなります。

- ✅ **API キー不要**
- ✅ **アカウント不要**
- ✅ **ローカルインストール不要**

**`/plugin install` でかんたんインストール：**

JSON 設定ファイルを手動で編集する代わりに、1つのコマンドでインストールできます：

```bash
copilot

> /plugin install microsoftdocs/mcp
```

これにより、サーバーと関連するエージェントスキルが自動的に追加されます。インストールされるスキルは以下の通りです：

- **microsoft-docs**: コンセプト、チュートリアル、ファクトの検索
- **microsoft-code-reference**: API の検索、コードサンプル、トラブルシューティング
- **microsoft-skill-creator**: Microsoft テクノロジーに関するカスタムスキルを生成するメタスキル

**使い方：**
```bash
copilot

> What's the recommended way to deploy a Python app to Azure App Service? Search Microsoft Learn.
```

📚 詳細はこちら: [Microsoft Learn MCP Server overview](https://learn.microsoft.com/training/support/mcp-get-started)

### `web_fetch` による Web アクセス

Copilot CLI には、任意の URL からコンテンツを取得できる組み込みの `web_fetch` ツールがあります。ターミナルを離れることなく、README、API ドキュメント、リリースノートを取り込むのに便利です。MCP サーバーは不要です。

アクセス可能な URL は `~/.copilot/config.json`（Copilot の一般設定）で制御できます。これは MCP サーバー定義用の `~/.copilot/mcp-config.json` とは別のファイルです。

```json
{
  "permissions": {
    "allowedUrls": [
      "https://api.github.com/**",
      "https://docs.github.com/**",
      "https://*.npmjs.org/**"
    ],
    "blockedUrls": [
      "http://**"
    ]
  }
}
```

**使い方：**
```bash
copilot

> Fetch and summarize the README from https://github.com/facebook/react
```

### カスタム MCP サーバーの構築

Copilot を独自の API、データベース、社内ツールに接続したい場合は、Python でカスタム MCP サーバーを構築できます。既製のサーバー（GitHub、Filesystem、Context7）がほとんどのユースケースをカバーしているため、これは完全にオプションです。

📖 ブックアプリを例にした完全なウォークスルーは [カスタム MCP サーバーガイド](mcp-custom-server.md) をご覧ください。

📚 より詳しい背景情報は [MCP for Beginners course](https://github.com/microsoft/mcp-for-beginners) をご覧ください。

</details>

<a id="complete-configuration-file"></a>

### 完全な設定ファイル

Filesystem と Context7 サーバーを含む完全な `mcp-config.json` はこちらです：

> 💡 **注意:** GitHub MCP は組み込みです。設定ファイルに追加する必要はありません。

```json
{
  "mcpServers": {
    "filesystem": {
      "type": "local",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."],
      "tools": ["*"]
    },
    "context7": {
      "type": "local",
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"],
      "tools": ["*"]
    }
  }
}
```

グローバルアクセスには `~/.copilot/mcp-config.json` に、プロジェクト固有の設定には `.vscode/mcp.json` に保存してください。

---

# MCP サーバーの使い方

MCP サーバーの設定ができたので、何ができるか見ていきましょう。

<img src="images/using-mcp-servers.png" alt="Using MCP Servers - Hub-and-spoke diagram showing a Developer CLI connected to GitHub, Filesystem, Context7, and Custom/Web Fetch servers" width="800" />

---

## サーバー使用例

**試したいサーバーを選ぶか、順番に進めてください。**

| 試したいこと | ジャンプ先 |
|---|---|
| GitHub リポジトリ、Issue、PR | [GitHub サーバー](#github-server-built-in) |
| プロジェクトファイルの閲覧 | [Filesystem サーバーの使い方](#filesystem-server-usage) |
| ライブラリドキュメントの検索 | [Context7 サーバーの使い方](#context7-server-usage) |
| カスタムサーバー、Microsoft Learn MCP、web_fetch の使い方 | [さらに先へ（使い方）](#beyond-the-basics-usage) |

<details>
<summary><strong>GitHub サーバー（組み込み）</strong> - リポジトリ、Issue、PR などにアクセス</summary>
<a id="github-server-built-in"></a>

### GitHub サーバー（組み込み）

GitHub MCP サーバーは**組み込み**です。Copilot にログインしていれば（初期セットアップで行ったはずです）、すでに動作しています。設定は不要です！

> 💡 **動作しない場合は？** `/login` を実行して GitHub に再認証してください。

<details>
<summary><strong>Dev Container での認証</strong></summary>

- **GitHub Codespaces**（推奨）: 認証は自動的に行われます。`gh` CLI が Codespace のトークンを引き継ぎます。操作は不要です。
- **ローカル Dev Container（Docker）**: コンテナの起動後に `gh auth login` を実行し、Copilot を再起動してください。

**認証のトラブルシューティング：**
```bash
# 認証済みか確認
gh auth status

# 未認証の場合はログイン
gh auth login

# GitHub MCP が接続されているか確認
copilot
> /mcp show
```

</details>

| 機能 | 例 |
|---------|----------|
| **リポジトリ情報** | コミット、ブランチ、コントリビューターの表示 |
| **Issue** | Issue の一覧表示、作成、検索、コメント |
| **プルリクエスト** | PR の表示、差分の確認、PR の作成、ステータスチェック |
| **コード検索** | リポジトリ横断でのコード検索 |
| **Actions** | ワークフローの実行状況とステータスの照会 |

```bash
copilot

# このリポジトリの最近のアクティビティを確認
> List the last 5 commits in this repository

Recent commits:
1. abc1234 - Update chapter 05 skills examples (2 days ago)
2. def5678 - Add book app test fixtures (3 days ago)
3. ghi9012 - Fix typo in chapter 03 README (4 days ago)
...

# リポジトリの構造を調べる
> What branches exist in this repository?

Branches:
- main (default)
- chapter6 (current)

# リポジトリ全体でコードパターンを検索
> Search this repository for files that import pytest

Found 1 file:
- samples/book-app-project/tests/test_books.py
```

> 💡 **自分のフォークで作業していますか？** このコースリポジトリをフォークした場合、Issue やプルリクエストの作成など書き込み操作も試せます。以下の演習で練習します。

> ⚠️ **結果が表示されない場合は？** GitHub MCP はリモート（github.com 上）のリポジトリに対して動作し、ローカルファイルだけを対象としているわけではありません。リポジトリにリモートが設定されているか確認してください：`git remote -v` を実行。

</details>

<details>
<summary><strong>Filesystem サーバー</strong> - プロジェクトファイルの閲覧と分析</summary>
<a id="filesystem-server-usage"></a>

### Filesystem サーバー

設定が完了すると、Filesystem MCP は Copilot が自動的に使用できるツールを提供します：

```bash
copilot

> How many Python files are in the book-app-project directory?

Found 3 Python files in samples/book-app-project/:
- book_app.py
- books.py
- utils.py

> What's the total size of the data.json file?

samples/book-app-project/data.json: 2.4 KB

> Find all functions that don't have type hints in the book app

Found 2 functions without type hints:
- samples/book-app-project/utils.py:10 - get_user_choice()
- samples/book-app-project/utils.py:14 - get_book_details()
```

</details>

<details>
<summary><strong>Context7 サーバー</strong> - ライブラリドキュメントの検索</summary>
<a id="context7-server-usage"></a>

### Context7 サーバー

```bash
copilot

> What are the best practices for using pytest fixtures?

From pytest Documentation:

Fixtures - Use fixtures to provide a fixed baseline for tests:

    import pytest

    @pytest.fixture
    def sample_books():
        return [
            {"title": "1984", "author": "George Orwell", "year": 1949},
            {"title": "Dune", "author": "Frank Herbert", "year": 1965},
        ]

    def test_find_by_author(sample_books):
        # fixture is automatically passed as argument
        results = [b for b in sample_books if "Orwell" in b["author"]]
        assert len(results) == 1

Best practices:
- Use fixtures instead of setup/teardown methods
- Use tmp_path fixture for temporary files
- Use monkeypatch for modifying environment
- Scope fixtures appropriately (function, class, module, session)

> How can I apply this to the book app's test file?

# Copilot now knows the official pytest patterns
# and can apply them to samples/book-app-project/tests/test_books.py
```

</details>

<details>
<summary><strong>さらに先へ</strong> - カスタムサーバーと web_fetch の使い方</summary>
<a id="beyond-the-basics-usage"></a>

### さらに先へ

**カスタム MCP サーバー**: [カスタム MCP サーバーガイド](mcp-custom-server.md) で book-lookup サーバーを構築した場合、ブックコレクションに直接クエリできます：

```bash
copilot

> Look up information about "1984" using the book lookup server. Search for books by George Orwell
```

**Microsoft Learn MCP**: [Microsoft Learn MCP サーバー](#microsoft-learn-mcp-サーバー)をインストールした場合、Microsoft の公式ドキュメントを直接検索できます：

```bash
copilot

> How do I configure managed identity for an Azure Function? Search Microsoft Learn.
```

**Web Fetch**: 組み込みの `web_fetch` ツールを使って、任意の URL からコンテンツを取得できます：

```bash
copilot

> Fetch and summarize the README from https://github.com/facebook/react
```

</details>

---

## マルチサーバーワークフロー

これらのワークフローは、開発者が「もうこれなしでは仕事できない」と言う理由を示しています。各例は、1つのセッションで複数の MCP サーバーを組み合わせます。

<img src="images/issue-to-pr-workflow.png" alt="Issue to PR Workflow using MCP - Shows the complete flow from getting a GitHub issue through creating a pull request" width="800"/>

*完全な MCP ワークフロー：GitHub MCP がリポジトリデータを取得し、Filesystem MCP がコードを見つけ、Context7 MCP がベストプラクティスを提供し、Copilot が分析を行います*

以下の各例は自己完結しています。**興味のあるものを選ぶか、すべてお読みください。**

| 見たいもの | ジャンプ先 |
|---|---|
| 複数のサーバーが連携する様子 | [マルチサーバー探索](#multi-server-exploration) |
| Issue から PR への一連の流れ | [Issue から PR へのワークフロー](#issue-to-pr-workflow) |
| プロジェクトのヘルスチェック | [ヘルスダッシュボード](#health-dashboard) |

<details>
<summary><strong>マルチサーバー探索</strong> - Filesystem、GitHub、Context7 を1つのセッションで組み合わせる</summary>
<a id="multi-server-exploration"></a>

#### 複数の MCP サーバーでブックアプリを探索する

```bash
copilot

# ステップ 1: Filesystem MCP を使ってブックアプリを探索
> List all Python files in samples/book-app-project/ and summarize
> what each file does

Found 3 Python files:
- book_app.py: CLI entry point with command routing (list, add, remove, find)
- books.py: BookCollection class with data persistence via JSON
- utils.py: Helper functions for user input and display

# ステップ 2: GitHub MCP を使って最近の変更を確認
> What were the last 3 commits that touched files in samples/book-app-project/?

Recent commits affecting book app:
1. abc1234 - Add test fixtures for BookCollection (2 days ago)
2. def5678 - Add find_by_author method (5 days ago)
3. ghi9012 - Initial book app setup (1 week ago)

# ステップ 3: Context7 MCP を使ってベストプラクティスを確認
> What are Python best practices for JSON data persistence?

From Python Documentation:
- Use context managers (with statements) for file I/O
- Handle JSONDecodeError for corrupted files
- Use dataclasses for structured data
- Consider atomic writes to prevent data corruption

# ステップ 4: 推奨事項をまとめる
> Based on the book app code and these best practices,
> what improvements would you suggest?

Suggestions:
1. Add input validation in add_book() for empty strings and invalid years
2. Consider atomic writes in save_books() to prevent data corruption
3. Add type hints to utils.py functions (get_user_choice, get_book_details)
```

<details>
<summary>🎬 MCP ワークフローの動作を見てみよう！</summary>

![MCP Workflow Demo](images/mcp-workflow-demo.gif)

*デモの出力は一例です。使用するモデル、ツール、レスポンスはここに示されているものとは異なる場合があります。*

</details>

**結果**: コード探索 → 履歴の確認 → ベストプラクティスの検索 → 改善計画。**すべて1つのターミナルセッションで、3つの MCP サーバーを組み合わせて実現。**

</details>

<details>
<summary><strong>Issue から PR へのワークフロー</strong> - ターミナルを離れることなく GitHub Issue からプルリクエストまで</summary>
<a id="issue-to-pr-workflow"></a>

#### Issue から PR へのワークフロー（自分のリポジトリで実行）

これは書き込み権限のある自分のフォークまたはリポジトリで最も効果的です：

> 💡 **今すぐ試せなくても心配ありません。** 読み取り専用のクローンを使用している場合は、課題で練習します。今は流れを理解するために読み進めてください。

```bash
copilot

> Get the details of GitHub issue #1

Issue #1: Add input validation for book year
Status: Open
Description: The add_book function accepts any year value...

> @samples/book-app-project/books.py Fix the issue described in issue #1

[Copilot implements year validation in add_book()]

> Run the tests to make sure the fix works

All 8 tests passed ✓

> Create a pull request titled "Add year validation to book app"

✓ Created PR #2: Add year validation to book app
```

**コピー＆ペーストなし。コンテキストの切り替えなし。1つのターミナルセッションで完結。**

</details>

<details>
<summary><strong>ヘルスダッシュボード</strong> - 複数のサーバーを使ったプロジェクトのヘルスチェック</summary>
<a id="health-dashboard"></a>

#### ブックアプリ ヘルスダッシュボード

```bash
copilot

> Give me a health report for the book app project:
> 1. List all functions across the Python files in samples/book-app-project/
> 2. Check which functions have type hints and which don't
> 3. Show what tests exist in samples/book-app-project/tests/
> 4. Check the recent commit history for this directory

Book App Health Report
======================

📊 Functions Found:
- books.py: 8 methods in BookCollection (all have type hints ✓)
- book_app.py: 6 functions (4 have type hints, 2 missing)
- utils.py: 3 functions (1 has type hints, 2 missing)

🧪 Test Coverage:
- test_books.py: 8 test functions covering BookCollection
- Missing: no tests for book_app.py CLI functions
- Missing: no tests for utils.py helper functions

📝 Recent Activity:
- 3 commits in the last week
- Most recent: added test fixtures

Recommendations:
- Add type hints to utils.py functions
- Add tests for book_app.py CLI handlers
- All files well-sized (<100 lines) - good structure!
```

**結果**: 複数のデータソースが数秒で集約されます。手動であれば、grep の実行、行数のカウント、git log の確認、テストファイルの閲覧が必要になり、15分以上かかる作業です。

</details>

---

# 練習

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

**🎉 基本はマスターしました！** MCP を理解し、サーバーの設定方法を学び、実際のワークフローを見てきました。ここからは自分で試してみましょう。

---

## ▶️ 実践してみよう

あなたの番です！以下の演習を完了して、ブックアプリプロジェクトで MCP サーバーを使う練習をしましょう。

### 演習 1: MCP のステータスを確認する

まずは利用可能な MCP サーバーを確認しましょう：

```bash
copilot

> /mcp show
```

GitHub サーバーが有効として表示されるはずです。表示されない場合は `/login` を実行して認証してください。

---

### 演習 2: Filesystem MCP でブックアプリを探索する

Filesystem サーバーを設定済みの場合、これを使ってブックアプリを探索しましょう：

```bash
copilot

> How many Python files are in samples/book-app-project/?
> What functions are defined in each file?
```

**期待される結果**: Copilot が `book_app.py`、`books.py`、`utils.py` とそれぞれの関数を一覧表示します。

> 💡 **Filesystem MCP をまだ設定していませんか？** 上記の[完全な設定ファイル](#complete-configuration-file)セクションから設定ファイルを作成してください。その後 Copilot を再起動してください。

---

### 演習 3: GitHub MCP でリポジトリ履歴を照会する

組み込みの GitHub MCP を使って、このコースリポジトリを探索しましょう：

```bash
copilot

> List the last 5 commits in this repository

> What branches exist in this repository?
```

**期待される結果**: Copilot が GitHub リモートからの最近のコミットメッセージとブランチ名を表示します。

> ⚠️ **Codespace をお使いですか？** 自動的に動作します。認証は引き継がれます。ローカルクローンの場合は、`gh auth status` でログイン済みであることを確認してください。

---

### 演習 4: 複数の MCP サーバーを組み合わせる

1つのセッションで Filesystem MCP と GitHub MCP を組み合わせましょう：

```bash
copilot

> Read samples/book-app-project/data.json and tell me what books are
> in the collection. Then check the recent commits to see when this
> file was last modified.
```

**期待される結果**: Copilot が JSON ファイルを読み取り（Filesystem MCP）、「The Hobbit」「1984」「Dune」「To Kill a Mockingbird」「Mysterious Book」の5冊を一覧表示し、GitHub にコミット履歴を問い合わせます。

**セルフチェック**: 「リポジトリのコミット履歴を確認して」が、手動で `git log` を実行してプロンプトに貼り付けるよりも優れている理由を説明できれば、MCP を理解できています。

---

## 📝 課題

### メインチャレンジ: ブックアプリ MCP 探索

ブックアプリプロジェクトで MCP サーバーを組み合わせて練習しましょう。以下のステップを1つの Copilot セッションで完了してください：

1. **MCP の動作確認**: `/mcp show` を実行して、少なくとも GitHub サーバーが有効であることを確認
2. **Filesystem MCP のセットアップ**（未設定の場合）: Filesystem サーバーの設定を含む `~/.copilot/mcp-config.json` を作成
3. **コードの探索**: Copilot に Filesystem サーバーを使って以下を依頼:
   - `samples/book-app-project/books.py` のすべての関数を一覧表示
   - `samples/book-app-project/utils.py` で型ヒントが欠けている関数を確認
   - `samples/book-app-project/data.json` を読み取り、データ品質の問題を特定（ヒント：最後のエントリを見てください）
4. **リポジトリのアクティビティ確認**: Copilot に GitHub MCP を使って以下を依頼:
   - `samples/book-app-project/` 内のファイルに影響した最近のコミットを一覧表示
   - オープンな Issue やプルリクエストがあるか確認
5. **サーバーの組み合わせ**: 1つのプロンプトで Copilot に以下を依頼:
   - `samples/book-app-project/tests/test_books.py` のテストファイルを読み取る
   - テスト済み関数を `books.py` の全関数と比較
   - テストカバレッジの不足をまとめる

**成功基準**: Filesystem と GitHub MCP のデータを1つの Copilot セッションでシームレスに組み合わせることができ、各 MCP サーバーがレスポンスにどう貢献したかを説明できること。

<details>
<summary>💡 ヒント（クリックして展開）</summary>

**ステップ 1: MCP の確認**
```bash
copilot
> /mcp show
# "github" が有効と表示されるはず
# 表示されない場合は: /login を実行
```

**ステップ 2: 設定ファイルの作成**

上記の[完全な設定ファイル](#complete-configuration-file)セクションの JSON を使用し、`~/.copilot/mcp-config.json` として保存してください。

**ステップ 3: 探すべきデータ品質の問題**

`data.json` の最後の本は：
```json
{
  "title": "Mysterious Book",
  "author": "",
  "year": 0,
  "read": false
}
```
著者が空で、出版年が 0 です。これがデータ品質の問題です！

**ステップ 5: テストカバレッジの比較**

`test_books.py` のテストは以下をカバーしています：`add_book`、`mark_as_read`、`remove_book`、`get_unread_books`、`find_book_by_title`。`load_books`、`save_books`、`list_books` のような関数には直接のテストがありません。`book_app.py` の CLI 関数と `utils.py` のヘルパー関数にはテストが一切ありません。

**MCP が動作しない場合:** 設定ファイルを編集した後、Copilot を再起動してください。

</details>

### ボーナスチャレンジ: カスタム MCP サーバーの構築

さらに深く学びたいですか？[カスタム MCP サーバーガイド](mcp-custom-server.md) に従って、任意の API に接続する独自の MCP サーバーを Python で構築しましょう。

---

<details>
<summary>🔧 <strong>よくある間違いとトラブルシューティング</strong>（クリックして展開）</summary>

### よくある間違い

| 間違い | 何が起こるか | 対処法 |
|---------|--------------|-----|
| GitHub MCP が組み込みであることを知らない | 手動でインストール・設定しようとする | GitHub MCP はデフォルトで含まれています。次を試してください：「List the recent commits in this repo」 |
| 設定ファイルの場所を間違える | MCP 設定が見つからない・編集できない | ユーザーレベルの設定は `~/.copilot/mcp-config.json`、プロジェクトレベルは `.vscode/mcp.json` |
| 設定ファイルの JSON が不正 | MCP サーバーの読み込みに失敗 | `/mcp show` で設定を確認。JSON 構文を検証 |
| MCP サーバーの認証を忘れる | 「Authentication failed」エラー | 一部の MCP は個別の認証が必要。各サーバーの要件を確認 |

### トラブルシューティング

**「MCP server not found」** - 以下を確認してください：
1. npm パッケージが存在するか：`npm view @modelcontextprotocol/server-github`
2. 設定が有効な JSON であるか
3. サーバー名が設定と一致しているか

`/mcp show` を使って現在の設定を確認してください。

**「GitHub authentication failed」** - 組み込みの GitHub MCP は `/login` の認証情報を使用します。以下を試してください：

```bash
copilot
> /login
```

これにより GitHub に再認証されます。問題が解決しない場合は、GitHub アカウントにアクセスしようとしているリポジトリに対する適切な権限があることを確認してください。

**「MCP server failed to start」** - サーバーログを確認してください：
```bash
# サーバーコマンドを手動で実行してエラーを確認
npx -y @modelcontextprotocol/server-github
```

**MCP ツールが利用できない** - サーバーが有効であることを確認してください：
```bash
copilot

> /mcp show
# サーバーが表示され、有効になっているか確認
```

サーバーが無効な場合は、再有効化の方法について以下の[追加の `/mcp` コマンド](#-追加の-mcp-コマンド)をご覧ください。

</details>

---

<details>
<summary>📚 <strong>追加の <code>/mcp</code> コマンド</strong>（クリックして展開）</summary>
<a id="-追加の-mcp-コマンド"></a>

`/mcp show` 以外にも、MCP サーバーを管理するためのコマンドがいくつかあります：

| コマンド | 説明 |
|---------|--------------|
| `/mcp show` | 設定されたすべての MCP サーバーとステータスを表示 |
| `/mcp add` | 新しいサーバーを追加するためのインタラクティブセットアップ |
| `/mcp edit <server-name>` | 既存のサーバー設定を編集 |
| `/mcp enable <server-name>` | 無効化されたサーバーを有効化 |
| `/mcp disable <server-name>` | サーバーを一時的に無効化 |
| `/mcp delete <server-name>` | サーバーを完全に削除 |

このコースのほとんどの場面では `/mcp show` だけで十分です。その他のコマンドは、管理するサーバーが増えてきたときに役立ちます。

</details>

---

# まとめ

## 🔑 重要なポイント

1. **MCP** は Copilot を外部サービス（GitHub、ファイルシステム、ドキュメント）に接続する
2. **GitHub MCP は組み込み** - 設定不要、`/login` だけで使える
3. **Filesystem と Context7** は `~/.copilot/mcp-config.json` で設定する
4. **マルチサーバーワークフロー** で1つのセッション内の複数ソースからデータを組み合わせる
5. **サーバーのステータス確認** は `/mcp show` で（追加のサーバー管理コマンドも利用可能）
6. **カスタムサーバー** で任意の API に接続できる（オプション、付録ガイドに記載）

> 📋 **クイックリファレンス**: コマンドとショートカットの完全な一覧は [GitHub Copilot CLI command reference](https://docs.github.com/en/copilot/reference/cli-command-reference) をご覧ください。

---

## ➡️ 次のステップ

モード、コンテキスト、ワークフロー、エージェント、スキル、MCP といった、すべてのビルディングブロックが揃いました。次はそれらを組み合わせましょう。

**[Chapter 07: すべてをまとめる](../07-putting-it-together/README.ja.md)** では、以下を学びます：

- エージェント、スキル、MCP を統合したワークフローの構築
- アイデアからマージ済み PR までの完全な機能開発
- フックによる自動化
- チーム環境でのベストプラクティス

---

**[← Chapter 05 に戻る](../05-skills/README.ja.md)** | **[Chapter 07 へ進む →](../07-putting-it-together/README.ja.md)**
