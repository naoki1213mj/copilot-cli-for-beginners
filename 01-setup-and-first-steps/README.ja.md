![第01章: はじめの一歩](images/chapter-header.png)

> **AIが瞬時にバグを見つけ、難解なコードを解説し、動作するスクリプトを生成する様子をご覧ください。そして、GitHub Copilot CLIの3つの使い方を学びましょう。**

この章から本格的な体験が始まります！開発者たちがGitHub Copilot CLIを「いつでも相談できるシニアエンジニア」と表現する理由を、実際に体験していただきます。AIが数秒でセキュリティバグを発見し、複雑なコードをわかりやすく解説し、動作するスクリプトを即座に生成する様子を目にするでしょう。そして、3つのインタラクションモード（Interactive、Plan、Programmatic）をマスターし、どんなタスクにどのモードを使うべきか正確に判断できるようになります。

> ⚠️ **前提条件**: まず **[第00章: クイックスタート](../00-quick-start/README.ja.md)** を完了してください。以下のデモを実行するには、GitHub Copilot CLIがインストールされ、認証が完了している必要があります。

## 🎯 学習目標

この章を終えると、以下のことができるようになります：

- ハンズオンデモを通じてGitHub Copilot CLIがもたらす生産性の向上を体験する
- タスクに応じて適切なモード（Interactive、Plan、Programmatic）を選択する
- スラッシュコマンドを使ってセッションを制御する

> ⏱️ **所要時間の目安**: 約45分（読む時間15分 + ハンズオン30分）

---

# 初めてのCopilot CLI体験

<img src="images/first-copilot-experience.png" alt="Developer sitting at a desk with code on the monitor and glowing particles representing AI assistance" width="800"/>

さっそくCopilot CLIで何ができるか体験してみましょう。

---

## まずは慣れよう：最初のプロンプト

印象的なデモに入る前に、今すぐ試せるシンプルなプロンプトから始めましょう。**コードリポジトリは不要です**！ターミナルを開いてCopilot CLIを起動するだけです：

```bash
copilot
```

以下の初心者向けプロンプトを試してみてください：

```
> Explain what a dataclass is in Python in simple terms

> Write a function that sorts a list of dictionaries by a specific key

> What's the difference between a list and a tuple in Python?

> Give me 5 best practices for writing clean Python code
```

Pythonを使っていない方もご安心ください！お好みの言語について質問すればOKです。

自然な会話のように感じられることに気づくでしょう。同僚に質問するように聞くだけです。探索が終わったら、`/exit` と入力してセッションを終了します。

**重要なポイント**: GitHub Copilot CLIは会話型です。始めるのに特別な構文は必要ありません。自然な言葉で質問するだけです。

## 実際に動かしてみよう

それでは、開発者たちが「いつでも相談できるシニアエンジニア」と呼ぶ理由を見ていきましょう。

> 📖 **サンプルの読み方**: `>` で始まる行は、Copilot CLIのインタラクティブセッション内で入力するプロンプトです。`>` が付いていない行は、ターミナルで実行するシェルコマンドです。

> 💡 **サンプル出力について**: このコース全体で表示されるサンプル出力は例示です。Copilot CLIの応答は毎回異なるため、あなたの結果は表現、フォーマット、詳細度が異なります。正確なテキストではなく、返される情報の*種類*に注目してください。

### デモ1: 数秒でコードレビュー

このコースには、意図的にコード品質の問題を含むサンプルファイルが付属しています。レビューしてみましょう：

```bash
# ローカルで作業している場合、まだクローンしていなければコースリポジトリをクローン
git clone https://github.com/github/copilot-cli-for-beginners
cd copilot-cli-for-beginners

# Copilotを起動
copilot
```

インタラクティブセッション内で：

```
> Review @samples/book-app-project/book_app.py for code quality issues and suggest improvements
```

> 💡 **`@` とは？** `@` シンボルはCopilot CLIにファイルを読み込むよう指示します。これについては第02章で詳しく学びます。今はコマンドをそのままコピーしてください。

---

<details>
<summary>🎬 実際の動作を見る！</summary>

![Code Review Demo](images/code-review-demo.gif)

*デモの出力は異なります。お使いのモデル、ツール、応答はここに示されているものと異なります。*

</details>

---

**ポイント**: プロフェッショナルなコードレビューが数秒で完了します。手動レビューなら...もっと時間がかかりますよね！

---

### デモ2: 難解なコードの解説

コードを見て何をしているかわからなかったことはありませんか？Copilot CLIセッションで試してみましょう：

