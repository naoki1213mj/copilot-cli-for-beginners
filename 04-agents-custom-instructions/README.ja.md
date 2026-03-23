![Chapter 04: Agents and Custom Instructions](images/chapter-header.png)

> **Python コードレビュアー、テスト専門家、セキュリティレビュアーを…すべて1つのツールで雇えるとしたら？**

Chapter 03 では、コードレビュー、リファクタリング、デバッグ、テスト生成、Git 連携といった基本的なワークフローをマスターしました。これらにより GitHub Copilot CLI を高い生産性で使えるようになりました。さらにステップアップしましょう。

これまで Copilot CLI を汎用的なアシスタントとして使ってきました。エージェントを使うと、特定のペルソナと組み込みの基準を与えることができます。たとえば、型ヒントや PEP 8 を強制するコードレビュアーや、pytest のテストケースを書くテストヘルパーなどです。対象を絞った指示を持つエージェントが処理すると、同じプロンプトでも明らかに優れた結果が得られることがわかるでしょう。

## 🎯 学習目標

この章を終えると、以下のことができるようになります：

- 組み込みエージェントの使用：Plan（`/plan`）、Code-review（`/review`）、および自動エージェント（Explore、Task）の理解
- エージェントファイル（`.agent.md`）を使った特化型エージェントの作成
- ドメイン固有のタスクにエージェントを使用
- `/agent` および `--agent` によるエージェントの切り替え
- プロジェクト固有の基準に対応したカスタムインストラクションファイルの作成

> ⏱️ **想定所要時間**：約55分（読み物20分 ＋ ハンズオン35分）

---

## 🧩 現実世界のアナロジー：専門家を雇う

家のことで助けが必要なとき、「なんでも屋」は呼びませんよね。専門家を呼びます：

| 問題 | 専門家 | 理由 |
|------|--------|------|
| 水漏れ | 配管工 | 配管規格を熟知し、専門工具を持っている |
| 配線工事 | 電気工事士 | 安全要件を理解し、規格に適合 |
| 新しい屋根 | 屋根職人 | 素材や地域の気候条件を熟知 |

エージェントも同じ仕組みです。汎用的な AI の代わりに、特定のタスクに特化し、適切なプロセスを知っているエージェントを使います。一度指示を設定すれば、その専門分野が必要なときにいつでも再利用できます：コードレビュー、テスト、セキュリティ、ドキュメント作成。

<img src="images/hiring-specialists-analogy.png" alt="Hiring Specialists Analogy - Just as you call specialized tradespeople for house repairs, AI agents are specialized for specific tasks like code review, testing, security, and documentation" width="800" />

---

# エージェントを使う

組み込みエージェントとカスタムエージェントをすぐに使い始めましょう。

---

## *エージェントが初めて？* ここから始めよう！
エージェントを使ったことも作ったこともない方へ。このコースで始めるために必要なことをすべて説明します。

1. **今すぐ*組み込み*エージェントを試す：**
   ```bash
   copilot
   > /plan Add input validation for book year in the book app
   ```
   これは Plan エージェントを呼び出し、ステップバイステップの実装計画を作成します。

2. **カスタムエージェントの例を見る：** エージェントの指示を定義するのは簡単です。提供されている [python-reviewer.agent.md](../.github/agents/python-reviewer.agent.md) ファイルを見てパターンを確認しましょう。

3. **コアコンセプトを理解する：** エージェントは、ジェネラリストではなくスペシャリストに相談するようなものです。「フロントエンドエージェント」はアクセシビリティやコンポーネントパターンに自動的に注目します。エージェントの指示にすでに指定されているため、毎回思い出させる必要はありません。


## 組み込みエージェント

**Chapter 03 の開発ワークフローで、すでにいくつかの組み込みエージェントを使っています！**
<br>`/plan` と `/review` は実はエージェントです。これで舞台裏で何が起こっているかわかりましたね。完全な一覧はこちらです：

