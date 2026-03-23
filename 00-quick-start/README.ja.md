![Chapter 00: Quick Start](images/chapter-header.png)

ようこそ！この章では、GitHub Copilot CLI（コマンドラインインターフェース）をインストールし、GitHub アカウントでサインインして、すべてが正しく動作することを確認します。これはクイックセットアップの章です。セットアップが完了したら、Chapter 01 から本格的なデモが始まります！

## 🎯 学習目標

この章を終えると、以下のことが完了しています：

- GitHub Copilot CLI のインストール
- GitHub アカウントでのサインイン
- 簡単なテストによる動作確認

> ⏱️ **所要時間の目安**: 約10分（読む時間5分 + ハンズオン5分）

---

## ✅ 前提条件

- Copilot にアクセスできる **GitHub アカウント**。[サブスクリプションオプションを確認](https://github.com/features/copilot/plans)。学生・教職員は [GitHub Education](https://education.github.com/pack) を通じて Copilot Pro を無料で利用できます。
- **ターミナルの基本操作**: `cd` や `ls` などのコマンドに慣れていること

### 「Copilot アクセス」とは

GitHub Copilot CLI を使用するには、有効な Copilot サブスクリプションが必要です。[github.com/settings/copilot](https://github.com/settings/copilot) でステータスを確認できます。以下のいずれかが表示されるはずです：

- **Copilot Individual** - 個人サブスクリプション
- **Copilot Business** - 組織を通じて提供
- **Copilot Enterprise** - エンタープライズを通じて提供
- **GitHub Education** - 認証済みの学生・教職員は無料

「You don't have access to GitHub Copilot」と表示される場合は、無料オプションを利用するか、プランに加入するか、アクセスを提供している組織に参加する必要があります。

---

## インストール

> ⏱️ **所要時間の目安**: インストールに2〜5分。認証にさらに1〜2分かかります。

### 推奨: GitHub Codespaces（セットアップ不要）

前提条件をインストールしたくない場合は、GitHub Codespaces を使用できます。GitHub Copilot CLI がすぐに使える状態で（サインインは必要です）、Python 3.13、pytest、GitHub CLI がプリインストールされています。

1. [このリポジトリをフォーク](https://github.com/github/copilot-cli-for-beginners/fork)して自分の GitHub アカウントに追加
2. **Code** > **Codespaces** > **Create codespace on main** を選択
3. コンテナのビルドが完了するまで数分待つ
4. 準備完了！Codespace 環境でターミナルが自動的に開きます。

> 💡 **Codespace での確認**: `cd samples/book-app-project && python book_app.py help` を実行して、Python とサンプルアプリが動作することを確認してください。

### 代替手段: ローカルインストール

> 💡 **どれを選べばいい？** Node.js がインストールされている場合は `npm` を使ってください。それ以外の場合は、お使いのシステムに合ったオプションを選択してください。

> 💡 **デモには Python が必要です**: このコースでは Python のサンプルアプリを使用します。ローカルで作業する場合は、デモを始める前に [Python 3.10+](https://www.python.org/downloads/) をインストールしてください。

> **注意:** コース全体で示される主なサンプルは Python（`samples/book-app-project`）を使用していますが、JavaScript（`samples/book-app-project-js`）や C#（`samples/book-app-project-cs`）版も用意されています。他の言語で作業したい場合はそちらをご利用ください。各サンプルには、その言語でアプリを実行するための手順が記載された README があります。

お使いのシステムに合った方法を選択してください：

### 全プラットフォーム共通（npm）

```bash
# Node.js がインストールされている場合、CLI を素早く導入できます
npm install -g @github/copilot
```

### macOS/Linux（Homebrew）

```bash
brew install copilot-cli
```

### Windows（WinGet）

```bash
winget install GitHub.Copilot
```

### macOS/Linux（インストールスクリプト）

```bash
curl -fsSL https://gh.io/copilot-install | bash
```

---

## 認証

ターミナルウィンドウを `copilot-cli-for-beginners` リポジトリのルートで開き、CLI を起動してフォルダへのアクセスを許可します。

```bash
copilot
```

リポジトリを含むフォルダを信頼するかどうかを尋ねられます（まだ信頼していない場合）。1回のみ信頼するか、今後のすべてのセッションで信頼するかを選択できます。

<img src="images/copilot-trust.png" alt="Copilot CLI でフォルダ内のファイルを信頼する" width="800"/>

フォルダを信頼した後、GitHub アカウントでサインインできます。

```
> /login
```

**次に起こること:**

1. Copilot CLI がワンタイムコード（例: `ABCD-1234`）を表示します
2. ブラウザが GitHub のデバイス認証ページを開きます。まだサインインしていない場合は GitHub にサインインしてください。
3. 指示に従ってコードを入力します
4. 「Authorize」を選択して GitHub Copilot CLI にアクセスを許可します
5. ターミナルに戻ります - サインイン完了です！

<img src="images/auth-device-flow.png" alt="デバイス認証フロー - ターミナルでのログインからサインイン確認までの5ステップのプロセス" width="800"/>

*デバイス認証フロー: ターミナルでコードが生成され、ブラウザで確認し、Copilot CLI が認証されます。*

**ヒント**: サインインはセッション間で保持されます。トークンが期限切れになるか、明示的にサインアウトしない限り、この操作は1回だけで済みます。

---

## 動作確認

### ステップ 1: Copilot CLI のテスト

サインインが完了したら、Copilot CLI が正しく動作することを確認しましょう。ターミナルで、まだ起動していない場合は CLI を起動してください：

```bash
> Say hello and tell me what you can help with
```

応答を受け取ったら、CLI を終了できます：

```bash
> /exit
```

---

<details>
<summary>🎬 実際の動作を見てみましょう！</summary>

![Hello Demo](images/hello-demo.gif)

*デモの出力は異なります。使用するモデル、ツール、応答はここに示されているものとは異なる場合があります。*

</details>

---

**期待される出力**: Copilot CLI の機能を一覧表示するフレンドリーな応答。

### ステップ 2: サンプルのブックアプリを実行する

このコースでは、CLI を使ってコース全体で探索・改善するサンプルアプリが用意されています（コードは */samples/book-app-project* にあります）。始める前に、*Python のブックコレクションターミナルアプリ*が動作することを確認してください。お使いのシステムに応じて `python` または `python3` を実行してください。

> **注意:** コース全体で示される主なサンプルは Python（`samples/book-app-project`）を使用していますが、JavaScript（`samples/book-app-project-js`）や C#（`samples/book-app-project-cs`）版も用意されています。他の言語で作業したい場合はそちらをご利用ください。各サンプルには、その言語でアプリを実行するための手順が記載された README があります。

```bash
cd samples/book-app-project
python book_app.py list
```

**期待される出力**: 「The Hobbit」、「1984」、「Dune」を含む5冊の本のリスト。

### ステップ 3: ブックアプリで Copilot CLI を試す

まずリポジトリのルートに戻ってください（ステップ 2 を実行した場合）：

```bash
cd ../..   # 必要に応じてリポジトリのルートに戻る
copilot 
> What does @samples/book-app-project/book_app.py do?
```

**期待される出力**: ブックアプリの主な関数とコマンドの概要。

エラーが表示された場合は、下の[トラブルシューティングセクション](#トラブルシューティング)を確認してください。

確認が終わったら Copilot CLI を終了できます：

```bash
> /exit
```

---

## ✅ 準備完了！

インストールはこれで完了です。本格的な学習は Chapter 01 から始まります：

- AI がブックアプリをレビューし、コード品質の問題を瞬時に発見する様子を確認
- Copilot CLI の3つの使い方を学習
- 自然な英語から動作するコードを生成

**[Chapter 01: はじめの一歩へ進む →](../01-setup-and-first-steps/README.ja.md)**

---

## トラブルシューティング

### 「copilot: command not found」

CLI がインストールされていません。別のインストール方法を試してください：

```bash
# brew が失敗した場合は npm を試してください:
npm install -g @github/copilot

# またはインストールスクリプト:
curl -fsSL https://gh.io/copilot-install | bash
```

### 「You don't have access to GitHub Copilot」

1. [github.com/settings/copilot](https://github.com/settings/copilot) で Copilot のサブスクリプションがあることを確認してください
2. 職場のアカウントを使用している場合は、組織が CLI アクセスを許可しているか確認してください

### 「Authentication failed」

再認証してください：

```bash
copilot
> /login
```

### ブラウザが自動的に開かない

[github.com/login/device](https://github.com/login/device) に手動でアクセスし、ターミナルに表示されたコードを入力してください。

### トークンの期限切れ

再度 `/login` を実行してください：

```bash
copilot
> /login
```

### それでも解決しない場合

- [GitHub Copilot CLI ドキュメント](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)を確認してください
- [GitHub Issues](https://github.com/github/copilot-cli/issues) で検索してください

---

## 🔑 重要なポイント

1. **GitHub Codespace ですぐに始められます** - Python、pytest、GitHub Copilot CLI がすべてプリインストールされているので、すぐにデモに取り組めます
2. **複数のインストール方法** - お使いのシステムに合った方法を選択（Homebrew、WinGet、npm、インストールスクリプト）
3. **一度きりの認証** - トークンが期限切れになるまでログインが保持されます
4. **ブックアプリが動作します** - コース全体を通して `samples/book-app-project` を使用します

> 📚 **公式ドキュメント**: インストールオプションと要件については [Copilot CLI のインストール](https://docs.github.com/copilot/how-tos/copilot-cli/cli-getting-started)を参照してください。

> 📋 **クイックリファレンス**: コマンドとショートカットの完全なリストは [GitHub Copilot CLI コマンドリファレンス](https://docs.github.com/en/copilot/reference/cli-command-reference)を参照してください。

---

**[Chapter 01: はじめの一歩へ進む →](../01-setup-and-first-steps/README.ja.md)**