```
> Explain what @samples/book-app-project/books.py does in simple terms
```

---

<details>
<summary>🎬 実際の動作を見る！</summary>

![Explain Code Demo](images/explain-code-demo.gif)

*デモの出力は異なります。お使いのモデル、ツール、応答はここに示されているものと異なります。*

</details>

---

**何が起こるか**: （出力は異なります）Copilot CLIがファイルを読み取り、コードを理解し、わかりやすく説明してくれます。

```
This is a book collection management module using Python dataclasses.

Think of it like a digital bookshelf:
- Book is a dataclass - a simple way to store book information (title, author, year, read status)
- BookCollection manages the entire collection and handles saving/loading

Key components:

1. @dataclass decorator (line 8)
   - Automatically creates __init__, __repr__, etc.
   - Clean way to define data structures in Python

2. BookCollection class (line 16)
   - Maintains a list of Book objects
   - Handles persistence with JSON file I/O
   - load_books() reads from data.json
   - save_books() writes to data.json using asdict()

3. Book operations:
   - add_book() - creates and saves new books
   - find_book_by_title() - searches collection
   - mark_as_read() - updates read status
   - find_by_author() - filters by author name

Common pattern: Read from JSON → Work with Python objects → Write back to JSON
```

**ポイント**: 複雑なコードを、まるで忍耐強いメンターのようにわかりやすく解説してくれます。

---

### デモ3: 動作するコードの生成

いつもなら15分かけてGoogle検索する関数が必要？セッション内でそのまま：

```
> Write a Python function that takes a list of books and returns statistics: 
  total count, number read, number unread, oldest and newest book
```

---

<details>
<summary>🎬 実際の動作を見る！</summary>

![Generate Code Demo](images/generate-code-demo.gif)

*デモの出力は異なります。お使いのモデル、ツール、応答はここに示されているものと異なります。*

</details>

---

**何が起こるか**: 数秒で完全に動作する関数が生成され、コピー＆ペーストですぐに実行できます。

探索が終わったら、セッションを終了しましょう：

```
> /exit
```

**ポイント**: 即座に結果が得られ、しかも一つの連続したセッション内で全て完了しました。

---

# モードとコマンド

<img src="images/modes-and-commands.png" alt="Futuristic control panel with glowing screens, dials, and equalizers representing Copilot CLI modes and commands" width="800"/>

Copilot CLIで何ができるかを見てきました。次は、これらの機能を*効果的に使う方法*を理解しましょう。ポイントは、状況に応じて3つのインタラクションモードのどれを使うかを知ることです。

> 💡 **補足**: Copilot CLIには、あなたの入力を待たずにタスクを進める **Autopilot** モードもあります。強力ですが、フルパーミッションの付与が必要で、プレミアムリクエストを自律的に使用します。このコースでは以下の3つのモードに焦点を当てます。基本に慣れたらAutopilotについてご案内します。

---

## 🧩 実世界のアナロジー: 外食

GitHub Copilot CLIの使い方は、外食に例えて考えるとわかりやすいです。旅の計画から注文まで、状況に応じて異なるアプローチが求められます：

| モード | 外食のアナロジー | 使うタイミング |
|------|----------------|-------------|
| **Plan** | レストランまでのGPSルート | 複雑なタスク - ルートを確認し、途中の立ち寄りを検討し、計画に合意してから出発 |
| **Interactive** | ウェイターとの会話 | 探索と反復 - 質問し、カスタマイズし、リアルタイムのフィードバックを得る |
| **Programmatic** | ドライブスルーでの注文 | 素早く具体的なタスク - 自分の環境にいたまま、すぐに結果を得る |

外食と同じように、どのアプローチが適切かは自然にわかるようになります。

<img src="images/ordering-food-analogy.png" alt="Three Ways to Use GitHub Copilot CLI - Plan Mode (GPS route to restaurant), Interactive Mode (talking to waiter), Programmatic Mode (drive-through)" width="800"/>

*タスクに応じてモードを選択: Planは事前の計画に、Interactiveは対話的なコラボレーションに、Programmaticは素早いワンショットの結果に*

### どのモードから始めるべき？

**Interactiveモードから始めましょう。**
- 試行錯誤やフォローアップの質問ができます
- 会話を通じて自然にコンテキストが蓄積されます
- 間違えても `/clear` で簡単にやり直せます

慣れてきたら、以下も試してみましょう：
- **Programmaticモード** (`copilot -p "<プロンプト>"`) - 素早いワンオフの質問に
- **Planモード** (`/plan`) - コーディング前により詳細な計画が必要なとき

