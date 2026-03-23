# サンプルエージェント定義

このフォルダには、エージェントの使用を開始するのに役立つ、GitHub Copilot CLI用のシンプルなエージェントテンプレートが含まれています。

## クイックスタート

```bash
# エージェントを個人のエージェントフォルダにコピー
cp hello-world.agent.md ~/.copilot/agents/

# またはチーム共有用にプロジェクトにコピー
cp python-reviewer.agent.md .github/agents/
```

## このフォルダのサンプルファイル

| ファイル | 説明 | 最適な用途 |
|---------|------|-----------|
| `hello-world.agent.md` | 最小限の例（11行） | フォーマットの学習 |
| `python-reviewer.agent.md` | Pythonコード品質レビュアー | コードレビュー、PEP 8、型ヒント |
| `pytest-helper.agent.md` | Pytestテスト専門家 | テスト生成、フィクスチャ、エッジケース |

## その他のエージェントを見つける

- **[github/awesome-copilot](https://github.com/github/awesome-copilot)** - コミュニティエージェントと手順を含むGitHub公式リソース

---

## エージェントファイルのフォーマット

各エージェントファイルには、少なくとも`description`フィールドを持つYAMLフロントマターが必要です：

```markdown
---
name: my-agent
description: Brief description of what this agent does
tools: ["read", "edit", "search"]  # オプション：利用可能なツールを制限
---

# Agent Name

Agent instructions go here...
```

**利用可能なYAMLプロパティ：**

| プロパティ | 必須 | 説明 |
|-----------|------|------|
| `description` | **はい** | エージェントの機能 |
| `name` | いいえ | 表示名（デフォルトはファイル名） |
| `tools` | いいえ | 許可されたツールのリスト（省略 = すべて）。以下のエイリアスを参照。 |
| `target` | いいえ | `vscode`または`github-copilot`のみに制限 |

**ツールエイリアス**: `read`、`edit`、`search`、`execute`（シェル）、`web`、`agent`

> 💡 **注意**: `model`プロパティはVS Codeでは動作しますが、Copilot CLIではまだサポートされていません。
>
> 📖 **公式ドキュメント**: [カスタムエージェント設定](https://docs.github.com/copilot/reference/custom-agents-configuration)

## エージェントファイルの配置場所

エージェントは以下の場所に保存できます：
- `~/.copilot/agents/` - すべてのプロジェクトで利用可能なグローバルエージェント
- `.github/agents/` - プロジェクト固有のエージェント
- `.agent.md`ファイル - VS Code互換フォーマット

各エージェントは`.agent.md`拡張子の個別ファイルです。

---

## 使用例

```bash
# 特定のエージェントで開始
copilot --agent python-reviewer

# またはセッション中にインタラクティブにエージェントを選択
copilot
> /agent
# リストから"python-reviewer"を選択

# エージェントの専門知識がプロンプトに適用される
> @samples/book-app-project/books.py Review this code for quality issues

# 別のエージェントに切り替え
> /agent
# "pytest-helper"を選択

> @samples/book-app-project/tests/test_books.py What additional tests should we add?
```

---

## 独自のエージェント作成

1. `~/.copilot/agents/`に`.agent.md`拡張子の新しいファイルを作成
2. 少なくとも`description`フィールドを持つYAMLフロントマターを追加
3. 説明的なヘッダーを追加（例：`# Security Agent`）
4. エージェントの専門分野、基準、動作を定義
5. `/agent`または`--agent <name>`でエージェントを使用

**効果的なエージェントのためのヒント：**
- 専門分野を具体的に
- コード基準とパターンを含める
- エージェントがチェックする内容を定義
- 出力フォーマットの好みを含める
