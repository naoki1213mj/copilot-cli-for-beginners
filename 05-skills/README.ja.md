![Chapter 05: Skills システム](images/chapter-header.png)

> **チームのベストプラクティスを毎回説明しなくても、Copilot が自動的に適用してくれたらどうでしょう？**

この章では、Agent Skills（エージェントスキル）について学びます。スキルとは、タスクに関連する場合に Copilot が自動的に読み込む指示が入ったフォルダです。エージェントが Copilot の*考え方*を変えるのに対し、スキルは Copilot に*特定のタスクの実行方法*を教えます。セキュリティ監査スキルを作成してセキュリティに関する質問時に自動適用させたり、チーム標準のレビュー基準を構築して一貫したコード品質を確保したり、Copilot CLI、VS Code、Copilot coding agent 全体でスキルがどのように機能するかを学びます。


## 🎯 学習目標

この章を終えると、以下のことができるようになります：

- Agent Skills の仕組みと使用するタイミングを理解する
- SKILL.md ファイルを使ってカスタムスキルを作成する
- 共有リポジトリのコミュニティスキルを使用する
- スキル・エージェント・MCP の使い分けを理解する

> ⏱️ **想定所要時間**: 約55分（読み物20分 + ハンズオン35分）

---

## 🧩 身近なたとえ話：電動工具

汎用のドリルも便利ですが、専用のアタッチメントを付けるとさらに強力になります。
<img src="images/power-tools-analogy.png" alt="電動工具 - スキルが Copilot の機能を拡張する" width="800"/>


スキルも同じ仕組みです。作業に応じてドリルビットを交換するように、タスクに応じて Copilot にスキルを追加できます：

| スキルアタッチメント | 用途 |
|------------|---------|
| `commit` | 一貫したコミットメッセージを生成する |
| `security-audit` | OWASP の脆弱性をチェックする |
| `generate-tests` | 包括的な pytest テストを作成する |
| `code-checklist` | チームのコード品質基準を適用する |



*スキルは Copilot の機能を拡張する専用のアタッチメントです*

---

# スキルの仕組み

<img src="images/how-skills-work.png" alt="星空の背景に光の軌跡で繋がれた、Copilot スキルを表す輝く RPG スタイルのスキルアイコン" width="800"/>

スキルとは何か、なぜ重要なのか、エージェントや MCP との違いを学びます。

---

## *スキルが初めての方は*こちらから！

1. **利用可能なスキルを確認する：**
   ```bash
   copilot
   > /skills list
   ```
   プロジェクトフォルダや個人フォルダにある、Copilot が検出できるすべてのスキルが表示されます。

2. **実際のスキルファイルを見てみる：** 提供されている [code-checklist SKILL.md](../.github/skills/code-checklist/SKILL.md) を確認してパターンを把握しましょう。YAML フロントマターと Markdown の指示文で構成されています。

3. **基本コンセプトを理解する：** スキルは、プロンプトがスキルの説明に一致したときに Copilot が*自動的に*読み込む、タスク固有の指示です。有効化する必要はなく、自然に質問するだけで使えます。


## スキルを理解する

Agent Skills は、タスクに**関連する場合に自動的に読み込まれる**指示、スクリプト、リソースが含まれたフォルダです。Copilot はプロンプトを読み取り、一致するスキルがあるかを確認し、関連する指示を自動的に適用します。

```bash
copilot

> Check books.py against our quality checklist
# Copilot は「code-checklist」スキルに一致すると検出し、
# Python の品質チェックリストを自動的に適用します

> Generate tests for the BookCollection class
# Copilot は「pytest-gen」スキルを読み込み、
# 好みのテスト構造を適用します

> What are the code quality issues in this file?
# Copilot は「code-checklist」スキルを読み込み、
# チームの基準に照らしてチェックします
```