---

## 3つのモード

### モード1: Interactiveモード（ここから始めよう）

<img src="images/interactive-mode.png" alt="Interactive Mode - Like talking to a waiter who can answer questions and adjust the order" width="250"/>

**最適な用途**: 探索、反復、複数ターンの会話。質問に答え、フィードバックを受け取り、その場で注文を調整してくれるウェイターとの会話のようなものです。

インタラクティブセッションを開始：

```bash
copilot
```

ここまで見てきたように、自然に入力できるプロンプトが表示されます。利用可能なコマンドのヘルプを表示するには：

```
> /help
```

**重要なポイント**: Interactiveモードはコンテキストを維持します。各メッセージは前のメッセージの上に積み重なり、まさに実際の会話のようです。

#### Interactiveモードの例

```bash
copilot

> Review @samples/book-app-project/utils.py and suggest improvements

> Add type hints to all functions

> Make the error handling more robust

> /exit
```

各プロンプトが前の回答の上に積み重なっていることに注目してください。毎回やり直すのではなく、会話を続けているのです。

---

### モード2: Planモード

<img src="images/plan-mode.png" alt="Plan Mode - Like planning a route before a trip using GPS" width="250"/>

**最適な用途**: 実行前にアプローチを確認したい複雑なタスク。GPSで旅行前にルートを計画するのに似ています。

Planモードは、コードを書く前にステップバイステップの計画を作成するのに役立ちます。`/plan` コマンドを使うか、**Shift+Tab** を押してPlanモードに切り替えます：

> 💡 **ヒント**: **Shift+Tab** でモードを切り替えられます: Interactive → Plan → Autopilot。インタラクティブセッション中にいつでも押してコマンドを入力せずにモードを切り替えられます。

```bash
copilot

> /plan Add a "mark as read" command to the book app
```

**Planモードの出力:** （出力は異なる場合があります）

```
📋 Implementation Plan

Step 1: Update the command handler in book_app.py
  - Add new elif branch for "mark" command
  - Create handle_mark_as_read() function

Step 2: Implement the handler function
  - Prompt user for book title
  - Call collection.mark_as_read(title)
  - Display success/failure message

Step 3: Update help text
  - Add "mark" to available commands list
  - Document the command usage

Step 4: Test the flow
  - Add a book
  - Mark it as read
  - Verify status changes in list output

Proceed with implementation? [Y/n]
```

**重要なポイント**: Planモードでは、コードが書かれる前にアプローチを確認・修正できます。計画が完成したら、Copilot CLIにファイルとして保存するよう指示することもできます。例えば、「この計画を `mark_as_read_plan.md` に保存して」と言えば、計画の詳細を含むMarkdownファイルが作成されます。

> 💡 **もっと複雑なものを試したい？** `/plan Add search and filter capabilities to the book app` を試してみてください。Planモードはシンプルな機能からフルアプリケーションまで対応できます。

