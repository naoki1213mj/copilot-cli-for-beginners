![Chapter 07: Putting It All Together](images/chapter-header.png)

> **これまでに学んだすべてがここで結集します。アイデアからマージ済みPRまでを1回のセッションで実現しましょう。**

この章では、これまでに学んだことをすべて組み合わせて完全なワークフローを構築します。マルチエージェント連携による機能開発、コミット前にセキュリティ問題を検出するpre-commitフックの設定、CI/CDパイプラインへのCopilotの統合、そしてアイデアからマージ済みPRまでを1つのターミナルセッションで実現する方法を学びます。ここでGitHub Copilot CLIが真の生産性向上ツールとなります。

> 💡 **注意**: この章では、これまでに学んだすべてを組み合わせる方法を紹介します。**エージェント、スキル、MCPがなくても生産的に作業できます（ただし、あると非常に便利です）。** コアワークフロー — 説明、計画、実装、テスト、レビュー、出荷 — は、第00〜03章の組み込み機能だけで動作します。

## 🎯 学習目標

この章を終えると、以下ができるようになります：

- エージェント、スキル、MCP（Model Context Protocol）を統合ワークフローで組み合わせる
- マルチツールアプローチで完全な機能を構築する
- フックを使った基本的な自動化を設定する
- プロフェッショナルな開発のベストプラクティスを適用する

> ⏱️ **所要時間の目安**: 約75分（読む時間15分 + ハンズオン60分）

---

## 🧩 実世界のたとえ話：オーケストラ

<img src="images/orchestra-analogy.png" alt="Orchestra Analogy - Unified Workflow" width="800"/>

交響楽団にはさまざまなセクションがあります：
- **弦楽器**は土台を提供します（コアワークフローのようなもの）
- **金管楽器**は力強さを加えます（専門知識を持つエージェントのようなもの）
- **木管楽器**は彩りを加えます（機能を拡張するスキルのようなもの）
- **打楽器**はリズムを保ちます（外部システムと接続するMCPのようなもの）

それぞれのセクションだけでは限られた音しか出せません。しかし、優れた指揮のもとで合わさると、壮大な作品が生まれます。

**この章が教えるのはまさにそれです！**<br>
*オーケストラの指揮者のように、エージェント、スキル、MCPを統合ワークフローへとオーケストレーションします*

まず、コードの変更、テストの生成、レビュー、PRの作成を1つのセッションで行うシナリオを見ていきましょう。

---

## アイデアからマージ済みPRまでを1セッションで