> 💡 **重要なポイント**: スキルは、プロンプトがスキルの説明に一致すると**自動的にトリガー**されます。自然に質問するだけで、Copilot が裏側で関連するスキルを適用します。次に学ぶように、スキルを直接呼び出すこともできます。

> 🧰 **すぐに使えるテンプレート**: コピー＆ペーストで試せるシンプルなスキルは [.github/skills](../.github/skills/) フォルダをご覧ください。

### スラッシュコマンドによる直接呼び出し

自動トリガーがスキルの主な動作方法ですが、スキル名をスラッシュコマンドとして使って**直接呼び出す**こともできます：

```bash
> /generate-tests Create tests for the user authentication module

> /code-checklist Check books.py for code quality issues

> /security-audit Check the API endpoints for vulnerabilities
```

特定のスキルを確実に使いたい場合に、明示的な制御が可能です。

> 📝 **スキルとエージェントの呼び出しの違い**: スキルの呼び出しとエージェントの呼び出しを混同しないでください：
> - **スキル**: `/skill-name <プロンプト>`、例：`/code-checklist Check this file`
> - **エージェント**: `/agent`（リストから選択）または `copilot --agent <name>`（コマンドライン）
>
> 同じ名前（例：「code-reviewer」）のスキルとエージェントの両方がある場合、`/code-reviewer` と入力するとエージェントではなく**スキル**が呼び出されます。

### スキルが使用されたかどうかの確認方法

Copilot に直接聞くことができます：

```bash
> What skills did you use for that response?

> What skills do you have available for security reviews?
```

### スキル vs エージェント vs MCP

スキルは GitHub Copilot の拡張モデルの一部に過ぎません。エージェントや MCP サーバーとの比較は以下の通りです。

> *MCP についてはまだ心配しないでください。[Chapter 06](../06-mcp-servers/README.ja.md) で説明します。スキルが全体像のどこに位置するかを示すためにここに含めています。*

<img src="images/skills-agents-mcp-comparison.png" alt="エージェント、スキル、MCP サーバーの違いと、それらがワークフローにどう組み合わさるかを示す比較図" width="800"/>

| 機能 | 役割 | 使用するタイミング |
|---------|--------------|-------------|
| **エージェント** | AI の考え方を変える | 多くのタスクにわたる専門知識が必要な場合 |
| **スキル** | タスク固有の指示を提供する | 詳細な手順を伴う特定の反復タスク |
| **MCP** | 外部サービスに接続する | API からのリアルタイムデータが必要な場合 |

幅広い専門知識にはエージェントを、特定のタスク指示にはスキルを、外部データには MCP を使用します。エージェントは会話中に1つ以上のスキルを使用できます。たとえば、コードのチェックを依頼すると、エージェントは `security-audit` スキルと `code-checklist` スキルの両方を自動的に適用する場合があります。