> 📚 **Autopilotモード**: Shift+Tabで **Autopilot** という3番目のモードに切り替わることに気づいたかもしれません。Autopilotモードでは、Copilotが各ステップの後であなたの入力を待たずに計画全体を進めます。同僚にタスクを渡して「終わったら教えて」と言うようなものです。典型的なワークフローは「計画 → 承認 → Autopilot」です。つまり、まず良い計画を書けるようになることが重要です。InteractiveモードとPlanモードに慣れてから、準備ができたら[公式ドキュメント](https://docs.github.com/copilot/concepts/agents/copilot-cli/autopilot)を参照してください。

---

### モード3: Programmaticモード

<img src="images/programmatic-mode.png" alt="Programmatic Mode - Like using a drive-through for a quick order" width="250"/>

**最適な用途**: 自動化、スクリプト、CI/CD、シングルショットコマンド。ウェイターと話す必要なく素早く注文できるドライブスルーのようなものです。

対話不要のワンタイムコマンドには `-p` フラグを使用します：

```bash
# コード生成
copilot -p "Write a function that checks if a number is even or odd"

# 素早いヘルプ
copilot -p "How do I read a JSON file in Python?"
```

**重要なポイント**: Programmaticモードは素早い回答を返して終了します。会話なし、入力 → 出力のみです。

<details>
<summary>📚 <strong>さらに詳しく: スクリプトでのProgrammaticモードの活用</strong>（クリックで展開）</summary>

慣れてきたら、`-p` をシェルスクリプト内で使うことができます：

```bash
#!/bin/bash

# コミットメッセージを自動生成
COMMIT_MSG=$(copilot -p "Generate a commit message for: $(git diff --staged)")
git commit -m "$COMMIT_MSG"

# ファイルをレビュー
copilot --allow-all -p "Review @myfile.py for issues"
```
> ⚠️ **`--allow-all` について**: このフラグはすべてのパーミッションプロンプトをスキップし、Copilot CLIが確認なしにファイルの読み取り、コマンドの実行、URLへのアクセスを行えるようにします。Programmaticモード（`-p`）ではアクションを承認するインタラクティブセッションがないため、これが必要です。`--allow-all` は自分で書いたプロンプトと信頼できるディレクトリでのみ使用してください。信頼できない入力や機密性の高いディレクトリでは使用しないでください。

</details>

---

## 必須スラッシュコマンド

これらのコマンドはInteractiveモードで使用できます。**まずはこの6つだけ覚えましょう** - 日常使用の90%をカバーします：

| コマンド | 機能 | 使うタイミング |
|---------|------|-------------|
| `/help` | 利用可能なすべてのコマンドを表示 | コマンドを忘れたとき |
| `/clear` | 会話をクリアして最初からやり直す | トピックを切り替えるとき |
| `/plan` | コーディング前に作業を計画する | より複雑な機能を実装するとき |
| `/research` | GitHubやウェブソースを使った詳細な調査 | コーディング前にトピックを調査する必要があるとき |
| `/model` | AIモデルを表示または切り替える | AIモデルを変更したいとき |
| `/exit` | セッションを終了する | 作業が終わったとき |

入門としてはこれで十分です！慣れてきたら、追加のコマンドを探索できます。

> 📚 **公式ドキュメント**: コマンドとフラグの完全なリストは [CLIコマンドリファレンス](https://docs.github.com/copilot/reference/cli-command-reference) を参照してください。

<details>
<summary>📚 <strong>追加コマンド</strong>（クリックで展開）</summary>

> 💡 上記の必須コマンドで日常的な使用の多くをカバーできます。このリファレンスは、さらに探索する準備ができたときのためのものです。

### エージェント環境

| コマンド | 機能 |
|---------|------|
| `/init` | リポジトリ用のCopilot設定を初期化 |
| `/agent` | 利用可能なエージェントを閲覧・選択 |
| `/skills` | 拡張機能のためのスキルを管理 |
| `/mcp` | MCPサーバー設定を管理 |

> 💡 スキルについては[第05章](../05-skills/README.ja.md)で詳しく解説します。MCPサーバーについては[第06章](../06-mcp-servers/README.ja.md)で解説します。

### モデルとサブエージェント

| コマンド | 機能 |
|---------|------|
| `/model` | AIモデルを表示または切り替える |
| `/delegate` | GitHub上のCopilotコーディングエージェント（クラウド上のエージェント）にタスクを委譲 |
| `/fleet` | 複雑なタスクを並列サブタスクに分割して高速化 |
| `/tasks` | バックグラウンドのサブエージェントとデタッチされたシェルセッションを表示 |

### コード

| コマンド | 機能 |
|---------|------|
| `/diff` | 現在のディレクトリで行われた変更をレビュー |
| `/pr` | 現在のブランチのプルリクエストを操作 |
| `/review` | コードレビューエージェントを実行して変更を分析 |
| `/research` | GitHubやウェブソースを使った詳細な調査を実行 |
| `/terminal-setup` | マルチライン入力サポートを有効化（shift+enter と ctrl+enter） |

### パーミッション

| コマンド | 機能 |
|---------|------|
| `/allow-all` | このセッションのすべてのパーミッションプロンプトを自動承認 |
| `/add-dir <directory>` | 許可リストにディレクトリを追加 |
| `/list-dirs` | 許可されたすべてのディレクトリを表示 |
| `/cwd`, `/cd [directory]` | 作業ディレクトリを表示または変更 |

> ⚠️ **注意して使用**: `/allow-all` は確認プロンプトをスキップします。信頼できるプロジェクトには便利ですが、信頼できないコードには注意してください。

### セッション

| コマンド | 機能 |
|---------|------|
| `/resume` | 別のセッションに切り替え（オプションでセッションIDを指定） |
| `/rename` | 現在のセッションの名前を変更 |
| `/context` | コンテキストウィンドウのトークン使用量と視覚化を表示 |
| `/usage` | セッションの使用メトリクスと統計を表示 |
| `/session` | セッション情報とワークスペースの概要を表示 |
| `/compact` | コンテキスト使用量を減らすために会話を要約 |
| `/share` | セッションをMarkdownファイルまたはGitHub Gistとしてエクスポート |

### ヘルプとフィードバック

| コマンド | 機能 |
|---------|------|
| `/help` | 利用可能なすべてのコマンドを表示 |
| `/changelog` | CLIバージョンの変更履歴を表示 |
| `/feedback` | GitHubにフィードバックを送信 |
| `/theme` | ターミナルテーマを表示または設定 |

### クイックシェルコマンド

`!` をプレフィックスに付けることで、AIを経由せずにシェルコマンドを直接実行できます：

```bash
copilot

> !git status
# AIをバイパスして直接 git status を実行

> !python -m pytest tests/
# 直接 pytest を実行
```

### モデルの切り替え

Copilot CLIはOpenAI、Anthropic、Googleなどの複数のAIモデルをサポートしています。利用可能なモデルはサブスクリプションレベルと地域によって異なります。`/model` を使ってオプションを確認し、切り替えましょう：

```bash
copilot
> /model

# 利用可能なモデルが表示され、選択できます。Sonnet 4.5を選択してみましょう。
```

> 💡 **ヒント**: モデルによって消費する「プレミアムリクエスト」の数が異なります。**1x** とマークされたモデル（Claude Sonnet 4.5など）は、優れたデフォルトの選択肢です。高性能で効率的です。倍率の高いモデルはプレミアムリクエストの割り当てをより早く消費するので、本当に必要なときのために取っておきましょう。

</details>

---

# 実践

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

学んだことを実践に移しましょう。

---

## ▶️ 自分で試してみよう

### インタラクティブな探索

Copilotを起動し、フォローアッププロンプトを使ってBook Appを段階的に改善してみましょう：

```bash
copilot

> Review @samples/book-app-project/book_app.py - what could be improved?

> Refactor the if/elif chain into a more maintainable structure

> Add type hints to all the handler functions

> /exit
```

### 機能を計画する

`/plan` を使って、コードを書く前にCopilot CLIに実装計画を立てさせましょう：

```bash
copilot

> /plan Add a search feature to the book app that can find books by title or author

# 計画をレビュー
# 承認または修正
# ステップバイステップで実装される様子を見る
```

### Programmaticモードで自動化

`-p` フラグを使うと、Interactiveモードに入らずにターミナルから直接Copilot CLIを実行できます。以下のスクリプトをリポジトリのルートからターミナルにコピー＆ペーストして（Copilot内ではなく）、Book Appのすべてのpythonファイルをレビューしてみましょう。

```bash
# Book Appのすべてのpythonファイルをレビュー
for file in samples/book-app-project/*.py; do
  echo "Reviewing $file..."
  copilot --allow-all -p "Quick code quality review of @$file - critical issues only"
done
```

**PowerShell (Windows):**

```powershell
# Review all Python files in the book app
Get-ChildItem samples/book-app-project/*.py | ForEach-Object {
  $relativePath = "samples/book-app-project/$($_.Name)";
  Write-Host "Reviewing $relativePath...";
  copilot --allow-all -p "Quick code quality review of @$relativePath - critical issues only" 
}
```

---

デモを完了したら、以下のバリエーションを試してみましょう：

1. **Interactiveチャレンジ**: `copilot` を起動してBook Appを探索します。`@samples/book-app-project/books.py` について質問し、3回連続で改善を依頼してみましょう。

2. **Planモードチャレンジ**: `/plan Add rating and review features to the book app` を実行します。計画をよく読んでください。内容は理にかなっていますか？

3. **Programmaticチャレンジ**: `copilot --allow-all -p "List all functions in @samples/book-app-project/book_app.py and describe what each does"` を実行します。一発でうまくいきましたか？

---

## 📝 課題

### メインチャレンジ: Book Appのユーティリティを改善する

ハンズオンの例では `book_app.py` のレビューとリファクタリングに焦点を当てました。次は同じスキルを別のファイル `utils.py` で練習しましょう：

1. インタラクティブセッションを開始: `copilot`
2. Copilot CLIにファイルを要約させる: `@samples/book-app-project/utils.py What does each function in this file do?`
3. 入力バリデーションの追加を依頼: 「`get_user_choice()` に空の入力や非数値のエントリを処理するバリデーションを追加して」
4. エラーハンドリングの改善を依頼: 「`get_book_details()` がタイトルに空文字列を受け取った場合どうなりますか？ガード処理を追加して」
5. docstringを依頼: 「`get_book_details()` にパラメータの説明と戻り値を含む包括的なdocstringを追加して」
6. プロンプト間でコンテキストがどのように引き継がれるかを観察しましょう。各改善は前の改善の上に積み重なります
7. `/exit` で終了

**成功基準**: 入力バリデーション、エラーハンドリング、docstringが追加された改善版 `utils.py` が、マルチターンの会話を通じて完成していること。

<details>
<summary>💡 ヒント（クリックで展開）</summary>

**試してみるプロンプト例:**
```bash
> @samples/book-app-project/utils.py What does each function in this file do?
> Add validation to get_user_choice() so it handles empty input and non-numeric entries
> What happens if get_book_details() receives an empty string for the title? Add guards for that.
> Add a comprehensive docstring to get_book_details() with parameter descriptions and return values
```

**よくある問題:**
- Copilot CLIが確認の質問をしてきたら、自然に答えてください
- コンテキストは引き継がれるので、各プロンプトは前のプロンプトの上に積み重なります
- やり直したい場合は `/clear` を使ってください

</details>

### ボーナスチャレンジ: モードを比較する

例では `/plan` で検索機能を、`-p` でバッチレビューを行いました。今度は3つのモードすべてを1つの新しいタスクで試してみましょう: `BookCollection` クラスに `list_by_year()` メソッドを追加します：

1. **Interactive**: `copilot` → ステップバイステップでメソッドの設計と構築を依頼
2. **Plan**: `/plan Add a list_by_year(start, end) method to BookCollection that filters books by publication year range`
3. **Programmatic**: `copilot --allow-all -p "@samples/book-app-project/books.py Add a list_by_year(start, end) method that returns books published between start and end year inclusive"`

**振り返り**: どのモードが最も自然に感じましたか？それぞれをどんなときに使いますか？

---

<details>
<summary>🔧 <strong>よくある間違いとトラブルシューティング</strong>（クリックで展開）</summary>

### よくある間違い

| 間違い | 何が起こるか | 対処法 |
|---------|------------|------|
| `/exit` の代わりに `exit` と入力 | Copilot CLIは「exit」をコマンドではなくプロンプトとして扱う | スラッシュコマンドは常に `/` で始まる |
| マルチターンの会話に `-p` を使用 | 各 `-p` 呼び出しは前の呼び出しの記憶がなく独立している | コンテキストを積み重ねる会話にはInteractiveモード（`copilot`）を使用 |
| `$` や `!` を含むプロンプトでクォートを忘れる | Copilot CLIに渡される前にシェルが特殊文字を解釈してしまう | プロンプトをクォートで囲む: `copilot -p "What does $HOME mean?"` |

### トラブルシューティング

**「Model not available」** - お使いのサブスクリプションにすべてのモデルが含まれていない可能性があります。`/model` で利用可能なモデルを確認してください。

**「Context too long」** - 会話がコンテキストウィンドウ全体を使い切りました。`/clear` でリセットするか、新しいセッションを開始してください。

**「Rate limit exceeded」** - 数分待ってから再試行してください。バッチ操作にはディレイ付きのProgrammaticモードの使用を検討してください。

</details>

---

# まとめ

## 🔑 重要なポイント

1. **Interactiveモード** は探索と反復のためのもの - コンテキストが引き継がれます。それまでに話したことを覚えている相手との会話のようなものです。
2. **Planモード** は通常、より複雑なタスクのためのもの。実装前にレビューできます。
3. **Programmaticモード** は自動化のためのもの。対話は不要です。
4. **4つの必須コマンド** (`/help`、`/clear`、`/plan`、`/exit`) で日常使用の大部分をカバーします。

> 📋 **クイックリファレンス**: コマンドとショートカットの完全なリストは [GitHub Copilot CLI コマンドリファレンス](https://docs.github.com/en/copilot/reference/cli-command-reference) を参照してください。

---

## ➡️ 次のステップ

3つのモードを理解したところで、次はCopilot CLIにコードのコンテキストを伝える方法を学びましょう。

**[第02章: コンテキストと会話](../02-context-conversations/README.ja.md)** では、以下を学びます：

- ファイルやディレクトリを参照する `@` 構文
- `--resume` と `--continue` によるセッション管理
- コンテキスト管理がCopilot CLIを真に強力にする仕組み

---

**[← コースホームに戻る](../README.ja.md)** | **[第02章へ進む →](../02-context-conversations/README.ja.md)**
