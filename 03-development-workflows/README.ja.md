![Chapter 03: Development Workflows](images/chapter-header.png)

> **AIが、あなたが気づいてもいなかったバグを見つけてくれるとしたら？**

この章では、GitHub Copilot CLIを日常的に使いこなします。テスト、リファクタリング、デバッグ、Gitなど、毎日頼りにしているワークフローの中で活用していきます。

## 🎯 学習目標

この章を終えると、以下のことができるようになります：

- Copilot CLIで包括的なコードレビューを実行する
- レガシーコードを安全にリファクタリングする
- AIの支援を使って問題をデバッグする
- テストを自動生成する
- Copilot CLIをGitワークフローに統合する

> ⏱️ **想定所要時間**: 約60分（読書15分＋ハンズオン45分）

---

## 🧩 現実世界のアナロジー：大工のワークフロー

大工は道具の使い方を知っているだけでなく、仕事ごとの*ワークフロー*を持っています：

<img src="images/carpenter-workflow-steps.png" alt="Craftsman workshop showing three workflow lanes: Building Furniture (Measure, Cut, Assemble, Finish), Fixing Damage (Assess, Remove, Repair, Match), and Quality Check (Inspect, Test Joints, Check Alignment)" width="800"/>

同様に、開発者もタスクごとにワークフローを持っています。GitHub Copilot CLIはこれらのワークフローそれぞれを強化し、日々のコーディング作業をより効率的かつ効果的にします。

---

# 5つのワークフロー

<img src="images/five-workflows.png" alt="Five glowing neon icons representing code review, testing, debugging, refactoring, and git integration workflows" width="800"/>

以下の各ワークフローは独立しています。現在のニーズに合ったものを選ぶか、すべてを順に進めてください。

---

## 自分に合ったワークフローを選ぼう

この章では、開発者が一般的に使う5つのワークフローを取り上げます。**ただし、一度にすべてを読む必要はありません！** 各ワークフローは下の折りたたみセクションに独立してまとまっています。自分に必要なもの、現在のプロジェクトに最適なものを選んでください。残りは後からいつでも探索できます。

<img src="images/five-workflows-swimlane.png" alt="Five Development Workflows: Code Review, Refactoring, Debugging, Test Generation, and Git Integration shown as horizontal swimlanes" width="800"/>

