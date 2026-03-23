![Chapter 02: コンテキストと会話](images/chapter-header.png)

> **AIがファイル1つずつではなく、コードベース全体を見渡せるとしたら？**

この章では、GitHub Copilot CLI の真の力、コンテキストを活用する方法を学びます。`@` 構文を使ってファイルやディレクトリを参照し、Copilot CLI にコードベースを深く理解させる方法を習得します。セッションをまたいで会話を維持し、数日後に中断した箇所から正確に作業を再開する方法や、クロスファイル解析が単一ファイルのレビューでは見逃してしまうバグをどのようにキャッチするかを学びます。

## 🎯 学習目標

この章を終えると、以下のことができるようになります：

- `@` 構文を使ってファイル、ディレクトリ、画像を参照する
- `--resume` と `--continue` で以前のセッションを再開する
- [コンテキストウィンドウ](../GLOSSARY.md#context-window)の仕組みを理解する
- 効果的なマルチターン会話を行う
- 複数プロジェクトのワークフローでディレクトリ権限を管理する

> ⏱️ **所要時間目安**: 約50分（読み物20分 + ハンズオン30分）

---

## 🧩 実例アナロジー：同僚との作業

<img src="images/colleague-context-analogy.png" alt="Context Makes the Difference - Without vs With Context" width="800"/>

*同僚と同じように、Copilot CLI は心を読めるわけではありません。より多くの情報を提供することで、人間も Copilot もより的確なサポートができるようになります！*

同僚にバグを説明するときを想像してみてください：

> **コンテキストなし**: 「ブックアプリが動かないんだけど。」

> **コンテキストあり**: 「`books.py` を見てほしいんだけど、特に `find_book_by_title` 関数。大文字小文字を区別しない検索ができていないんだ。」

Copilot CLI にコンテキストを提供するには、*`@` 構文*を使って特定のファイルを指し示します。

---

# 必須：基本コンテキスト

<img src="images/essential-basic-context.png" alt="Glowing code blocks connected by light trails representing how context flows through Copilot CLI conversations" width="800"/>

このセクションでは、コンテキストを効果的に活用するために必要なすべてを網羅します。まずこの基本をマスターしましょう。

---

## @ 構文

`@` シンボルはプロンプト内でファイルやディレクトリを参照するために使います。Copilot CLI に「このファイルを見て」と伝える方法です。

> 💡 **メモ**: このコースのすべての例はリポジトリに含まれる `samples/` フォルダを使用しているので、すべてのコマンドを直接試すことができます。

### 今すぐ試してみよう（セットアップ不要）

お使いのコンピュータにある任意のファイルで試せます：

```bash
copilot

# 任意のファイルを指定する
> Explain what @package.json does
> Summarize @README.md
> What's in @.gitignore and why?
```

> 💡 **手元にプロジェクトがない場合** 簡単なテストファイルを作成できます：
> ```bash
> echo "def greet(name): return 'Hello ' + name" > test.py
> copilot
> > What does @test.py do?
> ```

### 基本的な @ パターン

| パターン | 動作 | 使用例 |
|---------|------|--------|
| `@file.py` | 単一ファイルを参照 | `Review @samples/book-app-project/books.py` |
| `@folder/` | ディレクトリ内のすべてのファイルを参照 | `Review @samples/book-app-project/` |
| `@file1.py @file2.py` | 複数ファイルを参照 | `Compare @samples/book-app-project/book_app.py @samples/book-app-project/books.py` |

### 単一ファイルの参照

```bash
copilot

> Explain what @samples/book-app-project/utils.py does
```

---

<details>
<summary>🎬 実際の動作を見る！</summary>

![File Context Demo](images/file-context-demo.gif)

*デモの出力は異なる場合があります。使用するモデル、ツール、レスポンスはここに示されているものと異なります。*

</details>

---

### 複数ファイルの参照

```bash
copilot

> Compare @samples/book-app-project/book_app.py and @samples/book-app-project/books.py for consistency
```

### ディレクトリ全体の参照

```bash
copilot

> Review all files in @samples/book-app-project/ for error handling
```

---

## クロスファイルインテリジェンス

ここからコンテキストがスーパーパワーになります。単一ファイルの解析は便利ですが、クロスファイル解析は変革をもたらします。

<img src="images/cross-file-intelligence.png" alt="Cross-File Intelligence - comparing single-file vs cross-file analysis showing how analyzing files together reveals bugs, data flow, and patterns invisible in isolation" width="800"/>

### デモ：複数ファイルにまたがるバグを発見する

```bash
copilot

> @samples/book-app-project/book_app.py @samples/book-app-project/books.py
>
> How do these files work together? What's the data flow?
```

> 💡 **上級者向けオプション**: セキュリティに焦点を当てたクロスファイル解析には、Python セキュリティの例を試してください：
> ```bash
> > @samples/buggy-code/python/user_service.py @samples/buggy-code/python/payment_processor.py
> > Find security vulnerabilities that span BOTH files
> ```

---

<details>
<summary>🎬 実際の動作を見る！</summary>

![Multi-File Demo](images/multi-file-demo.gif)

*デモの出力は異なる場合があります。使用するモデル、ツール、レスポンスはここに示されているものと異なります。*

</details>

---

**Copilot CLI が発見する内容**:

```
Cross-Module Analysis
=====================

1. DATA FLOW PATTERN
   book_app.py creates BookCollection instance and calls methods
   books.py defines BookCollection class and manages data persistence

   Flow: book_app.py (UI) → books.py (business logic) → data.json (storage)

2. DUPLICATE DISPLAY FUNCTIONS
   book_app.py:9-21    show_books() function
   utils.py:28-36      print_books() function

   Impact: Two nearly identical functions doing the same thing. If you update
   one (like changing the format), you must remember to update the other.

3. INCONSISTENT ERROR HANDLING
   book_app.py handles ValueError from year conversion
   books.py silently returns None/False on errors

   Pattern: No unified approach to error handling across modules
```

**これが重要な理由**: 単一ファイルのレビューでは全体像を見逃してしまいます。クロスファイル解析でのみ以下が明らかになります：
- **重複コード** — 統合すべきもの
- **データフローパターン** — コンポーネント間の連携の仕組み
- **アーキテクチャの問題** — 保守性に影響するもの

---

### デモ：60秒でコードベースを理解する

<img src="images/codebase-understanding.png" alt="Split-screen comparison showing manual code review taking 1 hour versus AI-assisted analysis taking 10 seconds" width="800" />

プロジェクトに初めて参加する場合、Copilot CLI を使って素早く学べます。

```bash
copilot

> @samples/book-app-project/
>
> In one paragraph, what does this app do and what are its biggest quality issues?
```

**得られる結果**:
```
This is a CLI book collection manager that lets users add, list, remove, and
search books stored in a JSON file. The biggest quality issues are:

1. Duplicate display logic - show_books() and print_books() do the same thing
2. Inconsistent error handling - some errors raise exceptions, others return False
3. No input validation - year can be 0, empty strings accepted for title/author
4. Missing tests - no test coverage for critical functions like find_book_by_title

Priority fix: Consolidate duplicate display functions and add input validation.
```

**結果**: コードを1時間かけて読む作業が10秒に圧縮されます。どこに集中すべきかが正確にわかります。

---

## 実践的な例

### 例 1: コンテキストを使ったコードレビュー

```bash
copilot

> @samples/book-app-project/books.py Review this file for potential bugs

# Copilot CLI はファイル全体の内容を持っているため、具体的なフィードバックができます：
# "Line 49: Case-sensitive comparison may miss books..."
# "Line 29: JSON decode errors are caught but data corruption isn't logged..."

> What about @samples/book-app-project/book_app.py?

# book_app.py をレビューしつつ、books.py のコンテキストも保持しています
```

### 例 2: コードベースの理解

```bash
copilot

> @samples/book-app-project/books.py What does this module do?

# Copilot CLI は books.py を読み込み、BookCollection クラスを理解します

> @samples/book-app-project/ Give me an overview of the code structure

# Copilot CLI はディレクトリをスキャンして要約します

> How does the app save and load books?

# Copilot CLI は既に見たコードをたどることができます
```

<details>
<summary>🎬 マルチターン会話の動作を見る！</summary>

![Multi-Turn Demo](images/multi-turn-demo.gif)

*デモの出力は異なる場合があります。使用するモデル、ツール、レスポンスはここに示されているものと異なります。*

</details>

### 例 3: マルチファイルリファクタリング

```bash
copilot

> @samples/book-app-project/book_app.py @samples/book-app-project/utils.py
> I see duplicate display functions: show_books() and print_books(). Help me consolidate these.

# Copilot CLI は両方のファイルを見て、重複コードの統合方法を提案できます
```

---

## セッション管理

作業中にセッションは自動的に保存されます。以前のセッションを再開して、中断した箇所から続けることができます。

### セッションの自動保存

すべての会話は自動的に保存されます。通常通り終了するだけです：

```bash
copilot

> @samples/book-app-project/ Let's improve error handling across all modules

[... 作業を行う ...]

> /exit
```

### 最新のセッションを再開

```bash
# 中断した箇所から続ける
copilot --continue
```

### 特定のセッションを再開

```bash
# セッション一覧からインタラクティブに選択
copilot --resume

# または特定のセッションIDで再開
copilot --resume abc123
```

> 💡 **セッションIDはどうやって見つけるの？** 暗記する必要はありません。IDなしで `copilot --resume` を実行すると、過去のセッションの名前、ID、最終アクティブ時刻がインタラクティブなリストで表示されます。必要なものを選ぶだけです。
>
> **複数のターミナルではどうなるの？** 各ターミナルウィンドウはそれぞれ独立したセッションで、独自のコンテキストを持ちます。3つのターミナルで Copilot CLI を開いていれば、3つの別々のセッションになります。どのターミナルからでも `--resume` を実行すれば、すべてのセッションを閲覧できます。`--continue` フラグは、どのターミナルで閉じたかに関係なく、最も最近閉じたセッションを取得します。
>
> **再起動せずにセッションを切り替えられる？** はい。アクティブなセッション内から `/resume` スラッシュコマンドを使います：
> ```
> > /resume
> # 切り替え先のセッション一覧が表示されます
> ```

### セッションの整理

後で見つけやすいように、セッションにわかりやすい名前をつけましょう：

```bash
copilot

> /rename book-app-review
# セッションの名前が変更され、識別しやすくなります
```

### コンテキストの確認と管理

ファイルや会話を追加するにつれて、Copilot CLI の[コンテキストウィンドウ](../GLOSSARY.md#context-window)が埋まっていきます。2つのコマンドで管理できます：

```bash
copilot

> /context
Context usage: 45,000 / 128,000 tokens (35%)

> /clear
# コンテキストを消去してリフレッシュします。トピックを切り替えるときに使います
```

> 💡 **`/clear` を使うタイミング**: `books.py` をレビューしていて `utils.py` の話題に切り替えたい場合は、先に `/clear` を実行してください。そうしないと、古いトピックの古いコンテキストがレスポンスを混乱させる可能性があります。

---

### 中断した箇所から再開する

<img src="images/session-persistence-timeline.png" alt="Timeline showing how GitHub Copilot CLI sessions persist across days - start on Monday, resume on Wednesday with full context restored" width="800"/>

*セッションは終了時に自動保存されます。数日後でもフルコンテキストで再開：ファイル、課題、進捗がすべて記憶されています。*

数日にわたるワークフローを想像してみてください：

```bash
# 月曜日: ブックアプリのレビューを開始
copilot

> /rename book-app-review
> @samples/book-app-project/books.py
> Review and number all code quality issues

Quality Issues Found:
1. Duplicate display functions (book_app.py & utils.py) - MEDIUM
2. No input validation for empty strings - MEDIUM
3. Year can be 0 or negative - LOW
4. No type hints on all functions - LOW
5. Missing error logging - LOW

> Fix issue #1 (duplicate functions)
# 修正作業...

> /exit
```

```bash
# 水曜日: 中断した箇所からそのまま再開
copilot --continue

> What issues remain unfixed from our book app review?

Remaining issues from our book-app-review session:
2. No input validation for empty strings - MEDIUM
3. Year can be 0 or negative - LOW
4. No type hints on all functions - LOW
5. Missing error logging - LOW

Issue #1 (duplicate functions) was fixed on Monday.

> Let's tackle issue #2 next
```

**これが強力な理由**: 数日後でも、Copilot CLI は以下を記憶しています：
- 作業していた正確なファイル
- 番号付きの課題リスト
- すでに対処した項目
- 会話のコンテキスト

再説明の必要なし。ファイルの再読み込みも不要。作業を続けるだけです。

---

**🎉 これで基本はマスターです！** `@` 構文、セッション管理（`--continue`/`--resume`/`/rename`）、コンテキストコマンド（`/context`/`/clear`）があれば十分に生産的に作業できます。以下はすべてオプションです。準備ができたら戻ってきてください。

---

# オプション：さらに深く

<img src="images/optional-going-deeper.png" alt="Abstract crystal cave in blue and purple tones representing deeper exploration of context concepts" width="800"/>

これらのトピックは上記の基本の上に構築されます。**興味のあるものを選ぶか、[練習](#practice)に進んでください。**

| 学びたいこと... | ジャンプ先 |
|---|---|
| ワイルドカードパターンと追加セッションコマンド | [追加の @ パターンとセッションコマンド](#additional-patterns) |
| 複数のプロンプトにまたがるコンテキストの構築 | [コンテキストを意識した会話](#context-aware-conversations) |
| トークン制限と `/compact` | [コンテキストウィンドウの理解](#understanding-context-windows) |
| 参照すべきファイルの選び方 | [参照するものの選び方](#choosing-what-to-reference) |
| スクリーンショットやモックアップの解析 | [画像の操作](#working-with-images) |

<details>
<summary><strong>追加の @ パターンとセッションコマンド</strong></summary>
<a id="additional-patterns"></a>

### 追加の @ パターン

パワーユーザー向けに、Copilot CLI はワイルドカードパターンと画像参照をサポートしています：

| パターン | 動作 |
|---------|------|
| `@folder/*.py` | フォルダ内のすべての .py ファイル |
| `@**/test_*.py` | 再帰的ワイルドカード：任意の場所のすべてのテストファイルを検索 |
| `@image.png` | UIレビュー用の画像ファイル |

```bash
copilot

> Find all TODO comments in @samples/book-app-project/**/*.py
```

### セッション情報の表示

```bash
copilot

> /session
# 現在のセッション詳細とワークスペースの概要を表示

> /usage
# セッションのメトリクスと統計を表示
```

### セッションの共有

```bash
copilot

> /share file ./my-session.md
# セッションをマークダウンファイルとしてエクスポート

> /share gist
# セッションの GitHub gist を作成
```

</details>

<details>
<summary><strong>コンテキストを意識した会話</strong></summary>
<a id="context-aware-conversations"></a>

### コンテキストを意識した会話

マジックは、互いに積み重なるマルチターン会話で起こります。

#### 例：段階的な改善

```bash
copilot

> @samples/book-app-project/books.py Review the BookCollection class

Copilot CLI: "The class looks functional, but I notice:
1. Missing type hints on some methods
2. No validation for empty title/author
3. Could benefit from better error handling"

> Add type hints to all methods

Copilot CLI: "Here's the class with complete type hints..."
[型付きバージョンを表示]

> Now improve error handling

Copilot CLI: "Building on the typed version, here's improved error handling..."
[バリデーションと適切な例外を追加]

> Generate tests for this final version

Copilot CLI: "Based on the class with types and error handling..."
[包括的なテストを生成]
```

各プロンプトが前の作業の上に構築されていることに注目してください。これがコンテキストの力です。

</details>

<details>
<summary><strong>コンテキストウィンドウの理解</strong></summary>
<a id="understanding-context-windows"></a>

### コンテキストウィンドウの理解

基本セクションで `/context` と `/clear` は学びました。ここではコンテキストウィンドウの仕組みをより深く解説します。

すべてのAIには「コンテキストウィンドウ」があります。これは一度に考慮できるテキストの量のことです。

<img src="images/context-window-visualization.png" alt="Context Window Visualization" width="800"/>

*コンテキストウィンドウはデスクのようなもの：一度に置けるものには限りがあります。ファイル、会話履歴、システムプロンプトのすべてがスペースを使います。*

#### 上限に達したときの動作

```bash
copilot

> /context

Context usage: 45,000 / 128,000 tokens (35%)

# ファイルや会話を追加するにつれて増加します

> @large-codebase/

Context usage: 120,000 / 128,000 tokens (94%)

# 警告: コンテキスト制限に近づいています

> @another-large-file.py

Context limit reached. Older context will be summarized.
```

#### `/compact` コマンド

コンテキストが埋まりつつあるが会話を失いたくない場合、`/compact` が履歴を要約してトークンを解放します：

```bash
copilot

> /compact
# 会話履歴を要約し、コンテキストスペースを解放します
# 主要な発見事項や決定事項は保持されます
```

#### コンテキスト効率化のヒント

| 状況 | 操作 | 理由 |
|------|------|------|
| 新しいトピックを開始 | `/clear` | 無関係なコンテキストを除去 |
| 長い会話 | `/compact` | 履歴を要約し、トークンを解放 |
| 特定のファイルが必要 | `@folder/` ではなく `@file.py` | 必要なものだけを読み込む |
| 上限に到達 | 新しいセッションを開始 | フレッシュな128Kコンテキスト |
| 複数のトピック | トピックごとに `/rename` を使用 | 正しいセッションを簡単に再開 |

#### 大規模コードベースのベストプラクティス

1. **具体的に指定**: `@samples/book-app-project/` ではなく `@samples/book-app-project/books.py`
2. **トピック間でクリア**: 焦点を切り替えるときは `/clear` を使用
3. **`/compact` を活用**: 会話を要約してコンテキストを解放
4. **複数セッションを使用**: 機能やトピックごとに1セッション

</details>

<details>
<summary><strong>参照するものの選び方</strong></summary>
<a id="choosing-what-to-reference"></a>

### 参照するものの選び方

コンテキストにおいて、すべてのファイルが同等ではありません。賢く選ぶ方法を説明します：

#### ファイルサイズの考慮

| ファイルサイズ | おおよその[トークン](../GLOSSARY.md#token)数 | 戦略 |
|-------------|-------------------|------|
| 小（100行未満） | 約500〜1,500トークン | 自由に参照してOK |
| 中（100〜500行） | 約1,500〜7,500トークン | 特定のファイルを参照 |
| 大（500行以上） | 7,500トークン以上 | 選択的に、特定のファイルを使用 |
| 非常に大きい（1000行以上） | 15,000トークン以上 | 分割するかセクションを絞ることを検討 |

**具体例：**
- ブックアプリの4つの Python ファイル合計 ≈ 2,000〜3,000トークン
- 典型的な Python モジュール（200行）≈ 3,000トークン
- Flask API ファイル（400行）≈ 6,000トークン
- package.json ≈ 200〜500トークン
- 短いプロンプト + レスポンス ≈ 500〜1,500トークン

> 💡 **コードの簡易見積もり:** コードの行数に約15を掛けるとおおよそのトークン数がわかります。これはあくまで推定値であることに注意してください。

#### 含めるべきものと除外すべきもの

**高い価値**（含めるべき）：
- エントリポイント（`book_app.py`、`main.py`、`app.py`）
- 質問対象の特定のファイル
- ターゲットファイルが直接インポートしているファイル
- 設定ファイル（`requirements.txt`、`pyproject.toml`）
- データモデルやデータクラス

**低い価値**（除外を検討）：
- 生成ファイル（コンパイル出力、バンドル済みアセット）
- Node modules やベンダーディレクトリ
- 大きなデータファイルやフィクスチャ
- 質問に関係のないファイル

#### 具体性のスペクトラム

```
低い具体性 ────────────────────────► 高い具体性
@samples/book-app-project/                      @samples/book-app-project/books.py:47-52
     │                                       │
     └─ すべてをスキャン                      └─ 必要なものだけ
        （コンテキストを多く使用）                  （コンテキストを節約）
```

**広く指定すべき場合** (`@samples/book-app-project/`):
- 初期のコードベース探索
- 多数のファイルにまたがるパターンの発見
- アーキテクチャレビュー

**具体的に指定すべき場合** (`@samples/book-app-project/books.py`):
- 特定の問題のデバッグ
- 特定ファイルのコードレビュー
- 単一の関数についての質問

#### 実践例：段階的コンテキスト読み込み

```bash
copilot

# ステップ 1: 構造から始める
> @package.json What frameworks does this project use?

# ステップ 2: 回答に基づいて絞り込む
> @samples/book-app-project/ Show me the project structure

# ステップ 3: 重要なものにフォーカス
> @samples/book-app-project/books.py Review the BookCollection class

# ステップ 4: 必要に応じて関連ファイルを追加
> @samples/book-app-project/book_app.py @samples/book-app-project/books.py How does the CLI use the BookCollection?
```

この段階的アプローチにより、コンテキストを集中的かつ効率的に保てます。

</details>

<details>
<summary><strong>画像の操作</strong></summary>
<a id="working-with-images"></a>

### 画像の操作

`@` 構文を使って会話に画像を含めることも、単に**クリップボードから貼り付ける**（Cmd+V / Ctrl+V）こともできます。Copilot CLI はスクリーンショット、モックアップ、ダイアグラムを解析して、UIのデバッグ、デザインの実装、エラー分析を支援します。

```bash
copilot

> @images/screenshot.png What is happening in this image?

> @images/mockup.png Write the HTML and CSS to match this design. Place it in a new file called index.html and put the CSS in styles.css.
```

> 📖 **詳細**: サポートされている形式、実践的なユースケース、画像とコードの組み合わせ方のヒントについては、[追加のコンテキスト機能](../appendices/additional-context.md#working-with-images)を参照してください。

</details>

---

# 練習

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

コンテキストとセッション管理のスキルを実践する時間です。

---

## ▶️ 自分で試してみよう

### フルプロジェクトレビュー

コースにはそのままレビューできるサンプルファイルが含まれています。copilot を起動して、次に示すプロンプトを実行してください：

```bash
copilot

> @samples/book-app-project/ Give me a code quality review of this project

# Copilot CLI は以下のような問題を特定します：
# - 重複した表示関数
# - 入力バリデーションの欠如
# - 一貫性のないエラーハンドリング
```

> 💡 **自分のファイルで試したい場合** 小さな Python プロジェクトを作成し（`mkdir -p my-project/src`）、.py ファイルを追加して、`@my-project/src/` でレビューしてみてください。必要であれば、copilot にサンプルコードを作成してもらうこともできます！

### セッションワークフロー

```bash
copilot

> /rename book-app-review
> @samples/book-app-project/books.py Let's add input validation for empty titles

[Copilot CLI がバリデーションのアプローチを提案]

> Implement that fix
> Now consolidate the duplicate display functions in @samples/book-app-project/
> /exit

# 後で - 中断した箇所から再開
copilot --continue

> Generate tests for the changes we made
```

---

デモを完了したら、以下のバリエーションを試してみてください：

1. **クロスファイルチャレンジ**: book_app.py と books.py がどのように連携しているかを分析：
   ```bash
   copilot
   > @samples/book-app-project/book_app.py @samples/book-app-project/books.py
   > What's the relationship between these files? Are there any code smells?
   ```

2. **セッションチャレンジ**: セッションを開始し、`/rename my-first-session` で名前をつけ、何か作業をして、`/exit` で終了し、`copilot --continue` を実行してください。以前やっていたことを覚えていますか？

3. **コンテキストチャレンジ**: セッション中に `/context` を実行してください。何トークン使用していますか？`/compact` を試して再度確認してみましょう。（`/compact` の詳細については、「さらに深く」セクションの[コンテキストウィンドウの理解](#understanding-context-windows)を参照してください。）

**セルフチェック**: `@folder/` が各ファイルを個別に開くよりもなぜ強力なのか説明できれば、コンテキストを理解したと言えます。

---

## 📝 課題

### メインチャレンジ：データフローの追跡

ハンズオンの例ではコード品質レビューと入力バリデーションに焦点を当てました。今度は同じコンテキストスキルを別のタスク、アプリ内のデータの流れの追跡に活用してみましょう：

1. インタラクティブセッションを開始: `copilot`
2. `books.py` と `book_app.py` を一緒に参照:
   `@samples/book-app-project/books.py @samples/book-app-project/book_app.py Trace how a book goes from user input to being saved in data.json. What functions are involved at each step?`
3. 追加コンテキストとしてデータファイルを含める:
   `@samples/book-app-project/data.json What happens if this JSON file is missing or corrupted? Which functions would fail?`
4. クロスファイルの改善を依頼:
   `@samples/book-app-project/books.py @samples/book-app-project/utils.py Suggest a consistent error-handling strategy that works across both files.`
5. セッションの名前変更: `/rename data-flow-analysis`
6. `/exit` で終了し、`copilot --continue` で再開してデータフローについてフォローアップの質問をする

**成功基準**: 複数ファイルにまたがるデータを追跡でき、名前付きセッションを再開でき、クロスファイルの提案を得られること。

<details>
<summary>💡 ヒント（クリックして展開）</summary>

**開始方法：**
```bash
cd /path/to/copilot-cli-for-beginners
copilot
> @samples/book-app-project/books.py @samples/book-app-project/book_app.py Trace how a book goes from user input to being saved in data.json.
> @samples/book-app-project/data.json What happens if this file is missing or corrupted?
> /rename data-flow-analysis
> /exit
```

再開: `copilot --continue`

**便利なコマンド：**
- `@file.py` - 単一ファイルを参照
- `@folder/` - フォルダ内のすべてのファイルを参照（末尾の `/` に注意）
- `/context` - コンテキストの使用量を確認
- `/rename <name>` - セッションに名前をつけて簡単に再開

</details>

### ボーナスチャレンジ：コンテキスト制限

1. `@samples/book-app-project/` でブックアプリのすべてのファイルを一度に参照
2. 異なるファイル（`books.py`、`utils.py`、`book_app.py`、`data.json`）について詳細な質問をいくつか行う
3. `/context` を実行して使用量を確認。どのくらいの速さで埋まりますか？
4. `/compact` を使ってスペースを回復する練習をし、会話を続ける
5. より具体的なファイル参照（フォルダ全体ではなく `@samples/book-app-project/books.py` など）を試して、コンテキスト使用量にどう影響するか確認

---

<details>
<summary>🔧 <strong>よくある間違いとトラブルシューティング</strong>（クリックして展開）</summary>

### よくある間違い

| 間違い | 起こること | 修正方法 |
|--------|----------|---------|
| ファイル名の前の `@` を忘れる | Copilot CLI は "books.py" をプレーンテキストとして扱う | `@samples/book-app-project/books.py` を使ってファイルを参照 |
| セッションが自動的に保持されると思い込む | `copilot` を新しく開始すると以前のコンテキストがすべて失われる | `--continue`（最後のセッション）または `--resume`（セッションを選択）を使用 |
| カレントディレクトリ外のファイルを参照 | 「Permission denied」または「File not found」エラー | `/add-dir /path/to/directory` を使ってアクセスを許可 |
| トピック切り替え時に `/clear` を使わない | 古いコンテキストが新しいトピックのレスポンスを混乱させる | 別のタスクを始める前に `/clear` を実行 |

### トラブルシューティング

**「File not found」エラー** - 正しいディレクトリにいることを確認してください：

```bash
pwd  # カレントディレクトリを確認
ls   # ファイル一覧を表示

# その後 copilot を起動して相対パスを使用
copilot

> Review @samples/book-app-project/books.py
```

**「Permission denied」** - 許可リストにディレクトリを追加してください：

```bash
copilot --add-dir /path/to/directory

# またはセッション内で：
> /add-dir /path/to/directory
```

**コンテキストがすぐに埋まる場合**：
- ファイル参照をより具体的にする
- 異なるトピック間で `/clear` を使用
- 作業を複数のセッションに分割する

</details>

---

# まとめ

## 🔑 重要ポイント

1. **`@` 構文**で Copilot CLI にファイル、ディレクトリ、画像のコンテキストを提供
2. **マルチターン会話**はコンテキストが蓄積されるにつれて互いの上に構築される
3. **セッションは自動保存**: `--continue` または `--resume` で中断した箇所から再開
4. **コンテキストウィンドウ**には制限がある: `/context`、`/clear`、`/compact` で管理
5. **権限フラグ**（`--add-dir`、`--allow-all`）で複数ディレクトリのアクセスを制御。賢く使いましょう！
6. **画像参照**（`@screenshot.png`）でUIの問題を視覚的にデバッグ

> 📚 **公式ドキュメント**: コンテキスト、セッション、ファイル操作の完全なリファレンスは [Use Copilot CLI](https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli) を参照してください。

> 📋 **クイックリファレンス**: コマンドとショートカットの完全なリストは [GitHub Copilot CLI command reference](https://docs.github.com/en/copilot/reference/cli-command-reference) を参照してください。

---

## ➡️ 次のステップ

Copilot CLI にコンテキストを与える方法を学んだので、次は実際の開発タスクに活用しましょう。今学んだコンテキスト技術（ファイル参照、クロスファイル解析、セッション管理）は、次の章の強力なワークフローの基盤となります。

**[Chapter 03: 開発ワークフロー](../03-development-workflows/README.ja.md)**では、以下を学びます：

- コードレビューワークフロー
- リファクタリングパターン
- デバッグ支援
- テスト生成
- Git 連携

---

**[← Chapter 01 に戻る](../01-setup-and-first-steps/README.ja.md)** | **[Chapter 03 に進む →](../03-development-workflows/README.ja.md)**