| エージェント | 呼び出し方 | 機能 |
|-------------|-----------|------|
| **Plan** | `/plan` または `Shift+Tab`（モード切替） | コーディング前にステップバイステップの実装計画を作成 |
| **Code-review** | `/review` | ステージ済み/未ステージの変更に対し、焦点を絞った実用的なフィードバックを提供 |
| **Init** | `/init` | プロジェクト設定ファイル（インストラクション、エージェント）を生成 |
| **Explore** | *自動* | コードベースの探索や分析を求めたときに内部的に使用される |
| **Task** | *自動* | テスト、ビルド、リント、依存関係のインストールなどのコマンドを実行 |

<br>

**組み込みエージェントの動作例** - Plan、Code-review、Explore、Task の呼び出し例

```bash
copilot

# Plan エージェントを呼び出して実装計画を作成
> /plan Add input validation for book year in the book app

# Code-review エージェントで変更をレビュー
> /review

# Explore と Task エージェントは関連する場面で自動的に呼び出されます：
> Run the test suite        # Task エージェントを使用

> Explore how book data is loaded    # Explore エージェントを使用
```

Task エージェントについて：舞台裏で動作し、何が起こっているかを管理・追跡して、きれいでわかりやすい形式で報告します：

| 結果 | 表示内容 |
|------|---------|
| ✅ **成功** | 簡潔なサマリー（例：「All 247 tests passed」「Build succeeded」） |
| ❌ **失敗** | スタックトレース、コンパイラエラー、詳細ログを含む完全な出力 |