> 📚 **詳細情報**: スキルのフォーマットとベストプラクティスの完全なリファレンスは、公式ドキュメント [About Agent Skills](https://docs.github.com/copilot/concepts/agents/about-agent-skills) をご覧ください。

---

## 手動プロンプトから自動的な専門知識へ

スキルの作成方法に入る前に、*なぜ*学ぶ価値があるのかを見てみましょう。一貫性の向上を実感すれば、「どうやって」の部分もより理解しやすくなります。

### スキル導入前：一貫性のないレビュー

コードレビューのたびに、何かを忘れてしまうかもしれません：

```bash
copilot

> Review this code for issues
# 一般的なレビュー - チーム固有の懸念事項を見落とす可能性があります
```

または、毎回長いプロンプトを書く必要があります：

```bash
> Review this code checking for bare except clauses, missing type hints,
> mutable default arguments, missing context managers for file I/O,
> functions over 50 lines, print statements in production code...
```

所要時間：入力に **30秒以上**。一貫性：**記憶力次第**。

### スキル導入後：自動的なベストプラクティス

`code-checklist` スキルをインストールすれば、自然に質問するだけです：

```bash
copilot

> Check the book collection code for quality issues
```

**裏側で起きていること**：
1. Copilot がプロンプト内の「code quality」と「issues」を検出
2. スキルの説明を確認し、`code-checklist` スキルが一致すると判断
3. チームの品質チェックリストを自動的に読み込み
4. すべてのチェックを一覧表示せずに適用

<img src="images/skill-auto-discovery-flow.png" alt="スキルの自動トリガーの仕組み - Copilot がプロンプトに適したスキルを自動的にマッチングする4ステップのフロー" width="800"/>

*自然に質問するだけで、Copilot がプロンプトに適したスキルをマッチングし自動的に適用します。*

**出力例**：
```
## Code Checklist: books.py

### Code Quality
- [PASS] All functions have type hints
- [PASS] No bare except clauses
- [PASS] No mutable default arguments
- [PASS] Context managers used for file I/O
- [PASS] Functions are under 50 lines
- [PASS] Variable and function names follow PEP 8

### Input Validation
- [FAIL] User input is not validated - add_book() accepts any year value
- [FAIL] Edge cases not fully handled - empty strings accepted for title/author
- [PASS] Error messages are clear and helpful

### Testing
- [FAIL] No corresponding pytest tests found

### Summary
3 items need attention before merge
```

**違い**: チームの基準が毎回自動的に適用され、入力する必要がありません。

---

<details>
<summary>🎬 実際の動作を見てみましょう！</summary>

![Skill Trigger Demo](images/skill-trigger-demo.gif)

*デモの出力は異なる場合があります。使用するモデル、ツール、レスポンスはここに表示されているものと異なります。*

</details>

---

## スケールでの一貫性：チーム PR レビュースキル

チームに10項目の PR チェックリストがあるとします。スキルがなければ、すべての開発者が10項目すべてを覚えている必要があり、誰かが必ず何かを忘れます。`pr-review` スキルがあれば、チーム全体で一貫したレビューが実現します：

```bash
copilot

> Can you review this PR?
```

Copilot がチームの `pr-review` スキルを自動的に読み込み、10項目すべてをチェックします：

```
PR Review: feature/user-auth

## Security ✅
- No hardcoded secrets
- Input validation present
- No bare except clauses

## Code Quality ⚠️
- [WARN] print statement on line 45 - remove before merge
- [WARN] TODO on line 78 missing issue reference
- [WARN] Missing type hints on public functions

## Testing ✅
- New tests added
- Edge cases covered

## Documentation ❌
- [FAIL] Breaking change not documented in CHANGELOG
- [FAIL] API changes need OpenAPI spec update
```

**このパワー**: チームメンバー全員が同じ基準を自動的に適用します。新入社員もチェックリストを暗記する必要はありません。スキルが代わりに処理します。

---

# カスタムスキルの作成

<img src="images/creating-managing-skills.png" alt="スキルの作成と管理を表す、人間とロボットの手が光る LEGO 風ブロックの壁を組み立てている様子" width="800"/>

SKILL.md ファイルから独自のスキルを構築します。

---

## スキルの配置場所

スキルは `.github/skills/`（プロジェクト固有）または `~/.copilot/skills/`（ユーザーレベル）に保存します。

### Copilot がスキルを見つける方法

Copilot は以下の場所を自動的にスキャンしてスキルを検出します：

| 配置場所 | スコープ |
|----------|-------|
| `.github/skills/` | プロジェクト固有（git 経由でチームと共有） |
| `~/.copilot/skills/` | ユーザー固有（個人のスキル） |

### スキルの構造

各スキルは `SKILL.md` ファイルを含む独自のフォルダに格納されます。オプションでスクリプト、サンプル、その他のリソースを含めることもできます：

```
.github/skills/
└── my-skill/
    ├── SKILL.md           # 必須: スキルの定義と指示
    ├── examples/          # オプション: Copilot が参照できるサンプルファイル
    │   └── sample.py
    └── scripts/           # オプション: スキルが使用するスクリプト
        └── validate.sh
```

> 💡 **ヒント**: ディレクトリ名は SKILL.md のフロントマターの `name` と一致させましょう（小文字でハイフン区切り）。

### SKILL.md のフォーマット

スキルは YAML フロントマター付きのシンプルな Markdown 形式を使用します：

```markdown
---
name: code-checklist
description: Comprehensive code quality checklist with security, performance, and maintainability checks
license: MIT
---

# Code Checklist

When checking code, look for:

## Security
- SQL injection vulnerabilities
- XSS vulnerabilities
- Authentication/authorization issues
- Sensitive data exposure

## Performance
- N+1 query problems (running one query per item instead of one query for all items)
- Unnecessary loops or computations
- Memory leaks
- Blocking operations

## Maintainability
- Function length (flag functions > 50 lines)
- Code duplication
- Missing error handling
- Unclear naming

## Output Format
Provide issues as a numbered list with severity:
- [CRITICAL] - Must fix before merge
- [HIGH] - Should fix before merge
- [MEDIUM] - Should address soon
- [LOW] - Nice to have
```

**YAML プロパティ：**

| プロパティ | 必須 | 説明 |
|----------|----------|-------------|
| `name` | **はい** | 一意の識別子（小文字、スペースにはハイフンを使用） |
| `description` | **はい** | スキルの機能と Copilot がいつ使うべきか |
| `license` | いいえ | このスキルに適用されるライセンス |

> 📖 **公式ドキュメント**: [About Agent Skills](https://docs.github.com/copilot/concepts/agents/about-agent-skills)

### 最初のスキルを作成する

OWASP Top 10 の脆弱性をチェックするセキュリティ監査スキルを作りましょう：

```bash
# スキルディレクトリを作成
mkdir -p .github/skills/security-audit

# SKILL.md ファイルを作成
cat > .github/skills/security-audit/SKILL.md << 'EOF'
---
name: security-audit
description: Security-focused code review checking OWASP (Open Web Application Security Project) Top 10 vulnerabilities
---

# Security Audit

Perform a security audit checking for:

## Injection Vulnerabilities
- SQL injection (string concatenation in queries)
- Command injection (unsanitized shell commands)
- LDAP injection
- XPath injection

## Authentication Issues
- Hardcoded credentials
- Weak password requirements
- Missing rate limiting
- Session management flaws

## Sensitive Data
- Plaintext passwords
- API keys in code
- Logging sensitive information
- Missing encryption

## Access Control
- Missing authorization checks
- Insecure direct object references
- Path traversal vulnerabilities

## Output
For each issue found, provide:
1. File and line number
2. Vulnerability type
3. Severity (CRITICAL/HIGH/MEDIUM/LOW)
4. Recommended fix
EOF

# スキルをテストする（スキルはプロンプトに基づいて自動的に読み込まれます）
copilot
> @samples/book-app-project/ Check this code for security vulnerabilities
# Copilot は「security vulnerabilities」がスキルに一致すると検出し、
# OWASP チェックリストを自動的に適用します
```

**期待される出力**（結果は異なる場合があります）：

```
Security Audit: book-app-project

[HIGH] Hardcoded file path (book_app.py, line 12)
  File path is hardcoded rather than configurable
  Fix: Use environment variable or config file

[MEDIUM] No input validation (book_app.py, line 34)
  User input passed directly to function without sanitization
  Fix: Add input validation before processing

✅ No SQL injection found
✅ No hardcoded credentials found
```

---

## 良いスキル説明の書き方

SKILL.md の `description` フィールドは非常に重要です！Copilot がスキルを読み込むかどうかを判断する材料になります：

```markdown
---
name: security-audit
description: Use for security reviews, vulnerability scanning,
  checking for SQL injection, XSS, authentication issues,
  OWASP Top 10 vulnerabilities, and security best practices
---
```

> 💡 **ヒント**: 普段の質問の仕方に合ったキーワードを含めましょう。「security review」と言うなら、説明に「security review」を含めてください。

### スキルとエージェントの組み合わせ

スキルとエージェントは連携して動作します。エージェントが専門知識を提供し、スキルが具体的な指示を提供します：

```bash
# code-reviewer エージェントで開始
copilot --agent code-reviewer

> Check the book app for quality issues
# code-reviewer エージェントの専門知識と
# code-checklist スキルのチェックリストが組み合わさります
```

---

# スキルの管理と共有

インストール済みスキルの確認、コミュニティスキルの発見、自分のスキルの共有方法を学びます。

<img src="images/managing-sharing-skills.png" alt="スキルの管理と共有 - CLI スキルの発見、使用、作成、共有のサイクル" width="800" />

---

## `/skills` コマンドによるスキル管理

`/skills` コマンドを使ってインストール済みスキルを管理します：

| コマンド | 機能 |
|---------|--------------|
| `/skills list` | インストール済みの全スキルを表示 |
| `/skills info <name>` | 特定のスキルの詳細を取得 |
| `/skills add <name>` | スキルを有効化（リポジトリまたはマーケットプレイスから） |
| `/skills remove <name>` | スキルを無効化またはアンインストール |
| `/skills reload` | SKILL.md ファイルの編集後にスキルを再読み込み |

> 💡 **覚えておきましょう**: プロンプトごとにスキルを「有効化」する必要はありません。インストールされると、プロンプトが説明に一致した場合にスキルは**自動的にトリガー**されます。これらのコマンドは、利用可能なスキルを管理するためのもので、使用するためのものではありません。

### 例：スキルの表示

```bash
copilot

> /skills list

Available skills:
- security-audit: Security-focused code review checking OWASP Top 10
- generate-tests: Generate comprehensive unit tests with edge cases
- code-checklist: Team code quality checklist
...

> /skills info security-audit

Skill: security-audit
Source: Project
Location: .github/skills/security-audit/SKILL.md
Description: Security-focused code review checking OWASP Top 10 vulnerabilities
```

---

<details>
<summary>実際の動作を見てみましょう！</summary>

![List Skills Demo](images/list-skills-demo.gif)

*デモの出力は異なる場合があります。使用するモデル、ツール、レスポンスはここに表示されているものと異なります。*

</details>

---

### `/skills reload` を使うタイミング

スキルの SKILL.md ファイルを作成または編集した後、Copilot を再起動せずに変更を反映するには `/skills reload` を実行します：

```bash
# スキルファイルを編集
# その後 Copilot で：
> /skills reload
Skills reloaded successfully.
```

> 💡 **知っておくと便利**: `/compact` で会話履歴を要約した後でも、スキルは引き続き有効です。コンパクト化後にリロードする必要はありません。

---

## コミュニティスキルの発見と利用

### プラグインによるスキルのインストール

> 💡 **プラグインとは？** プラグインは、スキル、エージェント、MCP サーバー設定をまとめてバンドルできるインストール可能なパッケージです。Copilot CLI の「アプリストア」の拡張機能のようなものです。

`/plugin` コマンドを使ってこれらのパッケージを閲覧・インストールできます：

```bash
copilot

> /plugin list
# インストール済みのプラグインを表示

> /plugin marketplace
# 利用可能なプラグインを閲覧

> /plugin install <plugin-name>
# マーケットプレイスからプラグインをインストール
```

プラグインは複数の機能をまとめてバンドルできます。1つのプラグインに、連携して動作する関連スキル、エージェント、MCP サーバー設定が含まれることがあります。

### コミュニティスキルリポジトリ

コミュニティリポジトリから既製のスキルも入手できます：

- **[Awesome Copilot](https://github.com/github/awesome-copilot)** - スキルのドキュメントやサンプルを含む GitHub Copilot の公式リソース

### コミュニティスキルの手動インストール

GitHub リポジトリでスキルを見つけたら、そのフォルダをスキルディレクトリにコピーします：

```bash
# awesome-copilot リポジトリをクローン
git clone https://github.com/github/awesome-copilot.git /tmp/awesome-copilot

# 特定のスキルをプロジェクトにコピー
cp -r /tmp/awesome-copilot/skills/code-checklist .github/skills/

# または全プロジェクトで個人使用する場合
cp -r /tmp/awesome-copilot/skills/code-checklist ~/.copilot/skills/
```

> ⚠️ **インストール前に確認**: プロジェクトにコピーする前に、必ずスキルの `SKILL.md` を読んでください。スキルは Copilot の動作を制御するため、悪意のあるスキルは有害なコマンドの実行やコードの予期しない変更を指示する可能性があります。

---

# 演習

<img src="../images/practice.png" alt="ハンズオン演習の準備が整った、コードが表示されたモニター、ランプ、コーヒーカップ、ヘッドフォンのある温かみのあるデスク" width="800"/>

学んだことを活かして、独自のスキルを構築・テストしましょう。

---

## ▶️ やってみよう

### さらにスキルを作成する

異なるパターンを示す2つのスキルを紹介します。上記の「最初のスキルを作成する」と同じ `mkdir` + `cat` のワークフローに従うか、スキルを適切な場所にコピー＆ペーストしてください。その他のサンプルは [.github/skills](../.github/skills) にあります。

### pytest テスト生成スキル

コードベース全体で一貫した pytest 構造を確保するスキルです：

```bash
mkdir -p .github/skills/pytest-gen

cat > .github/skills/pytest-gen/SKILL.md << 'EOF'
---
name: pytest-gen
description: Generate comprehensive pytest tests with fixtures and edge cases
---

# pytest Test Generation

Generate pytest tests that include:

## Test Structure
- Use pytest conventions (test_ prefix)
- One assertion per test when possible
- Clear test names describing expected behavior
- Use fixtures for setup/teardown

## Coverage
- Happy path scenarios
- Edge cases: None, empty strings, empty lists
- Boundary values
- Error scenarios with pytest.raises()

## Fixtures
- Use @pytest.fixture for reusable test data
- Use tmpdir/tmp_path for file operations
- Mock external dependencies with pytest-mock

## Output
Provide complete, runnable test file with proper imports.
EOF
```

### チーム PR レビュースキル

チーム全体で一貫した PR レビュー基準を強制するスキルです：

```bash
mkdir -p .github/skills/pr-review

cat > .github/skills/pr-review/SKILL.md << 'EOF'
---
name: pr-review
description: Team-standard PR review checklist
---

# PR Review

Review code changes against team standards:

## Security Checklist
- [ ] No hardcoded secrets or API keys
- [ ] Input validation on all user data
- [ ] No bare except clauses
- [ ] No sensitive data in logs

## Code Quality
- [ ] Functions under 50 lines
- [ ] No print statements in production code
- [ ] Type hints on public functions
- [ ] Context managers for file I/O
- [ ] No TODOs without issue references

## Testing
- [ ] New code has tests
- [ ] Edge cases covered
- [ ] No skipped tests without explanation

## Documentation
- [ ] API changes documented
- [ ] Breaking changes noted
- [ ] README updated if needed

## Output Format
Provide results as:
- ✅ PASS: Items that look good
- ⚠️ WARN: Items that could be improved
- ❌ FAIL: Items that must be fixed before merge
EOF
```

### さらに挑戦する

1. **スキル作成チャレンジ**: 3項目のチェックリストを行う `quick-review` スキルを作成してください：
   - 裸の except 文
   - 型ヒントの欠如
   - 不明確な変数名

   テスト方法: 「Do a quick review of books.py」と質問する

2. **スキル比較**: 詳細なセキュリティレビューのプロンプトを手動で書く時間を計ってみましょう。次に「Check for security issues in this file」と質問して security-audit スキルを自動的に読み込ませます。スキルでどのくらい時間を節約できましたか？

3. **チームスキルチャレンジ**: チームのコードレビューチェックリストについて考えてみましょう。スキルとしてエンコードできますか？スキルが常にチェックすべき3つの項目を書き出してみましょう。

**セルフチェック**: `description` フィールドがなぜ重要かを説明できれば、スキルを理解しています（Copilot がスキルを読み込むかどうかを判断する材料だからです）。

---

## 📝 課題

### メインチャレンジ：ブックサマリースキルの作成

上記の例では `pytest-gen` と `pr-review` スキルを作成しました。次は、まったく異なる種類のスキルを作成する練習をしましょう：データからフォーマットされた出力を生成するスキルです。

1. 現在のスキルを一覧表示する: Copilot を実行して `/skills list` を渡します。`ls .github/skills/` でプロジェクトスキルを、`ls ~/.copilot/skills/` で個人スキルを確認することもできます。
2. `.github/skills/book-summary/SKILL.md` に `book-summary` スキルを作成し、ブックコレクションのフォーマットされた Markdown サマリーを生成する
3. スキルに含めるべき内容：
   - 明確な名前と説明（説明はマッチングに重要！）
   - 具体的なフォーマットルール（例：タイトル、著者、年、読了ステータスを含む Markdown テーブル）
   - 出力規約（例：読了ステータスに ✅/❌ を使用、年で並べ替え）
4. スキルをテストする: `@samples/book-app-project/data.json Summarize the books in this collection`
5. `/skills list` でスキルの自動トリガーを確認する
6. `/book-summary Summarize the books in this collection` で直接呼び出しを試す

**成功基準**: ブックコレクションについて質問すると Copilot が自動的に適用する、動作する `book-summary` スキルが完成していること。

<details>
<summary>💡 ヒント（クリックで展開）</summary>

**スターターテンプレート**: `.github/skills/book-summary/SKILL.md` を作成：

```markdown
---
name: book-summary
description: Generate a formatted markdown summary of a book collection
---

# Book Summary Generator

Generate a summary of the book collection following these rules:

1. Output a markdown table with columns: Title, Author, Year, Status
2. Use ✅ for read books and ❌ for unread books
3. Sort by year (oldest first)
4. Include a total count at the bottom
5. Flag any data issues (missing authors, invalid years)

Example:
| Title | Author | Year | Status |
|-------|--------|------|--------|
| 1984 | George Orwell | 1949 | ✅ |
| Dune | Frank Herbert | 1965 | ❌ |

**Total: 2 books (1 read, 1 unread)**
```

**テスト方法：**
```bash
copilot
> @samples/book-app-project/data.json Summarize the books in this collection
# 説明のマッチに基づいてスキルが自動トリガーされるはずです
```

**トリガーされない場合:** `/skills reload` を試してからもう一度質問してください。

</details>

### ボーナスチャレンジ：コミットメッセージスキル

1. 一貫したフォーマットの Conventional Commit メッセージを生成する `commit-message` スキルを作成する
2. 変更をステージングし、「Generate a commit message for my staged changes」と質問してテストする
3. スキルをドキュメント化し、`copilot-skill` トピックを付けて GitHub で共有する

---

<details>
<summary>🔧 <strong>よくある間違いとトラブルシューティング</strong>（クリックで展開）</summary>

### よくある間違い

| 間違い | 起きること | 修正方法 |
|---------|--------------|-----|
| ファイル名を `SKILL.md` 以外にする | スキルが認識されない | ファイル名は正確に `SKILL.md` にする必要があります |
| 曖昧な `description` フィールド | スキルが自動的に読み込まれない | 説明は主要な検出メカニズムです。具体的なトリガーワードを使いましょう |
| フロントマターに `name` または `description` が欠落 | スキルの読み込みに失敗 | YAML フロントマターに両方のフィールドを追加してください |
| 間違ったフォルダの場所 | スキルが見つからない | `.github/skills/skill-name/`（プロジェクト）または `~/.copilot/skills/skill-name/`（個人）を使用 |

### トラブルシューティング

**スキルが使用されない** - 期待通りに Copilot がスキルを使用しない場合：

1. **説明を確認する**: 質問の仕方と一致していますか？
   ```markdown
   # 悪い例: 曖昧すぎる
   description: Reviews code

   # 良い例: トリガーワードを含む
   description: Use for code reviews, checking code quality,
     finding bugs, security issues, and best practice violations
   ```

2. **ファイルの場所を確認する**：
   ```bash
   # プロジェクトスキル
   ls .github/skills/

   # ユーザースキル
   ls ~/.copilot/skills/
   ```

3. **SKILL.md のフォーマットを確認する**: フロントマターは必須です：
   ```markdown
   ---
   name: skill-name
   description: What the skill does and when to use it
   ---

   # Instructions here
   ```

**スキルが表示されない** - フォルダ構造を確認してください：
```
.github/skills/
└── my-skill/           # フォルダ名
    └── SKILL.md        # 正確に SKILL.md でなければなりません（大文字小文字区別あり）
```

スキルを作成または編集した後、変更が反映されるように `/skills reload` を実行してください。

**スキルが読み込まれるかテストする** - Copilot に直接聞いてください：
```bash
> What skills do you have available for checking code quality?
# Copilot は見つけた関連スキルを説明します
```

**スキルが実際に動作しているかの確認方法**

1. **出力フォーマットを確認する**: スキルが出力フォーマットを指定している場合（`[CRITICAL]` タグなど）、レスポンスにそれが含まれているか確認する
2. **直接聞く**: レスポンスを受け取った後、「Did you use any skills for that?」と聞く
3. **有無で比較する**: `--no-custom-instructions` を使って同じプロンプトを試し、違いを確認する：
   ```bash
   # スキルあり
   copilot --allow-all -p "Review @file.py for security issues"

   # スキルなし（ベースライン比較）
   copilot --allow-all -p "Review @file.py for security issues" --no-custom-instructions
   ```
4. **特定のチェックを確認する**: スキルに特定のチェック（「50行を超える関数」など）が含まれている場合、それが出力に現れるか確認する

</details>

---

# まとめ

## 🔑 重要なポイント

1. **スキルは自動的**: プロンプトがスキルの説明に一致すると Copilot が読み込みます
2. **直接呼び出し**: `/skill-name` のスラッシュコマンドでスキルを直接呼び出すこともできます
3. **SKILL.md のフォーマット**: YAML フロントマター（name、description、オプションの license）と Markdown の指示文
4. **場所が重要**: `.github/skills/` はプロジェクト/チーム共有用、`~/.copilot/skills/` は個人用
5. **説明が鍵**: 普段の質問の仕方に合った説明を書きましょう

> 📋 **クイックリファレンス**: コマンドとショートカットの完全なリストは [GitHub Copilot CLI コマンドリファレンス](https://docs.github.com/en/copilot/reference/cli-command-reference) をご覧ください。

---

## ➡️ 次のステップ

スキルは自動読み込みされる指示で Copilot の機能を拡張します。しかし、外部サービスへの接続はどうでしょうか？そこで MCP の出番です。

**[Chapter 06: MCP サーバー](../06-mcp-servers/README.ja.md)** では、以下を学びます：

- MCP（Model Context Protocol）とは何か
- GitHub、ファイルシステム、ドキュメントサービスへの接続
- MCP サーバーの設定
- マルチサーバーワークフロー

---

**[← Chapter 04 に戻る](../04-agents-custom-instructions/README.ja.md)** | **[Chapter 06 に進む →](../06-mcp-servers/README.ja.md)**
