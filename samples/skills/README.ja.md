# サンプルスキル

GitHub Copilot CLI用のすぐに使えるスキルテンプレート。任意のスキルフォルダをコピーしてすぐに使い始められます。

## クイックスタート

```bash
# スキルを個人のスキルフォルダにコピー
cp -r hello-world ~/.copilot/skills/

# またはチーム共有用にプロジェクトにコピー
cp -r code-checklist .github/skills/
```

## 利用可能なスキル

| スキル | 説明 | 最適な用途 |
|--------|------|-----------|
| `hello-world` | 最小限の例（フォーマットの学習） | 初めてのスキル作成者 |
| `code-checklist` | Pythonコード品質チェックリスト（PEP 8、型ヒント、バリデーション） | 一貫した品質チェック |
| `pytest-gen` | 包括的なpytestテスト生成 | 構造化されたテスト生成 |
| `commit-message` | Conventional Commitメッセージ | 標準化されたgit履歴 |

## スキルの仕組み

スキルは、プロンプトがスキルの`description`フィールドと一致したときに**自動的にトリガー**されます。手動で呼び出す必要はありません。

```bash
copilot

> Check this code for quality issues
# Copilotがこれが"code-checklist"スキルに一致することを検出し、自動的に読み込む

> Generate a commit message
# Copilotが"commit-message"スキルを読み込む
```

スキルを直接呼び出すこともできます：
```bash
> /code-checklist Check books.py
> /pytest-gen Generate tests for BookCollection
> /commit-message
```

## スキルの構造

各スキルは`SKILL.md`ファイルを含むフォルダです：

```
skill-name/
└── SKILL.md    # 必須：フロントマター + 手順を含む
```

`SKILL.md`ファイルには`name`と`description`（両方必須）のYAMLフロントマターがあります：

```markdown
---
name: my-skill
description: What this skill does and when to use it
---

# Skill Instructions

Your instructions here...
```

## その他のスキルを見つける

- **[github/awesome-copilot](https://github.com/github/awesome-copilot)** - コミュニティスキルを含むGitHub公式リソース
- **`/plugin marketplace`** - Copilot CLI内からスキルを閲覧・インストール

## 独自のスキル作成

1. フォルダを作成：`mkdir ~/.copilot/skills/my-skill`
2. フロントマター付きの`SKILL.md`を作成
3. 手順を追加
4. descriptionに一致する質問をCopilotに聞いてテスト

詳細なガイダンスは[チャプター05：スキル](../../05-skills/README.ja.md)を参照してください。