エディタ、ターミナル、テストランナー、GitHub UIを切り替えるたびにコンテキストを失う代わりに、すべてのツールを1つのターミナルセッションで組み合わせることができます。このパターンは、以下の[統合パターン](#パワーユーザー向けの統合パターン)セクションで詳しく説明します。

```bash
# Copilotをインタラクティブモードで起動
copilot

> I need to add a "list unread" command to the book app that shows only
> books where read is False. What files need to change?

# Copilotが大まかな計画を作成...

# PYTHON-REVIEWERエージェントに切り替え
> /agent
# "python-reviewer"を選択

> @samples/book-app-project/books.py Design a get_unread_books method.
> What is the best approach?

# Python-reviewerエージェントが以下を生成：
# - メソッドのシグネチャと戻り値の型
# - リスト内包表記を使ったフィルタ実装
# - 空のコレクションに対するエッジケースの処理

# PYTEST-HELPERエージェントに切り替え
> /agent
# "pytest-helper"を選択

> @samples/book-app-project/tests/test_books.py Design test cases for
> filtering unread books.

# Pytest-helperエージェントが以下を生成：
# - 空のコレクションのテストケース
# - 既読/未読が混在する場合のテストケース
# - すべて既読の場合のテストケース

# 実装
> Add a get_unread_books method to BookCollection in books.py
> Add a "list unread" command option in book_app.py
> Update the help text in the show_help function

# テスト
> Generate comprehensive tests for the new feature

# 以下のような複数のテストが生成されます：
# - 正常系（3テスト）— 正しくフィルタリング、既読を除外、未読を含む
# - エッジケース（4テスト）— 空のコレクション、すべて既読、未読なし、1冊のみ
# - パラメータ化（5ケース）— @pytest.mark.parametrizeで既読/未読の割合を変えて検証
# - 統合テスト（4テスト）— mark_as_read、remove_book、add_book、データ整合性との相互作用

# 変更をレビュー
> /review

# レビューに問題がなければ、/prで現在のブランチのPRを操作
> /pr [view|create|fix|auto]

# または、ターミナルからCopilotにPRの下書きを自然に依頼
> Create a pull request titled "Feature: Add list unread books command"
```

**従来のアプローチ**: エディタ、ターミナル、テストランナー、ドキュメント、GitHub UIを切り替え。切り替えるたびにコンテキストが失われ、摩擦が生じます。

**重要なポイント**: あなたはアーキテクトのようにスペシャリストに指示を出しました。詳細は彼らが処理しました。あなたはビジョンを担いました。

> 💡 **さらに一歩進める**: このような大規模なマルチステップの計画には、`/fleet`を使ってCopilotに独立したサブタスクを並列実行させてみてください。詳細は[公式ドキュメント](https://docs.github.com/copilot/concepts/agents/copilot-cli/fleet)を参照してください。

---

# その他のワークフロー

<img src="images/combined-workflows.png" alt="People assembling a colorful giant jigsaw puzzle with gears, representing how agents, skills, and MCP combine into unified workflows" width="800"/>

第04〜06章を完了したパワーユーザー向けに、エージェント、スキル、MCPがどのように効果を倍増させるかを示すワークフローです。

## 統合パターン

すべてを組み合わせるためのメンタルモデルはこちらです：

<img src="images/integration-pattern.png" alt="The Integration Pattern - A 4-phase workflow: Gather Context (MCP), Analyze and Plan (Agents), Execute (Skills + Manual), Complete (MCP)" width="800"/>

---

## ワークフロー1：バグ調査と修正

完全なツール統合による実践的なバグ修正：

```bash
copilot

# フェーズ1：GitHubからバグの詳細を取得（MCPが提供）
> Get the details of issue #1

# 学び：「find_by_authorが部分名で動作しない」

# フェーズ2：ベストプラクティスの調査（Web + GitHubソースによるディープリサーチ）
> /research Best practices for Python case-insensitive string matching

# フェーズ3：関連コードの確認
> @samples/book-app-project/books.py Show me the find_by_author method

# フェーズ4：エキスパートの分析
> /agent
# "python-reviewer"を選択

> Analyze this method for issues with partial name matching

# エージェントの指摘：メソッドが部分文字列マッチングではなく完全一致を使用している

# フェーズ5：エージェントのガイダンスに基づいて修正
> Implement the fix using lowercase comparison and 'in' operator

# フェーズ6：テストの生成
> /agent
# "pytest-helper"を選択

> Generate pytest tests for find_by_author with partial matches
> Include test cases: partial name, case variations, no matches

# フェーズ7：コミットとPR
> Generate a commit message for this fix

> Create a pull request linking to issue #1
```

---

## ワークフロー2：コードレビューの自動化（オプション）

> 💡 **このセクションはオプションです。** pre-commitフックはチームにとって便利ですが、生産的に作業するために必須ではありません。始めたばかりの方はスキップしても構いません。
>
> ⚠️ **パフォーマンスに関する注意**: このフックはステージングされたファイルごとに`copilot -p`を呼び出すため、ファイルごとに数秒かかります。大きなコミットの場合は、重要なファイルに限定するか、代わりに`/review`で手動レビューを行うことを検討してください。

**gitフック**とは、特定のタイミングでGitが自動的に実行するスクリプトです。たとえば、コミットの直前に実行されます。これを使ってコードの自動チェックを行えます。以下は、コミットに対してCopilotの自動レビューを設定する方法です：

```bash
# pre-commitフックを作成
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash

# ステージングされたファイルを取得（Pythonファイルのみ）
STAGED=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.py$')

if [ -n "$STAGED" ]; then
  echo "Running Copilot review on staged files..."

  for file in $STAGED; do
    echo "Reviewing $file..."

    # ハングを防ぐためにタイムアウトを使用（ファイルごとに60秒）
    # --allow-allはファイルの読み書きを自動承認し、フックを無人で実行できるようにします。
    # 自動スクリプトでのみ使用してください。インタラクティブセッションでは、Copilotに許可を求めさせてください。
    REVIEW=$(timeout 60 copilot --allow-all -p "Quick security review of @$file - critical issues only" 2>/dev/null)

    # タイムアウトが発生したか確認
    if [ $? -eq 124 ]; then
      echo "Warning: Review timed out for $file (skipping)"
      continue
    fi

    if echo "$REVIEW" | grep -qi "CRITICAL"; then
      echo "Critical issues found in $file:"
      echo "$REVIEW"
      exit 1
    fi
  done

  echo "Review passed"
fi
EOF

chmod +x .git/hooks/pre-commit
```

> ⚠️ **macOSユーザーへ**: `timeout`コマンドはmacOSにはデフォルトで含まれていません。`brew install coreutils`でインストールするか、`timeout 60`をタイムアウトガードなしの単純な呼び出しに置き換えてください。

> 📚 **公式ドキュメント**: フックの完全なAPIについては、[フックの使用方法](https://docs.github.com/copilot/how-tos/copilot-cli/use-hooks)と[フック設定リファレンス](https://docs.github.com/copilot/reference/hooks-configuration)を参照してください。
>
> 💡 **組み込みの代替手段**: Copilot CLIには、pre-commitなどのイベントで自動実行できる組み込みフックシステム（`copilot hooks`）もあります。上記の手動gitフックは完全な制御を提供し、組み込みシステムはより簡単に設定できます。どちらのアプローチがワークフローに適しているかは、上記のドキュメントを参照してください。

これで、すべてのコミットに対して簡易セキュリティレビューが実行されます：

```bash
git add samples/book-app-project/books.py
git commit -m "Update book collection methods"

# 出力：
# Running Copilot review on staged files...
# Reviewing samples/book-app-project/books.py...
# Critical issues found in samples/book-app-project/books.py:
# - Line 15: File path injection vulnerability in load_from_file
#
# Fix the issue and try again.
```

---

## ワークフロー3：新しいコードベースへのオンボーディング

新しいプロジェクトに参加する際に、コンテキスト、エージェント、MCPを組み合わせて素早くキャッチアップできます：

```bash
# Copilotをインタラクティブモードで起動
copilot

# フェーズ1：コンテキストで全体像を把握
> @samples/book-app-project/ Explain the high-level architecture of this codebase

# フェーズ2：特定のフローを理解する
> @samples/book-app-project/book_app.py Walk me through what happens
> when a user runs "python book_app.py add"

# フェーズ3：エージェントでエキスパートの分析を得る
> /agent
# "python-reviewer"を選択

> @samples/book-app-project/books.py Are there any design issues,
> missing error handling, or improvements you would recommend?

# フェーズ4：取り組む課題を見つける（MCPがGitHubアクセスを提供）
> List open issues labeled "good first issue"

# フェーズ5：コントリビューションを開始
> Pick the simplest open issue and outline a plan to fix it
```

このワークフローは、`@`コンテキスト、エージェント、MCPを1回のオンボーディングセッションに組み合わせたもので、この章の前半で紹介した統合パターンそのものです。

---

# ベストプラクティスと自動化

ワークフローをより効果的にするパターンと習慣です。

---

## ベストプラクティス

### 1. 分析の前にまずコンテキストを収集する

分析を依頼する前に、必ずコンテキストを収集しましょう：

```bash
# 良い例
> Get the details of issue #42
> /agent
# python-reviewerを選択
> Analyze this issue

# 効果が低い例
> /agent
# python-reviewerを選択
> Fix login bug
# エージェントにissueのコンテキストがない
```

### 2. エージェント、スキル、カスタムインストラクションの違いを理解する

各ツールには得意分野があります：

```bash
# エージェント：明示的に有効化する専門的なペルソナ
> /agent
# python-reviewerを選択
> Review this authentication code for security issues

# スキル：プロンプトがスキルの説明に一致すると自動で有効になるモジュール機能
# （先に作成する必要があります — 第05章を参照）
> Generate comprehensive tests for this code
# テストスキルが設定されていれば、自動的に有効化されます

# カスタムインストラクション（.github/copilot-instructions.md）：常に有効な
# ガイダンスで、切り替えやトリガーなしにすべてのセッションに適用されます
```

> 💡 **重要なポイント**: エージェントとスキルはどちらもコードの分析と生成が可能です。本当の違いは**有効化の方法**です — エージェントは明示的（`/agent`）、スキルは自動（プロンプトマッチ）、カスタムインストラクションは常時有効です。

### 3. セッションを集中させる

`/rename`でセッションにラベルを付け（履歴で見つけやすくなります）、`/exit`でクリーンに終了しましょう：

```bash
# 良い例：1つの機能ごとに1セッション
> /rename list-unread-feature
# 未読リスト機能に取り組む
> /exit

copilot
> /rename export-csv-feature
# CSVエクスポート機能に取り組む
> /exit

# 効果が低い例：1つの長いセッションですべてを行う
```

### 4. Copilotでワークフローを再利用可能にする

ワークフローをWikiにドキュメント化するだけでなく、Copilotが使えるようにリポジトリに直接エンコードしましょう：

- **カスタムインストラクション**（`.github/copilot-instructions.md`）：コーディング標準、アーキテクチャルール、ビルド/テスト/デプロイ手順に対する常時有効なガイダンス。すべてのセッションで自動的に従います。
- **プロンプトファイル**（`.github/prompts/`）：チームで共有できる再利用可能なパラメータ化されたプロンプト — コードレビュー、コンポーネント生成、PR説明文のテンプレートのようなものです。
- **カスタムエージェント**（`.github/agents/`）：チームの誰もが`/agent`で有効化できる専門的なペルソナ（セキュリティレビューアーやドキュメントライターなど）をエンコードします。
- **カスタムスキル**（`.github/skills/`）：関連する場面で自動的に有効化されるステップバイステップのワークフロー手順をパッケージ化します。

> 💡 **メリット**: 新しいチームメンバーは、ワークフローを無料で手に入れられます — 誰かの頭の中ではなく、リポジトリに組み込まれています。

---

## ボーナス：プロダクションパターン

これらのパターンはオプションですが、プロフェッショナルな環境では価値があります。

### PR説明文ジェネレーター

```bash
# 包括的なPR説明文を生成
BRANCH=$(git branch --show-current)
COMMITS=$(git log main..$BRANCH --oneline)

copilot -p "Generate a PR description for:
Branch: $BRANCH
Commits:
$COMMITS

Include: Summary, Changes Made, Testing Done, Screenshots Needed"
```

### CI/CDとの統合

既存のCI/CDパイプラインを持つチームの場合、GitHub Actionsを使ってすべてのPRに対してCopilotレビューを自動化できます。レビューコメントの自動投稿や重要な問題のフィルタリングが含まれます。

> 📖 **詳細**: GitHub Actionsワークフローの完全版、設定オプション、トラブルシューティングのヒントについては、[CI/CD統合](../appendices/ci-cd-integration.md)を参照してください。

---

# 練習

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

完全なワークフローを実践してみましょう。

---

## ▶️ 自分で試してみよう

デモを完了したら、以下のバリエーションを試してみてください：

1. **エンドツーエンドチャレンジ**: 小さな機能を選びます（例：「未読の本を一覧表示」や「CSVにエクスポート」）。完全なワークフローを使います：
   - `/plan`で計画
   - エージェント（python-reviewer、pytest-helper）で設計
   - 実装
   - テスト生成
   - PR作成

2. **自動化チャレンジ**: コードレビュー自動化ワークフローのpre-commitフックを設定します。意図的にファイルパスの脆弱性を含むコミットを行ってみてください。ブロックされますか？

3. **あなた自身のプロダクションワークフロー**: よく行うタスクに対して独自のワークフローを設計してください。チェックリストとして書き出しましょう。スキル、エージェント、フックで自動化できる部分はどこですか？

**セルフチェック**: エージェント、スキル、MCPがどのように連携するか、そしてそれぞれをいつ使うべきかを同僚に説明できれば、このコースを完了したことになります。

---

## 📝 課題

### メインチャレンジ：エンドツーエンドの機能開発

ハンズオンの例では「未読の本を一覧表示」機能の構築を説明しました。今度は別の機能で完全なワークフローを練習しましょう：**年の範囲で本を検索**：

1. Copilotを起動してコンテキストを収集：`@samples/book-app-project/books.py`
2. `/plan Add a "search by year" command that lets users find books published between two years`で計画
3. `BookCollection`に`find_by_year_range(start_year, end_year)`メソッドを実装
4. `book_app.py`に`handle_search_year()`関数を追加して、ユーザーに開始年と終了年を入力させる
5. テストを生成：`@samples/book-app-project/books.py @samples/book-app-project/tests/test_books.py Generate tests for find_by_year_range() including edge cases like invalid years, reversed range, and no results.`
6. `/review`でレビュー
7. READMEを更新：`@samples/book-app-project/README.md Add documentation for the new "search by year" command.`
8. コミットメッセージを生成

作業中にワークフローをドキュメント化しましょう。

**成功基準**: 計画、実装、テスト、ドキュメント、レビューを含め、Copilot CLIを使ってアイデアからコミットまでの機能開発を完了していること。

> 💡 **ボーナス**: 第04章でエージェントを設定済みの場合は、カスタムエージェントの作成と使用を試してみてください。たとえば、実装レビュー用のerror-handlerエージェントやREADME更新用のdoc-writerエージェントなどです。

<details>
<summary>💡 ヒント（クリックして展開）</summary>

**この章の冒頭にある[「アイデアからマージ済みPR」](#アイデアからマージ済みprまでを1セッションで)の例に従ってください。** 主な手順は以下の通りです：

1. `@samples/book-app-project/books.py`でコンテキストを収集
2. `/plan Add a "search by year" command`で計画
3. メソッドとコマンドハンドラを実装
4. エッジケース付きのテストを生成（無効な入力、空の結果、逆順の範囲）
5. `/review`でレビュー
6. `@samples/book-app-project/README.md`でREADMEを更新
7. `-p`でコミットメッセージを生成

**考慮すべきエッジケース：**
- ユーザーが「2000」と「1990」を入力した場合（逆順の範囲）はどうなるか？
- 範囲に一致する本がない場合はどうなるか？
- ユーザーが数値以外の入力をした場合はどうなるか？

**重要なのは完全なワークフローの練習です**：アイデア → コンテキスト → 計画 → 実装 → テスト → ドキュメント → コミット。

</details>

---

<details>
<summary>🔧 <strong>よくある間違い</strong>（クリックして展開）</summary>

| 間違い | 何が起こるか | 修正方法 |
|--------|------------|---------|
| すぐに実装に取りかかる | 後から修正コストが高い設計上の問題を見落とす | まず`/plan`を使ってアプローチを検討する |
| 複数のツールが役立つのに1つだけ使う | 結果が遅く、不十分になる | 組み合わせる：分析にエージェント → 実行にスキル → 統合にMCP |
| コミット前にレビューしない | セキュリティ問題やバグが紛れ込む | 必ず`/review`を実行するか、[pre-commitフック](#ワークフロー2コードレビューの自動化オプション)を使用する |
| ワークフローをチームと共有しない | 各自が車輪の再発明をする | 共有のエージェント、スキル、インストラクションにパターンをドキュメント化する |

</details>

---

# まとめ

## 🔑 重要なポイント

1. **統合 > 分離**: ツールを組み合わせて最大の効果を
2. **まずコンテキスト**: 分析の前に必要なコンテキストを収集
3. **エージェントが分析、スキルが実行**: 適材適所でツールを使う
4. **繰り返しを自動化**: フックとスクリプトで効果を倍増
5. **ワークフローをドキュメント化**: 共有可能なパターンがチーム全体に利益をもたらす

> 📋 **クイックリファレンス**: コマンドとショートカットの完全なリストについては、[GitHub Copilot CLIコマンドリファレンス](https://docs.github.com/en/copilot/reference/cli-command-reference)を参照してください。

---

## 🎓 コース完了！

おめでとうございます！以下を学びました：

| 章 | 学んだこと |
|----|-----------|
| 00 | Copilot CLIのインストールとクイックスタート |
| 01 | 3つの対話モード |
| 02 | @構文によるコンテキスト管理 |
| 03 | 開発ワークフロー |
| 04 | 専門エージェント |
| 05 | 拡張可能なスキル |
| 06 | MCPによる外部接続 |
| 07 | 統合されたプロダクションワークフロー |

これで、GitHub Copilot CLIを開発ワークフローにおける真の生産性向上ツールとして活用する準備が整いました。

## ➡️ 次のステップ

学びはここで終わりではありません：

1. **毎日練習する**: 実際の作業でCopilot CLIを使う
2. **カスタムツールを作る**: 自分のニーズに合ったエージェントやスキルを作成する
3. **知識を共有する**: チームがこれらのワークフローを導入するのを助ける
4. **最新情報を追う**: GitHub Copilotのアップデートで新機能をフォローする

### リソース

- [GitHub Copilot CLIドキュメント](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)
- [MCPサーバーレジストリ](https://github.com/modelcontextprotocol/servers)
- [コミュニティスキル](https://github.com/topics/copilot-skill)

---

**お疲れ様でした！さあ、素晴らしいものを作りましょう。**

**[← 第06章に戻る](../06-mcp-servers/README.ja.md)** | **[コースホームに戻る →](../README.ja.md)**