> 📚 **公式ドキュメント**：[GitHub Copilot CLI Agents](https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#use-custom-agents)

---

# Copilot CLI にエージェントを追加する

独自のエージェントをワークフローの一部として簡単に定義できます！一度定義すれば、あとは指示するだけ！

<img src="images/using-agents.png" alt="Four colorful AI robots standing together, each with different tools representing specialized agent capabilities" width="800"/>

## 🗂️ エージェントを追加する

エージェントファイルは `.agent.md` 拡張子を持つ Markdown ファイルです。YAML フロントマター（メタデータ）と Markdown の指示の2つの部分で構成されています。

> 💡 **YAML フロントマターが初めて？** ファイルの先頭にある `---` マーカーで囲まれた小さな設定ブロックです。YAML は単なる `key: value` のペアです。残りは通常の Markdown です。

最小限のエージェントはこちらです：

```markdown
---
name: my-reviewer
description: Code reviewer focused on bugs and security issues
---

# Code Reviewer

You are a code reviewer focused on finding bugs and security issues.

When reviewing code, always check for:
- SQL injection vulnerabilities
- Missing error handling
- Hardcoded secrets
```

> 💡 **必須 vs オプション**：`description` フィールドは必須です。`name`、`tools`、`model` などの他のフィールドはオプションです。

## エージェントファイルの配置場所

| 配置場所 | スコープ | 最適な用途 |
|---------|---------|-----------|
| `.github/agents/` | プロジェクト固有 | プロジェクトの規約を持つチーム共有エージェント |
| `~/.copilot/agents/` | グローバル（全プロジェクト） | どこでも使う個人用エージェント |

**このプロジェクトには [.github/agents/](../.github/agents/) フォルダにサンプルエージェントファイルが含まれています**。自分で書くことも、提供されているものをカスタマイズすることもできます。

<details>
<summary>📂 このコースのサンプルエージェントを見る</summary>

| ファイル | 説明 |
|---------|------|
| `hello-world.agent.md` | 最小限の例 - ここから始めましょう |
| `python-reviewer.agent.md` | Python コード品質レビュアー |
| `pytest-helper.agent.md` | pytest テスト専門家 |

```bash
# または個人用エージェントフォルダにコピー（すべてのプロジェクトで利用可能）
cp .github/agents/python-reviewer.agent.md ~/.copilot/agents/
```

コミュニティエージェントについては [github/awesome-copilot](https://github.com/github/awesome-copilot) を参照してください。

</details>


## 🚀 カスタムエージェントの2つの使い方

### インタラクティブモード
インタラクティブモード内で `/agent` を使ってエージェント一覧を表示し、使いたいエージェントを選択します。
エージェントを選択して会話を続けましょう。

```bash
copilot
> /agent
```

別のエージェントに変更する場合やデフォルトモードに戻る場合は、再度 `/agent` コマンドを使用します。

### プログラマティックモード

エージェントを指定して新しいセッションを直接起動します。

```bash
copilot --agent python-reviewer
> Review @samples/book-app-project/books.py
```

> 💡 **エージェントの切り替え**：`/agent` または `--agent` を再度使用することで、いつでも別のエージェントに切り替えられます。標準の Copilot CLI 体験に戻るには、`/agent` を使って **no agent** を選択してください。

---

# エージェントをさらに深く理解する

<img src="images/creating-custom-agents.png" alt="Robot being assembled on a workbench surrounded by components and tools representing custom agent creation" width="800"/>

> 💡 **このセクションはオプションです。** 組み込みエージェント（`/plan`、`/review`）はほとんどのワークフローに十分な機能を持っています。作業全体で一貫して適用される専門的な知識が必要な場合にカスタムエージェントを作成しましょう。

以下の各トピックはそれぞれ独立しています。**興味のあるものを選んでください - 一度にすべて読む必要はありません。**

| やりたいこと | ジャンプ先 |
|---|---|
| エージェントが汎用プロンプトに勝る理由を見る | [スペシャリスト vs ジェネリック](#specialist-vs-generic-see-the-difference) |
| 機能開発でエージェントを組み合わせる | [複数エージェントの連携](#working-with-multiple-agents) |
| エージェントの整理、命名、共有 | [エージェントの整理と共有](#organizing--sharing-agents) |
| 常時有効なプロジェクトコンテキストの設定 | [Copilot のプロジェクト設定](#configuring-your-project-for-copilot) |
| YAML プロパティとツールの参照 | [エージェントファイルリファレンス](#agent-file-reference) |

以下のシナリオをクリックして展開してください。

---

<a id="specialist-vs-generic-see-the-difference"></a>
<details>
<summary><strong>スペシャリスト vs ジェネリック：違いを見る</strong> - エージェントが汎用プロンプトよりも優れた出力を生成する理由</summary>

## スペシャリスト vs ジェネリック：違いを見る

ここがエージェントの価値を証明する場面です。違いを見てみましょう：

### エージェントなし（汎用 Copilot）

```bash
copilot

> Add a function to search books by year range in the book app
```

**汎用的な出力**：
```python
def search_by_year_range(books, start_year, end_year):
    results = []
    for book in books:
        if book['year'] >= start_year and book['year'] <= end_year:
            results.append(book)
    return results
```

基本的です。動きます。でも多くのことが欠けています。

---

### Python Reviewer エージェントを使った場合

```bash
copilot

> /agent
# "python-reviewer" を選択

> Add a function to search books by year range in the book app
```

**スペシャリストの出力**：
```python
from typing import List, Dict, Any

def search_by_year_range(
    books: List[Dict[str, Any]],
    start_year: int,
    end_year: int
) -> List[Dict[str, Any]]:
    """
    Search for books within a specified year range.

    Args:
        books: List of book dictionaries
        start_year: Starting year (inclusive)
        end_year: Ending year (inclusive)

    Returns:
        List of books published within the year range

    Raises:
        ValueError: If start_year is greater than end_year
        TypeError: If year values are not integers
    """
    if not isinstance(start_year, int) or not isinstance(end_year, int):
        raise TypeError("Year values must be integers")

    if start_year > end_year:
        raise ValueError(f"Start year ({start_year}) cannot be greater than end year ({end_year})")

    return [
        book for book in books
        if isinstance(book.get('year'), int)
        and start_year <= book['year'] <= end_year
    ]
```

**python-reviewer エージェントが自動的に含めるもの**：
- ✅ すべてのパラメータと戻り値に型ヒント
- ✅ Args/Returns/Raises を含む包括的な docstring
- ✅ 適切なエラーハンドリングによる入力バリデーション
- ✅ パフォーマンス向上のためのリスト内包表記
- ✅ エッジケースの処理（欠落/無効な年の値）
- ✅ PEP 8 準拠のフォーマット
- ✅ 防御的プログラミングの実践

**違い**：同じプロンプトで、劇的に優れた出力。エージェントは、あなたが頼むことを忘れてしまうような専門知識を持ち込んでくれます。

</details>

---

<a id="working-with-multiple-agents"></a>
<details>
<summary><strong>複数エージェントの連携</strong> - スペシャリストの組み合わせ、セッション中の切り替え、ツールとしてのエージェント</summary>

## 複数エージェントの連携

真の力は、スペシャリストが一つの機能に対して協力するときに発揮されます。

### 例：シンプルな機能の構築

```bash
copilot

> I want to add a "search by year range" feature to the book app

# python-reviewer を設計に使用
> /agent
# "python-reviewer" を選択

> @samples/book-app-project/books.py Design a find_by_year_range method. What's the best approach?

# pytest-helper に切り替えてテスト設計
> /agent
# "pytest-helper" を選択

> @samples/book-app-project/tests/test_books.py Design test cases for a find_by_year_range method.
> What edge cases should we cover?

# 両方の設計を統合
> Create an implementation plan that includes the method implementation and comprehensive tests.
```

**重要なポイント**：あなたはスペシャリストを指揮するアーキテクトです。彼らが詳細を担当し、あなたがビジョンを担当します。

<details>
<summary>🎬 実際の動作を見る！</summary>

![Python Reviewer Demo](images/python-reviewer-demo.gif)

*デモの出力は異なります - モデル、ツール、レスポンスはここに示されているものと異なる場合があります。*

</details>

### ツールとしてのエージェント

エージェントが設定されている場合、Copilot は複雑なタスクの実行中にそれらをツールとして呼び出すこともできます。フルスタック機能を求めた場合、Copilot は適切なスペシャリストエージェントに自動的に各部分を委任することがあります。

</details>

---

<a id="organizing--sharing-agents"></a>
<details>
<summary><strong>エージェントの整理と共有</strong> - 命名、ファイル配置、インストラクションファイル、チームでの共有</summary>

## エージェントの整理と共有

### エージェントの命名

エージェントファイルを作成する際、名前は重要です。`/agent` や `--agent` の後に入力するものであり、チームメイトがエージェント一覧で見るものです。

| ✅ 良い名前 | ❌ 避けるべき名前 |
|------------|-----------------|
| `frontend` | `my-agent` |
| `backend-api` | `agent1` |
| `security-reviewer` | `helper` |
| `react-specialist` | `code` |
| `python-backend` | `assistant` |

**命名規則：**
- 小文字とハイフンを使用：`my-agent-name.agent.md`
- ドメインを含める：`frontend`、`backend`、`devops`、`security`
- 必要に応じて具体的に：`react-typescript` vs 単なる `frontend`

---

### チームとの共有

エージェントファイルを `.github/agents/` に配置すると、バージョン管理されます。リポジトリにプッシュすれば、チームメンバー全員が自動的に利用できます。ただし、エージェントは Copilot がプロジェクトから読み込むファイルの一種にすぎません。**インストラクションファイル**もサポートしており、`/agent` を実行しなくても自動的にすべてのセッションに適用されます。

このように考えてください：エージェントは必要に応じて呼び出すスペシャリストで、インストラクションファイルは常に有効なチームルールです。

### ファイルの配置場所

エージェントファイルの主要な配置場所は2つあります（上記の[エージェントファイルの配置場所](#エージェントファイルの配置場所)を参照）。この判断ツリーを使って選択してください：

<img src="images/agent-file-placement-decision-tree.png" alt="Decision tree for where to put agent files: experimenting → current folder, team use → .github/agents/, everywhere → ~/.copilot/agents/" width="800"/>

**シンプルに始めましょう：** プロジェクトフォルダに `*.agent.md` ファイルを1つ作成します。満足できたら、恒久的な場所に移動しましょう。

エージェントファイル以外にも、Copilot は**プロジェクトレベルのインストラクションファイル**を自動的に読み込みます。`/agent` は不要です。`AGENTS.md`、`.instructions.md`、`/init` については以下の [Copilot のプロジェクト設定](#configuring-your-project-for-copilot) を参照してください。

</details>

---

<a id="configuring-your-project-for-copilot"></a>
<details>
<summary><strong>Copilot のプロジェクト設定</strong> - AGENTS.md、インストラクションファイル、/init セットアップ</summary>

## Copilot のプロジェクト設定

エージェントはオンデマンドで呼び出すスペシャリストです。**プロジェクト設定ファイル**は異なります：Copilot はすべてのセッションで自動的にそれらを読み込み、プロジェクトの規約、技術スタック、ルールを理解します。`/agent` を実行する必要はありません。リポジトリで作業するすべての人にコンテキストが常に有効です。

### /init によるクイックセットアップ

始める最も簡単な方法は、Copilot に設定ファイルを生成させることです：

```bash
copilot
> /init
```

Copilot がプロジェクトをスキャンし、カスタマイズされたインストラクションファイルを作成します。後から編集できます。

### インストラクションファイルの形式

| ファイル | スコープ | 備考 |
|---------|---------|------|
| `AGENTS.md` | プロジェクトルートまたはネスト | **クロスプラットフォーム標準** - Copilot や他の AI アシスタントで動作 |
| `.github/copilot-instructions.md` | プロジェクト | GitHub Copilot 固有 |
| `.github/instructions/*.instructions.md` | プロジェクト | 細かいトピック別の指示 |
| `CLAUDE.md`、`GEMINI.md` | プロジェクトルート | 互換性のためにサポート |

> 🎯 **始めたばかり？** プロジェクトの指示には `AGENTS.md` を使いましょう。他の形式は必要に応じて後で調べればOKです。

### AGENTS.md

`AGENTS.md` は推奨される形式です。Copilot や他の AI コーディングツールで動作する[オープンスタンダード](https://agents.md/)です。リポジトリルートに配置すれば、Copilot が自動的に読み込みます。このプロジェクト自体の [AGENTS.md](../AGENTS.md) が実際の使用例です。

典型的な `AGENTS.md` にはプロジェクトのコンテキスト、コードスタイル、セキュリティ要件、テスト基準が記述されています。`/init` で生成するか、サンプルファイルのパターンに従って自分で書きましょう。

### カスタムインストラクションファイル（.instructions.md）

より細かい制御が必要なチーム向けに、指示をトピック別のファイルに分割できます。各ファイルは一つの関心事をカバーし、自動的に適用されます：

```
.github/
└── instructions/
    ├── python-standards.instructions.md
    ├── security-checklist.instructions.md
    └── api-design.instructions.md
```

> 💡 **注意**：インストラクションファイルはどの言語でも使えます。この例はコースのプロジェクトに合わせて Python を使用していますが、TypeScript、Go、Rust、その他チームが使う任意の技術で同様のファイルを作成できます。

**コミュニティのインストラクションファイルを探す**：.NET、Angular、Azure、Python、Docker など、多くの技術をカバーする既成のインストラクションファイルは [github/awesome-copilot](https://github.com/github/awesome-copilot) を参照してください。

### カスタムインストラクションの無効化

Copilot にすべてのプロジェクト固有の設定を無視させたい場合（デバッグや動作比較に便利）：

```bash
copilot --no-custom-instructions
```

</details>

---

<a id="agent-file-reference"></a>
<details>
<summary><strong>エージェントファイルリファレンス</strong> - YAML プロパティ、ツールエイリアス、完全な例</summary>

## エージェントファイルリファレンス

### より完全な例

上記の[最小限のエージェント形式](#-エージェントを追加する)を見ました。ここでは `tools` プロパティを使用するより包括的なエージェントを紹介します。`~/.copilot/agents/python-reviewer.agent.md` を作成してください：

```markdown
---
name: python-reviewer
description: Python code quality specialist for reviewing Python projects
tools: ["read", "edit", "search", "execute"]
---

# Python Code Reviewer

You are a Python specialist focused on code quality and best practices.

**Your focus areas:**
- Code quality (PEP 8, type hints, docstrings)
- Performance optimization (list comprehensions, generators)
- Error handling (proper exception handling)
- Maintainability (DRY principles, clear naming)

**Code style requirements:**
- Use Python 3.10+ features (dataclasses, type hints, pattern matching)
- Follow PEP 8 naming conventions
- Use context managers for file I/O
- All functions must have type hints and docstrings

**When reviewing code, always check:**
- Missing type hints on function signatures
- Mutable default arguments
- Proper error handling (no bare except)
- Input validation completeness
```

### YAML プロパティ

| プロパティ | 必須 | 説明 |
|-----------|------|------|
| `name` | いいえ | 表示名（デフォルトはファイル名） |
| `description` | **はい** | エージェントの機能 - Copilot がいつ提案すべきか理解するのに役立ちます |
| `tools` | いいえ | 許可するツールのリスト（省略 = すべてのツールが利用可能）。以下のツールエイリアスを参照 |
| `target` | いいえ | `vscode` または `github-copilot` のみに制限 |

### ツールエイリアス

`tools` リストで以下の名前を使用します：
- `read` - ファイルの内容を読み取る
- `edit` - ファイルを編集する
- `search` - ファイルを検索する（grep/glob）
- `execute` - シェルコマンドを実行する（`shell`、`Bash` も可）
- `agent` - 他のカスタムエージェントを呼び出す

> 📖 **公式ドキュメント**：[Custom agents configuration](https://docs.github.com/copilot/reference/custom-agents-configuration)
>
> ⚠️ **VS Code のみ**：`model` プロパティ（AI モデルの選択用）は VS Code では動作しますが、GitHub Copilot CLI ではサポートされていません。クロスプラットフォームのエージェントファイルに安全に含めることができます。GitHub Copilot CLI はそれを無視します。

### その他のエージェントテンプレート

> 💡 **初心者向けの注意**：以下の例はテンプレートです。**記載されている具体的な技術を、あなたのプロジェクトで使用しているものに置き換えてください。** 重要なのは、言及されている特定の技術ではなく、エージェントの*構造*です。

このプロジェクトには [.github/agents/](../.github/agents/) フォルダに動作するサンプルが含まれています：
- [hello-world.agent.md](../.github/agents/hello-world.agent.md) - 最小限の例、ここから始めましょう
- [python-reviewer.agent.md](../.github/agents/python-reviewer.agent.md) - Python コード品質レビュアー
- [pytest-helper.agent.md](../.github/agents/pytest-helper.agent.md) - pytest テスト専門家

コミュニティエージェントについては [github/awesome-copilot](https://github.com/github/awesome-copilot) を参照してください。

</details>

---

# 実践

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

独自のエージェントを作成して、実際に動作させてみましょう。

---

## ▶️ 自分で試してみよう

```bash

# エージェントディレクトリを作成（存在しない場合）
mkdir -p .github/agents

# コードレビュアーエージェントを作成
cat > .github/agents/reviewer.agent.md << 'EOF'
---
name: reviewer
description: Senior code reviewer focused on security and best practices
---

# Code Reviewer Agent

You are a senior code reviewer focused on code quality.

**Review priorities:**
1. Security vulnerabilities
2. Performance issues
3. Maintainability concerns
4. Best practice violations

**Output format:**
Provide issues as a numbered list with severity tags:
[CRITICAL], [HIGH], [MEDIUM], [LOW]
EOF

# ドキュメントエージェントを作成
cat > .github/agents/documentor.agent.md << 'EOF'
---
name: documentor
description: Technical writer for clear and complete documentation
---

# Documentation Agent

You are a technical writer who creates clear documentation.

**Documentation standards:**
- Start with a one-sentence summary
- Include usage examples
- Document parameters and return values
- Note any gotchas or limitations
EOF

# エージェントを使ってみましょう
copilot --agent reviewer
> Review @samples/book-app-project/books.py

# エージェントを切り替える
copilot
> /agent
# "documentor" を選択
> Document @samples/book-app-project/books.py
```

---

## 📝 課題

### メインチャレンジ：専門エージェントチームの構築

ハンズオンの例で `reviewer` と `documentor` エージェントを作成しました。次は、別のタスクのためにエージェントを作成して使う練習をしましょう - ブックアプリのデータバリデーションの改善です：

1. `.github/agents/` に配置するエージェントファイル（`.agent.md`）を3つ作成（エージェントごとに1つ）
2. 作成するエージェント：
   - **data-validator**：`data.json` の欠落データや不正なデータをチェック（空の著者名、year=0、欠落フィールド）
   - **error-handler**：Python コードの一貫性のないエラーハンドリングをレビューし、統一的なアプローチを提案
   - **doc-writer**：docstring や README コンテンツを生成または更新
3. 各エージェントをブックアプリで使用：
   - `data-validator` → `@samples/book-app-project/data.json` を監査
   - `error-handler` → `@samples/book-app-project/books.py` と `@samples/book-app-project/utils.py` をレビュー
   - `doc-writer` → `@samples/book-app-project/books.py` に docstring を追加
4. コラボレーション：`error-handler` でエラーハンドリングのギャップを特定し、次に `doc-writer` で改善されたアプローチをドキュメント化

**成功基準**：一貫性のある高品質な出力を生成する3つの動作するエージェントがあり、`/agent` で切り替えられること。

<details>
<summary>💡 ヒント（クリックして展開）</summary>

**スターターテンプレート**：`.github/agents/` にエージェントごとに1つのファイルを作成：

`data-validator.agent.md`:
```markdown
---
description: Analyzes JSON data files for missing or malformed entries
---

You analyze JSON data files for missing or malformed entries.

**Focus areas:**
- Empty or missing author fields
- Invalid years (year=0, future years, negative years)
- Missing required fields (title, author, year, read)
- Duplicate entries
```

`error-handler.agent.md`:
```markdown
---
description: Reviews Python code for error handling consistency
---

You review Python code for error handling consistency.

**Standards:**
- No bare except clauses
- Use custom exceptions where appropriate
- All file operations use context managers
- Consistent return types for success/failure
```

`doc-writer.agent.md`:
```markdown
---
description: Technical writer for clear Python documentation
---

You are a technical writer who creates clear Python documentation.

**Standards:**
- Google-style docstrings
- Include parameter types and return values
- Add usage examples for public methods
- Note any exceptions raised
```

**エージェントのテスト：**

> 💡 **注意：** ローカルリポジトリに `samples/book-app-project/data.json` がすでにあるはずです。もし見つからない場合は、ソースリポジトリからオリジナル版をダウンロードしてください：
> [data.json](https://github.com/github/copilot-cli-for-beginners/blob/main/samples/book-app-project/data.json)

```bash
copilot
> /agent
# リストから "data-validator" を選択
> @samples/book-app-project/data.json Check for books with empty author fields or invalid years
```

**ヒント：** YAML フロントマターの `description` フィールドはエージェントが動作するために必須です。

</details>

### ボーナスチャレンジ：インストラクションライブラリ

オンデマンドで呼び出すエージェントを構築しました。次はもう一方の側を試しましょう：`/agent` なしで Copilot がすべてのセッションで自動的に読み込む**インストラクションファイル**です。

`.github/instructions/` フォルダを作成し、少なくとも3つのインストラクションファイルを含めてください：
- `python-style.instructions.md` - PEP 8 と型ヒントの規約を強制
- `test-standards.instructions.md` - テストファイルでの pytest 規約を強制
- `data-quality.instructions.md` - JSON データエントリのバリデーション

各インストラクションファイルをブックアプリのコードでテストしてください。

---

<details>
<summary>🔧 <strong>よくある間違いとトラブルシューティング</strong>（クリックして展開）</summary>

### よくある間違い

| 間違い | 発生する問題 | 修正方法 |
|-------|------------|---------|
| エージェントのフロントマターに `description` がない | エージェントが読み込まれないか検出されない | YAML フロントマターに必ず `description:` を含める |
| エージェントのファイル配置場所が間違っている | 使用時にエージェントが見つからない | `~/.copilot/agents/`（個人用）または `.github/agents/`（プロジェクト用）に配置 |
| `.agent.md` ではなく `.md` を使用 | ファイルがエージェントとして認識されない場合がある | `python-reviewer.agent.md` のような名前にする |
| エージェントプロンプトが長すぎる | 30,000文字の制限に達する可能性がある | エージェント定義は焦点を絞り、詳細な指示にはスキルを使用 |

### トラブルシューティング

**エージェントが見つからない** - エージェントファイルが以下のいずれかの場所に存在するか確認してください：
- `~/.copilot/agents/`
- `.github/agents/`

利用可能なエージェントの一覧を表示：

```bash
copilot
> /agent
# 利用可能なすべてのエージェントを表示
```

**エージェントが指示に従わない** - プロンプトを明確にし、エージェント定義により多くの詳細を追加してください：
- バージョンを含む具体的なフレームワーク/ライブラリ
- チームの規約
- コードパターンの例

**カスタムインストラクションが読み込まれない** - プロジェクトで `/init` を実行してプロジェクト固有の指示をセットアップしてください：

```bash
copilot
> /init
```

または無効になっていないか確認してください：
```bash
# カスタムインストラクションを読み込みたい場合は --no-custom-instructions を使用しないでください
copilot  # デフォルトでカスタムインストラクションを読み込みます
```

</details>

---

# まとめ

## 🔑 重要なポイント

1. **組み込みエージェント**：`/plan` と `/review` は直接呼び出し、Explore と Task は自動的に動作
2. **カスタムエージェント**は `.agent.md` ファイルで定義されたスペシャリスト
3. **良いエージェント**は明確な専門性、基準、出力形式を持つ
4. **マルチエージェント連携**は専門知識を組み合わせて複雑な問題を解決
5. **インストラクションファイル**（`.instructions.md`）はチームの基準を自動適用のためにエンコード
6. **一貫した出力**は適切に定義されたエージェントの指示から生まれる

> 📋 **クイックリファレンス**：コマンドとショートカットの完全なリストは [GitHub Copilot CLI command reference](https://docs.github.com/en/copilot/reference/cli-command-reference) を参照してください。

---

## ➡️ 次のステップ

エージェントは Copilot がコードに対して*どのようにアプローチし、ターゲットを絞ったアクションを取るか*を変えます。次は、**スキル** - Copilot が*どのステップ*に従うかを変えるものを学びます。エージェントとスキルの違いが気になりますか？Chapter 05 で正面から取り上げます。

**[Chapter 05: Skills System](../05-skills/README.ja.md)** では、以下を学びます：

- プロンプトからスキルが自動トリガーされる仕組み（スラッシュコマンド不要）
- コミュニティスキルのインストール
- SKILL.md ファイルによるカスタムスキルの作成
- エージェント、スキル、MCP の違い
- それぞれをいつ使うか

---

**[← Chapter 03 に戻る](../03-development-workflows/README.ja.md)** | **[Chapter 05 へ進む →](../05-skills/README.ja.md)**