| やりたいこと | ジャンプ先 |
|---|---|
| マージ前にコードをレビューしたい | [ワークフロー1：コードレビュー](#workflow-1-code-review) |
| 散らかったコードやレガシーコードを整理したい | [ワークフロー2：リファクタリング](#workflow-2-refactoring) |
| バグを追跡して修正したい | [ワークフロー3：デバッグ](#workflow-3-debugging) |
| コードのテストを生成したい | [ワークフロー4：テスト生成](#workflow-4-test-generation) |
| より良いコミットやPRを書きたい | [ワークフロー5：Git連携](#workflow-5-git-integration) |
| コーディング前にリサーチしたい | [クイックヒント：計画やコーディングの前にリサーチ](#quick-tip-research-before-you-plan-or-code) |
| バグ修正のワークフロー全体を見たい | [すべてをまとめる](#putting-it-all-together-bug-fix-workflow) |

**下のワークフローを選んで展開し**、GitHub Copilot CLIがその分野の開発プロセスをどのように強化できるか確認しましょう。

---

<a id="workflow-1-code-review"></a>
<details>
<summary><strong>ワークフロー1：コードレビュー</strong> - ファイルのレビュー、/reviewエージェントの使用、重要度チェックリストの作成</summary>

<img src="images/code-review-swimlane-single.png" alt="Code review workflow: review, identify issues, prioritize, generate checklist." width="800"/>

### 基本的なレビュー

この例では`@`記号を使ってファイルを参照し、Copilot CLIがそのコンテンツに直接アクセスしてレビューできるようにしています。

```bash
copilot

> Review @samples/book-app-project/book_app.py for code quality
```

---

<details>
<summary>🎬 実際の動作を見てみよう！</summary>

![Code Review Demo](images/code-review-demo.gif)

*デモの出力は異なります。お使いのモデル、ツール、レスポンスはここに表示されているものとは異なります。*

</details>

---

### 入力バリデーションのレビュー

Copilot CLIに特定の懸念事項（ここでは入力バリデーション）に焦点を当てたレビューを依頼するには、プロンプトで気になるカテゴリーを列挙します。

```text
copilot

> Review @samples/book-app-project/utils.py for input validation issues. Check for: missing validation, error handling gaps, and edge cases
```


### クロスファイルプロジェクトレビュー

`@`でディレクトリ全体を参照すると、Copilot CLIがプロジェクト内のすべてのファイルを一度にスキャンできます。

```bash
copilot

> @samples/book-app-project/ Review this entire project. Create a markdown checklist of issues found, categorized by severity
```

### インタラクティブなコードレビュー

マルチターン会話を使ってより深く掘り下げます。広範なレビューから始めて、再起動せずにフォローアップの質問をしていきます。

```bash
copilot

> @samples/book-app-project/book_app.py Review this file for:
> - Input validation
> - Error handling
> - Code style and best practices

# Copilot CLIが詳細なレビューを提供

> The user input handling - are there any edge cases I'm missing?

# Copilot CLIが空文字列や特殊文字に関する潜在的な問題を表示

> Create a checklist of all issues found, prioritized by severity

# Copilot CLIが優先度付きのアクションアイテムを生成
```

### レビューチェックリストテンプレート

Copilot CLIに特定のフォーマット（ここでは、Issueに貼り付けられる重要度別のMarkdownチェックリスト）で出力を構造化するよう依頼します。

```bash
copilot

> Review @samples/book-app-project/ and create a markdown checklist of issues found, categorized by:
> - Critical (data loss risks, crashes)
> - High (bugs, incorrect behavior)
> - Medium (performance, maintainability)
> - Low (style, minor improvements)
```

### Gitの変更を理解する（/reviewに重要）

`/review`コマンドを使用する前に、Gitにおける2種類の変更を理解する必要があります：

| 変更の種類 | 意味 | 確認方法 |
|-------------|---------------|------------|
| **ステージされた変更** | `git add`で次のコミット対象としてマークしたファイル | `git diff --staged` |
| **ステージされていない変更** | 変更したがまだ追加していないファイル | `git diff` |

```bash
# クイックリファレンス
git status           # ステージ済みとステージされていない変更の両方を表示
git add file.py      # ファイルをコミット用にステージ
git diff             # ステージされていない変更を表示
git diff --staged    # ステージされた変更を表示
```

### /reviewコマンドの使用

`/review`コマンドは組み込みの**code-reviewエージェント**を呼び出します。このエージェントは、ステージされた変更とステージされていない変更を高いシグナル対ノイズ比の出力で分析するために最適化されています。フリーフォームのプロンプトを書く代わりに、スラッシュコマンドを使って専用の組み込みエージェントを起動します。

```bash
copilot

> /review
# ステージ済み/ステージされていない変更に対してcode-reviewエージェントを呼び出す
# 焦点を絞った実用的なフィードバックを提供

> /review Check for security issues in authentication
# 特定の焦点を当てたレビューを実行
```

> 💡 **ヒント**: code-reviewエージェントは保留中の変更がある場合に最も効果を発揮します。より焦点を絞ったレビューのために、`git add`でファイルをステージしましょう。

</details>

---

<a id="workflow-2-refactoring"></a>
<details>
<summary><strong>ワークフロー2：リファクタリング</strong> - コードの再構成、関心の分離、エラーハンドリングの改善</summary>

<img src="images/refactoring-swimlane-single.png" alt="Refactoring workflow: assess code, plan changes, implement, verify behavior." width="800"/>

### シンプルなリファクタリング

> **まずこれを試してみよう：** `@samples/book-app-project/book_app.py The command handling uses if/elif chains. Refactor it to use a dictionary dispatch pattern.`

わかりやすい改善から始めましょう。ブックアプリでこれらを試してみてください。各プロンプトは`@`ファイル参照と具体的なリファクタリング指示を組み合わせて、Copilot CLIが何を変更すべきかを正確に把握できるようにしています。

```bash
copilot

> @samples/book-app-project/book_app.py The command handling uses if/elif chains. Refactor it to use a dictionary dispatch pattern.

> @samples/book-app-project/utils.py Add type hints to all functions

> @samples/book-app-project/book_app.py Extract the book display logic into utils.py for better separation of concerns
```

> 💡 **リファクタリングが初めて？** 複雑な変換に取り組む前に、型ヒントの追加や変数名の改善などのシンプルなリクエストから始めましょう。

---

<details>
<summary>🎬 実際の動作を見てみよう！</summary>

![Refactor Demo](images/refactor-demo.gif)

*デモの出力は異なります。お使いのモデル、ツール、レスポンスはここに表示されているものとは異なります。*

</details>

---

### 関心の分離

1つのプロンプトで`@`を使って複数のファイルを参照し、Copilot CLIがリファクタリングの一環としてファイル間でコードを移動できるようにします。

```bash
copilot

> @samples/book-app-project/utils.py @samples/book-app-project/book_app.py
> The utils.py file has print statements mixed with logic. Refactor to separate display functions from data processing.
```

### エラーハンドリングの改善

関連する2つのファイルを提供し、横断的な懸念を説明することで、Copilot CLIが両方のファイルにわたって一貫した修正を提案できるようにします。

```bash
copilot

> @samples/book-app-project/utils.py @samples/book-app-project/books.py
> These files have inconsistent error handling. Suggest a unified approach using custom exceptions.
```

### ドキュメントの追加

各docstringに何を含めるべきかを正確に指定するために、詳細な箇条書きリストを使用します。

```bash
copilot

> @samples/book-app-project/books.py Add comprehensive docstrings to all methods:
> - Include parameter types and descriptions
> - Document return values
> - Note any exceptions raised
> - Add usage examples
```

### テスト付きの安全なリファクタリング

マルチターン会話で関連する2つのリクエストを連鎖させます。まずテストを生成し、そのテストをセーフティネットとしてリファクタリングを行います。

```bash
copilot

> @samples/book-app-project/books.py Before refactoring, generate tests for current behavior

# まずテストを取得

> Now refactor the BookCollection class to use a context manager for file operations

# 自信を持ってリファクタリング - テストが動作の保持を検証
```

</details>

---

<a id="workflow-3-debugging"></a>
<details>
<summary><strong>ワークフロー3：デバッグ</strong> - バグの追跡、セキュリティ監査、ファイル間の問題追跡</summary>

<img src="images/debugging-swimlane-single.png" alt="Debugging workflow: understand error, locate root cause, fix, test." width="800"/>

### シンプルなデバッグ

> **まずこれを試してみよう：** `@samples/book-app-buggy/books_buggy.py Users report that searching for "The Hobbit" returns no results even though it's in the data. Debug why.`

何が問題なのかを説明することから始めます。バグのあるブックアプリで試せる一般的なデバッグパターンを紹介します。各プロンプトは`@`ファイル参照と明確な症状の説明を組み合わせて、Copilot CLIがバグを特定・診断できるようにしています。

```bash
copilot

# パターン：「Xを期待したがYが返った」
> @samples/book-app-buggy/books_buggy.py Users report that searching for "The Hobbit" returns no results even though it's in the data. Debug why.

# パターン：「予期しない動作」
> @samples/book-app-buggy/book_app_buggy.py When I remove a book that doesn't exist, the app says it was removed. Help me find why.

# パターン：「間違った結果」
> @samples/book-app-buggy/books_buggy.py When I mark one book as read, ALL books get marked. What's the bug?
```

> 💡 **デバッグのコツ**: *症状*（見えていること）と*期待*（あるべき動作）を説明しましょう。残りはCopilot CLIが解決してくれます。

---

<details>
<summary>🎬 実際の動作を見てみよう！</summary>

![Fix Bug Demo](images/fix-bug-demo.gif)

*デモの出力は異なります。お使いのモデル、ツール、レスポンスはここに表示されているものとは異なります。*

</details>

---

### 「バグ探偵」 - AIが関連バグを見つける

ここがコンテキストを意識したデバッグの真価が発揮される場面です。バグのあるブックアプリでこのシナリオを試してみましょう。`@`でファイル全体を提供し、ユーザーが報告した症状だけを説明します。Copilot CLIが根本原因を追跡し、近くにある追加のバグも発見する場合があります。

```bash
copilot

> @samples/book-app-buggy/books_buggy.py
>
> Users report: "Finding books by author name doesn't work for partial names"
> Debug why this happens
```

**Copilot CLIの動作**:
```
Root Cause: Line 80 uses exact match (==) instead of partial match (in).

Line 80: return [b for b in self.books if b.author == author]

The find_by_author function requires an exact match. Searching for "Tolkien"
won't find books by "J.R.R. Tolkien".

Fix: Change to case-insensitive partial match:
return [b for b in self.books if author.lower() in b.author.lower()]
```

**これが重要な理由**: Copilot CLIはファイル全体を読み、バグレポートのコンテキストを理解し、明確な説明付きの具体的な修正を提供します。

> 💡 **ボーナス**: Copilot CLIはファイル全体を分析するため、あなたが聞いていない*他の*問題も発見することがよくあります。たとえば、著者検索を修正している際に、`find_book_by_title`の大文字小文字の区別のバグにも気づくかもしれません！

### 実世界のセキュリティサイドバー

自分のコードのデバッグは重要ですが、本番アプリケーションのセキュリティ脆弱性を理解することも極めて重要です。この例を試してみてください：Copilot CLIに見慣れないファイルを指定して、セキュリティの問題を監査するよう依頼します。

```bash
copilot

> @samples/buggy-code/python/user_service.py Find all security vulnerabilities in this Python user service
```

このファイルは、本番アプリで遭遇する実世界のセキュリティパターンを示しています。

> 💡 **よく出てくるセキュリティ用語：**
> - **SQLインジェクション**: ユーザー入力がデータベースクエリに直接挿入されることで、攻撃者が悪意のあるコマンドを実行できてしまう脆弱性
> - **パラメータ化クエリ**: 安全な代替手段 - プレースホルダー（`?`）がユーザーデータをSQLコマンドから分離する
> - **レースコンディション**: 2つの操作が同時に発生し、互いに干渉すること
> - **XSS（クロスサイトスクリプティング）**: 攻撃者がWebページに悪意のあるスクリプトを注入すること

---

### エラーを理解する

スタックトレースを`@`ファイル参照と一緒にプロンプトに直接貼り付けることで、Copilot CLIがエラーをソースコードにマッピングできるようにします。

```bash
copilot

> I'm getting this error:
> AttributeError: 'NoneType' object has no attribute 'title'
>     at show_books (book_app.py:19)
>
> @samples/book-app-project/book_app.py Explain why and how to fix it
```

### テストケースを使ったデバッグ

正確な入力と観察された出力を説明することで、Copilot CLIに推論するための具体的で再現可能なテストケースを提供します。

```bash
copilot

> @samples/book-app-buggy/books_buggy.py The remove_book function has a bug. When I try to remove "Dune",
> it also removes "Dune Messiah". Debug this: explain the root cause and provide a fix.
```

### コード全体にわたる問題の追跡

複数のファイルを参照し、Copilot CLIにファイル間のデータフローを追跡して問題の発生箇所を特定するよう依頼します。

```bash
copilot

> Users report that the book list numbering starts at 0 instead of 1.
> @samples/book-app-buggy/book_app_buggy.py @samples/book-app-buggy/books_buggy.py
> Trace through the list display flow and identify where the issue occurs
```

### データの問題を理解する

データファイルとそれを読み込むコードを一緒に含めることで、Copilot CLIがエラーハンドリングの改善を提案する際に全体像を把握できるようにします。

```bash
copilot

> @samples/book-app-project/data.json @samples/book-app-project/books.py
> Sometimes the JSON file gets corrupted and the app crashes. How should we handle this gracefully?
```

</details>

---

<a id="workflow-4-test-generation"></a>
<details>
<summary><strong>ワークフロー4：テスト生成</strong> - 包括的なテストとエッジケースを自動生成</summary>

<img src="images/test-gen-swimlane-single.png" alt="Test Generation workflow: analyze function, generate tests, include edge cases, run." width="800"/>

> **まずこれを試してみよう：** `@samples/book-app-project/books.py Generate pytest tests for all functions including edge cases`

### 「テストの爆発」 - 2つのテスト vs 15以上のテスト

手動でテストを書く場合、開発者は通常2〜3個の基本テストを作成します：
- 正常な入力のテスト
- 異常な入力のテスト
- エッジケースのテスト

Copilot CLIに包括的なテストを生成するよう依頼すると何が起こるか見てみましょう！このプロンプトは`@`ファイル参照と構造化された箇条書きリストを使って、Copilot CLIを徹底的なテストカバレッジに導きます：

```bash
copilot

> @samples/book-app-project/books.py Generate comprehensive pytest tests. Include tests for:
> - Adding books
> - Removing books
> - Finding by title
> - Finding by author
> - Marking as read
> - Edge cases with empty data
```

---

<details>
<summary>🎬 実際の動作を見てみよう！</summary>

![Test Generation Demo](images/test-gen-demo.gif)

*デモの出力は異なります。お使いのモデル、ツール、レスポンスはここに表示されているものとは異なります。*

</details>

---

**得られるもの**: 以下を含む15以上の包括的なテスト：

```python
class TestBookCollection:
    # 正常系
    def test_add_book_creates_new_book(self):
        ...
    def test_list_books_returns_all_books(self):
        ...

    # 検索操作
    def test_find_book_by_title_case_insensitive(self):
        ...
    def test_find_book_by_title_returns_none_when_not_found(self):
        ...
    def test_find_by_author_partial_match(self):
        ...
    def test_find_by_author_case_insensitive(self):
        ...

    # エッジケース
    def test_add_book_with_empty_title(self):
        ...
    def test_remove_nonexistent_book(self):
        ...
    def test_mark_as_read_nonexistent_book(self):
        ...

    # データの永続化
    def test_save_books_persists_to_json(self):
        ...
    def test_load_books_handles_missing_file(self):
        ...
    def test_load_books_handles_corrupted_json(self):
        ...

    # 特殊文字
    def test_add_book_with_unicode_characters(self):
        ...
    def test_find_by_author_with_special_characters(self):
        ...
```

**結果**: 30秒で、考え抜いて書くのに1時間かかるようなエッジケーステストが手に入ります。

---

### ユニットテスト

単一の関数をターゲットにし、テストしたい入力カテゴリを列挙することで、Copilot CLIが焦点を絞った徹底的なユニットテストを生成します。

```bash
copilot

> @samples/book-app-project/utils.py Generate comprehensive pytest tests for get_book_details covering:
> - Valid input
> - Empty strings
> - Invalid year formats
> - Very long titles
> - Special characters in author names
```

### テストの実行

ツールチェーンについて平易な英語でCopilot CLIに質問しましょう。適切なシェルコマンドを生成してくれます。

```bash
copilot

> How do I run the tests? Show me the pytest command.

# Copilot CLIの応答：
# cd samples/book-app-project && python -m pytest tests/
# 詳細出力の場合: python -m pytest tests/ -v
# print文を表示する場合: python -m pytest tests/ -s
```

### 特定のシナリオ向けテスト

カバーしたい高度なシナリオやトリッキーなシナリオをリストアップし、Copilot CLIが正常系を超えたテストを生成するようにします。

```bash
copilot

> @samples/book-app-project/books.py Generate tests for these scenarios:
> - Adding duplicate books (same title and author)
> - Removing a book by partial title match
> - Finding books when collection is empty
> - File permission errors during save
> - Concurrent access to the book collection
```

### 既存ファイルへのテスト追加

単一の関数に対する*追加の*テストを依頼し、Copilot CLIが既存のテストを補完する新しいケースを生成するようにします。

```bash
copilot

> @samples/book-app-project/books.py
> Generate additional tests for the find_by_author function with edge cases:
> - Author name with hyphens (e.g., "Jean-Paul Sartre")
> - Author with multiple first names
> - Empty string as author
> - Author name with accented characters
```

</details>

---

<a id="workflow-5-git-integration"></a>
<details>
<summary><strong>ワークフロー5：Git連携</strong> - コミットメッセージ、PRの説明、/pr、/delegate、/diff</summary>

<img src="images/git-integration-swimlane-single.png" alt="Git Integration workflow: stage changes, generate message, commit, create PR." width="800"/>

> 💡 **このワークフローはGitの基本知識を前提としています**（ステージング、コミット、ブランチ）。Gitが初めての方は、先に他の4つのワークフローを試してみてください。

### コミットメッセージの生成

> **まずこれを試してみよう：** `copilot -p "Generate a conventional commit message for: $(git diff --staged)"` — 変更をステージしてからこれを実行し、Copilot CLIがコミットメッセージを書くのを確認しましょう。

この例では、`-p`インラインプロンプトフラグとシェルコマンド置換を使って、`git diff`の出力を直接Copilot CLIにパイプし、ワンショットでコミットメッセージを生成します。`$(...)`構文は括弧内のコマンドを実行し、その出力を外側のコマンドに挿入します。

```bash

# 変更内容を確認
git diff --staged

# [Conventional Commit](../GLOSSARY.md#conventional-commit)フォーマットでコミットメッセージを生成
# （"feat(books): add search"や"fix(data): handle empty input"のような構造化されたメッセージ）
copilot -p "Generate a conventional commit message for: $(git diff --staged)"

# 出力: "feat(books): add partial author name search
#
# - Update find_by_author to support partial matches
# - Add case-insensitive comparison
# - Improve user experience when searching authors"
```

---

<details>
<summary>🎬 実際の動作を見てみよう！</summary>

![Git Integration Demo](images/git-integration-demo.gif)

*デモの出力は異なります。お使いのモデル、ツール、レスポンスはここに表示されているものとは異なります。*

</details>

---

### 変更内容の説明

`git show`の出力を`-p`プロンプトにパイプして、最後のコミットの平易な日本語での要約を取得します。

```bash
# このコミットで何が変わったか？
copilot -p "Explain what this commit does: $(git show HEAD --stat)"
```

### PRの説明

`git log`の出力と構造化されたプロンプトテンプレートを組み合わせて、完全なプルリクエストの説明を自動生成します。

```bash
# ブランチの変更からPRの説明を生成
copilot -p "Generate a pull request description for these changes:
$(git log main..HEAD --oneline)

Include:
- Summary of changes
- Why these changes were made
- Testing done
- Breaking changes? (yes/no)"
```

### インタラクティブモードでの/prの使用（現在のブランチ用）

Copilot CLIのインタラクティブモードでブランチを操作している場合、`/pr`コマンドを使ってプルリクエストを操作できます。`/pr`を使用して、PRの表示、新規PRの作成、既存PRの修正、またはブランチの状態に基づいてCopilot CLIに自動判断させることができます。

```bash
copilot

> /pr [view|create|fix|auto]
```

### プッシュ前のレビュー

`-p`プロンプト内で`git diff main..HEAD`を使用して、すべてのブランチ変更に対するプッシュ前の簡易チェックを行います。

```bash
# プッシュ前の最終チェック
copilot -p "Review these changes for issues before I push:
$(git diff main..HEAD)"
```

### /delegateによるバックグラウンドタスク

`/delegate`コマンドは作業をGitHub上のCopilotコーディングエージェントに引き渡します。`/delegate`スラッシュコマンド（または`&`ショートカット）を使用して、明確に定義されたタスクをバックグラウンドエージェントにオフロードします。

```bash
copilot

> /delegate Add input validation to the login form

# または&プレフィックスショートカットを使用：
> & Fix the typo in the README header

# Copilot CLI:
# 1. 変更を新しいブランチにコミット
# 2. ドラフトプルリクエストを開く
# 3. GitHub上でバックグラウンドで作業
# 4. 完了後にレビューをリクエスト
```

これは、他の作業に集中している間に完了させたい明確に定義されたタスクに最適です。

### /diffでセッションの変更をレビュー

`/diff`コマンドは現在のセッション中に行われたすべての変更を表示します。このスラッシュコマンドを使って、コミット前にCopilot CLIが変更したすべてのファイルのビジュアルdiffを確認できます。

```bash
copilot

# 変更を加えた後...
> /diff

# このセッションで変更されたすべてのファイルのビジュアルdiffを表示
# コミット前のレビューに最適
```

</details>

---

## クイックヒント：計画やコーディングの前にリサーチ

ライブラリの調査、ベストプラクティスの理解、または馴染みのないトピックの探索が必要な場合は、コードを書く前に`/research`を使って詳細なリサーチ調査を実行しましょう：

```bash
copilot

> /research What are the best Python libraries for validating user input in CLI apps?
```

CopilotがGitHubリポジトリやWebソースを検索し、参考文献付きの要約を返します。新機能の開発を始める前に情報に基づいた判断をしたい場合に便利です。結果は`/share`で共有できます。

> 💡 **ヒント**: `/research`は`/plan`の*前に*使うと効果的です。まずアプローチをリサーチしてから、実装を計画しましょう。

---

## すべてをまとめる：バグ修正ワークフロー

報告されたバグを修正するための完全なワークフローはこちらです：

```bash

# 1. バグレポートを理解する
copilot

> Users report: 'Finding books by author name doesn't work for partial names'
> @samples/book-app-project/books.py Analyze and identify the likely cause

# 2. 問題をデバッグする（同じセッションで続行）
> Based on the analysis, show me the find_by_author function and explain the issue

> Fix the find_by_author function to handle partial name matches

# 3. 修正のテストを生成する
> @samples/book-app-project/books.py Generate pytest tests specifically for:
> - Full author name match
> - Partial author name match
> - Case-insensitive matching
> - Author name not found

# 4. コミットメッセージを生成する
copilot -p "Generate commit message for: $(git diff --staged)"

# 出力: "fix(books): support partial author name search"
```

### バグ修正ワークフローのまとめ

| ステップ | アクション | Copilotコマンド |
|------|--------|-----------------|
| 1 | バグを理解する | `> [バグの説明] @relevant-file.py Analyze the likely cause` |
| 2 | 詳細な分析を得る | `> Show me the function and explain the issue` |
| 3 | 修正を実装する | `> Fix the [具体的な問題]` |
| 4 | テストを生成する | `> Generate tests for [具体的なシナリオ]` |
| 5 | コミットする | `copilot -p "Generate commit message for: $(git diff --staged)"` |

---

# 実践

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

今度はあなたがこれらのワークフローを実際に試す番です。

---

## ▶️ 自分で試してみよう

デモを完了したら、以下のバリエーションを試してみてください：

1. **バグ探偵チャレンジ**: `samples/book-app-buggy/books_buggy.py`の`mark_as_read`関数のデバッグをCopilot CLIに依頼しましょう。1冊だけでなく全ての本が既読になってしまう理由を説明してくれましたか？

2. **テストチャレンジ**: ブックアプリの`add_book`関数のテストを生成しましょう。あなたが思いつかなかったであろうエッジケースをCopilot CLIがいくつ含めているか数えてみてください。

3. **コミットメッセージチャレンジ**: ブックアプリのファイルに小さな変更を加え、ステージし（`git add .`）、次を実行してください：
   ```bash
   copilot -p "Generate a conventional commit message for: $(git diff --staged)"
   ```
   そのメッセージは、あなたが素早く書いたものよりも良いですか？

**セルフチェック**: 「このバグをデバッグして」が「バグを見つけて」よりも強力である理由を説明できれば、開発ワークフローを理解しています（コンテキストが重要！）。

---

## 📝 課題

### メインチャレンジ：リファクタリング、テスト、そしてシップ

ハンズオンの例では`find_book_by_title`とコードレビューに焦点を当てました。今度は`book-app-project`の別の関数で同じワークフロースキルを練習しましょう：

1. **レビュー**: `books.py`の`remove_book()`のエッジケースと潜在的な問題をCopilot CLIにレビューしてもらいましょう：
   `@samples/book-app-project/books.py Review the remove_book() function. What happens if the title partially matches another book (e.g., "Dune" vs "Dune Messiah")? Are there any edge cases not handled?`
2. **リファクタリング**: 大文字小文字を区別しないマッチングや、本が見つからない場合に有用なフィードバックを返すなど、エッジケースに対応するよう`remove_book()`の改善をCopilot CLIに依頼しましょう
3. **テスト**: 改善された`remove_book()`関数に特化したpytestテストを生成しましょう。以下をカバーしてください：
   - 存在する本の削除
   - 大文字小文字を区別しないタイトルマッチング
   - 存在しない本に対する適切なフィードバックの返却
   - 空のコレクションからの削除
4. **レビュー**: 変更をステージし、`/review`を実行して残りの問題がないか確認しましょう
5. **コミット**: Conventional Commitメッセージを生成しましょう：
   `copilot -p "Generate a conventional commit message for: $(git diff --staged)"`

<details>
<summary>💡 ヒント（クリックで展開）</summary>

**各ステップのサンプルプロンプト：**

```bash
copilot

# ステップ1：レビュー
> @samples/book-app-project/books.py Review the remove_book() function. What edge cases are not handled?

# ステップ2：リファクタリング
> Improve remove_book() to use case-insensitive matching and return a clear message when the book isn't found. Show me the before and after code.

# ステップ3：テスト
> Generate pytest tests for the improved remove_book() function, including:
> - Removing a book that exists
> - Case-insensitive matching ("dune" should remove "Dune")
> - Book not found returns appropriate response
> - Removing from an empty collection

# ステップ4：レビュー
> /review

# ステップ5：コミット
> Generate a conventional commit message for this refactor
```

**ヒント:** `remove_book()`を改善した後、Copilot CLIに「このファイルの他の関数にも同じ改善が有効ですか？」と聞いてみてください。`find_book_by_title()`や`find_by_author()`にも同様の変更を提案するかもしれません。

</details>

### ボーナスチャレンジ：Copilot CLIでアプリケーションを作成する

> 💡 **注**: このGitHub Skillsの演習ではPythonではなく**Node.js**を使用します。練習するGitHub Copilot CLIのテクニック（Issueの作成、コードの生成、ターミナルからのコラボレーション）はどの言語にも適用できます。

この演習では、GitHub Copilot CLIを使ってIssueを作成し、コードを生成し、Node.jsの電卓アプリを構築しながらターミナルからコラボレーションする方法を紹介します。CLIのインストール、テンプレートとエージェントの使用、反復的なコマンドライン駆動の開発を練習します。

##### <img src="../images/github-skills-logo.png" width="28" align="center" /> [「Copilot CLIでアプリケーションを作成する」Skills演習を始める](https://github.com/skills/create-applications-with-the-copilot-cli)

---

<details>
<summary>🔧 <strong>よくある間違いとトラブルシューティング</strong>（クリックで展開）</summary>

### よくある間違い

| 間違い | 起こること | 修正方法 |
|---------|--------------|-----|
| 「このコードをレビューして」のような曖昧なプロンプトを使う | 具体的な問題を見逃す一般的なフィードバック | 具体的に指定する：「SQLインジェクション、XSS、認証の問題をレビューして」 |
| コードレビューに`/review`を使わない | 最適化されたcode-reviewエージェントを活用できない | 高いシグナル対ノイズ比の出力に調整された`/review`を使用する |
| コンテキストなしに「バグを見つけて」と依頼する | Copilot CLIがどのバグを経験しているかわからない | 症状を説明する：「Yをすると、ユーザーがXの症状を報告する」 |
| フレームワークを指定せずにテストを生成する | 間違った構文やアサーションライブラリのテストが生成される場合がある | 指定する：「Jestを使ったテストを生成して」または「pytestを使って」 |

### トラブルシューティング

**レビューが不完全に見える** - 何を探すべきかをより具体的に：

```bash
copilot

# こうではなく：
> Review @samples/book-app-project/book_app.py

# こう試す：
> Review @samples/book-app-project/book_app.py for input validation, error handling, and edge cases
```

**テストが使用フレームワークと一致しない** - フレームワークを指定する：

```bash
copilot

> @samples/book-app-project/books.py Generate tests using pytest (not unittest)
```

**リファクタリングが動作を変更してしまう** - Copilot CLIに動作の保持を依頼する：

```bash
copilot

> @samples/book-app-project/book_app.py Refactor command handling to use dictionary dispatch. IMPORTANT: Maintain identical external behavior - no breaking changes
```

</details>

---

# まとめ

## 🔑 重要なポイント

<img src="images/specialized-workflows.png" alt="Specialized Workflows for Every Task: Code Review, Refactoring, Debugging, Testing, and Git Integration" width="800"/>

1. **コードレビュー**は具体的なプロンプトで包括的になる
2. **リファクタリング**はテストを先に生成することでより安全になる
3. **デバッグ**はエラーとコードの両方をCopilot CLIに見せることで効果が上がる
4. **テスト生成**にはエッジケースとエラーシナリオを含めるべき
5. **Git連携**はコミットメッセージとPRの説明を自動化する

> 📋 **クイックリファレンス**: コマンドとショートカットの完全なリストは[GitHub Copilot CLIコマンドリファレンス](https://docs.github.com/en/copilot/reference/cli-command-reference)を参照してください。

---

## ✅ チェックポイント：基礎をマスターしました

**おめでとうございます！** これでGitHub Copilot CLIで生産性を発揮するためのすべてのコアスキルを身につけました：

| スキル | 章 | できるようになったこと |
|-------|---------|----------------|
| 基本コマンド | Ch 01 | インタラクティブモード、プランモード、プログラマティックモード（-p）、スラッシュコマンドの使用 |
| コンテキスト | Ch 02 | `@`でのファイル参照、セッション管理、コンテキストウィンドウの理解 |
| ワークフロー | Ch 03 | コードレビュー、リファクタリング、デバッグ、テスト生成、Git連携 |

Ch 04〜06ではさらに強力な追加機能を取り上げており、学ぶ価値があります。

---

## 🛠️ 自分だけのワークフローを構築する

GitHub Copilot CLIの「唯一の正解」はありません。自分のパターンを開発する際のヒントをいくつか紹介します：

> 📚 **公式ドキュメント**: GitHubが推奨するワークフローとヒントは[Copilot CLIベストプラクティス](https://docs.github.com/copilot/how-tos/copilot-cli/cli-best-practices)を参照してください。

- **重要な作業には`/plan`から始める。** 実行前にプランを洗練させましょう。良いプランがより良い結果につながります。
- **うまくいったプロンプトを保存する。** Copilot CLIが間違えたときは何が問題だったかをメモしましょう。時間とともに、あなた専用のプレイブックになります。
- **自由に実験する。** 長くて詳細なプロンプトを好む開発者もいれば、短いプロンプトとフォローアップを好む開発者もいます。さまざまなアプローチを試して、自然に感じるものを見つけましょう。

> 💡 **次の章では**: Ch 04と05で、ベストプラクティスをCopilot CLIが自動的に読み込むカスタム指示とスキルに体系化する方法を学びます。

---

## ➡️ 次のステップ

残りの章では、Copilot CLIの機能を拡張する追加機能を扱います：

| 章 | 内容 | 必要になる場面 |
|---------|----------------|---------------------|
| Ch 04: エージェント | 専門的なAIペルソナを作成 | ドメインエキスパート（フロントエンド、セキュリティ）が必要なとき |
| Ch 05: スキル | タスク用の自動読み込み指示 | 同じプロンプトを繰り返し使うとき |
| Ch 06: MCP | 外部サービスとの接続 | GitHub、データベースなどのライブデータが必要なとき |

**おすすめ**: コアワークフローを1週間試してから、具体的なニーズができたときにCh 04〜06に戻ってきましょう。

---

## 追加トピックへ進む

**[Chapter 04: エージェントとカスタム指示](../04-agents-custom-instructions/README.ja.md)**では、以下を学びます：

- 組み込みエージェント（`/plan`、`/review`）の使用
- `.agent.md`ファイルによる専門エージェント（フロントエンドエキスパート、セキュリティ監査者）の作成
- マルチエージェントコラボレーションパターン
- プロジェクト標準のためのカスタム指示ファイル

---

**[← Chapter 02に戻る](../02-context-conversations/README.ja.md)** | **[Chapter 04へ進む →](../04-agents-custom-instructions/README.ja.md)**
