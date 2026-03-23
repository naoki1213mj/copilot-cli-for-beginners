![GitHub Copilot CLI for Beginners](./images/copilot-banner.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)&ensp;
[![Open project in GitHub Codespaces](https://img.shields.io/badge/Codespaces-Open-blue?style=flat-square&logo=github)](https://codespaces.new/github/copilot-cli-for-beginners?hide_repo_select=true&ref=main&quickstart=true)&ensp;
[![Official Copilot CLI documentation](https://img.shields.io/badge/GitHub-CLI_Documentation-00a3ee?style=flat-square&logo=github)](https://docs.github.com/en/copilot/how-tos/copilot-cli)&ensp;
[![Join AI Foundry Discord](https://img.shields.io/badge/Discord-AI_Community-blue?style=flat-square&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

🎯 [学習内容](#学習内容) &ensp; ✅ [前提条件](#前提条件) &ensp; 🤖 [Copilotファミリー](#github-copilotファミリーを理解する) &ensp; 📚 [コース構成](#コース構成) &ensp; 📋 [コマンドリファレンス](#-github-copilot-cliコマンドリファレンス)

# GitHub Copilot CLI for Beginners

> **✨ AI搭載のコマンドライン支援で開発ワークフローを加速させましょう。**

GitHub Copilot CLIは、AIアシスタンスをターミナルに直接もたらします。ブラウザやコードエディタに切り替えることなく、質問したり、フル機能のアプリケーションを生成したり、コードをレビューしたり、テストを生成したり、問題をデバッグしたりすることができます。

コードを読んで、わかりにくいパターンを説明し、より速く作業する手助けをしてくれる、知識豊富な同僚が24時間365日利用できると考えてください！

このコースは以下の方を対象としています：

- コマンドラインからAIを使いたい**ソフトウェア開発者**
- IDE統合よりもキーボード駆動のワークフローを好む**ターミナルユーザー**
- AI支援のコードレビューと開発プラクティスを標準化したい**チーム**

<a href="https://aka.ms/githubcopilotdevdays" target="_blank">
  <picture>
    <img src="./images/copilot-dev-days.png" alt="GitHub Copilot Dev Days - Find or host an event" width="100%" />
  </picture>
</a>

## 🎯 学習内容

このハンズオンコースでは、GitHub Copilot CLIをゼロから生産的に使えるようになるまで学びます。全チャプターを通じて1つのPython書籍コレクションアプリを使い、AI支援ワークフローを使って段階的に改善していきます。コース終了時には、ターミナルからコードのレビュー、テストの生成、問題のデバッグ、ワークフローの自動化を自信を持って行えるようになります。

**AIの経験は不要です。** ターミナルが使えれば、これを学ぶことができます。

**最適な対象者：** 開発者、学生、ソフトウェア開発の経験がある方。

## ✅ 前提条件

始める前に、以下を確認してください：

- **GitHubアカウント**：[無料で作成](https://github.com/signup)<br>
- **GitHub Copilotアクセス**：[無料プラン](https://github.com/features/copilot/plans)、[月額サブスクリプション](https://github.com/features/copilot/plans)、または[学生・教師向け無料](https://education.github.com/pack)<br>
- **ターミナルの基本操作**：`cd`、`ls`、コマンドの実行に慣れていること

## 🤖 GitHub Copilotファミリーを理解する

GitHub Copilotは、AI搭載ツールのファミリーに進化しました。各ツールの位置づけは以下の通りです：

| 製品 | 実行環境 | 説明 |
|------|----------|------|
| [**GitHub Copilot CLI**](https://docs.github.com/copilot/how-tos/copilot-cli/cli-getting-started)<br>(このコース) | ターミナル | ターミナルネイティブのAIコーディングアシスタント |
| [**GitHub Copilot**](https://docs.github.com/copilot) | VS Code、Visual Studio、JetBrainsなど | エージェントモード、チャット、インライン提案 |
| [**Copilot on GitHub.com**](https://github.com/copilot) | GitHub | リポジトリについての没入型チャット、エージェント作成など |
| [**GitHub Copilot coding agent**](https://docs.github.com/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks) | GitHub | イシューをエージェントに割り当て、PRを受け取る |

このコースは**GitHub Copilot CLI**に焦点を当て、AIアシスタンスをターミナルに直接もたらします。

## 📚 コース構成

![GitHub Copilot CLI Learning Path](images/learning-path.png)

| チャプター | タイトル | 作成するもの |
|:----------:|----------|-------------|
| 00 | 🚀 [クイックスタート](./00-quick-start/README.ja.md) | インストールと動作確認 |
| 01 | 👋 [最初のステップ](./01-setup-and-first-steps/README.ja.md) | ライブデモ + 3つのインタラクションモード |
| 02 | 🔍 [コンテキストと会話](./02-context-conversations/README.ja.md) | マルチファイルプロジェクト分析 |
| 03 | ⚡ [開発ワークフロー](./03-development-workflows/README.ja.md) | コードレビュー、デバッグ、テスト生成 |
| 04 | 🤖 [専門AIアシスタントの作成](./04-agents-custom-instructions/README.ja.md) | ワークフロー用カスタムエージェント |
| 05 | 🛠️ [繰り返し作業の自動化](./05-skills/README.ja.md) | 自動読み込みされるスキル |
| 06 | 🔌 [GitHub、データベース、APIへの接続](./06-mcp-servers/README.ja.md) | MCPサーバー統合 |
| 07 | 🎯 [すべてをまとめる](./07-putting-it-together/README.ja.md) | 完全な機能ワークフロー |

## 📖 このコースの使い方

各チャプターは同じパターンに従います：

1. **実世界のアナロジー**：身近な比較を通じてコンセプトを理解する
2. **コアコンセプト**：必要な知識を学ぶ
3. **ハンズオン例**：実際のコマンドを実行して結果を確認する
4. **課題**：学んだことを実践する
5. **次のステップ**：次のチャプターのプレビュー

**コード例は実行可能です。** このコースのすべてのcopilotテキストブロックは、ターミナルにコピーして実行できます。

## 📋 GitHub Copilot CLIコマンドリファレンス

**[GitHub Copilot CLIコマンドリファレンス](https://docs.github.com/en/copilot/reference/cli-command-reference)** は、Copilot CLIを効果的に使用するためのコマンドとキーボードショートカットを見つけるのに役立ちます。

## 🙋 ヘルプ

- 🐛 **バグを見つけましたか？** [Issueを作成](https://github.com/github/copilot-cli-for-beginners/issues)
- 🤝 **貢献しませんか？** PRを歓迎します！
- 📚 **公式ドキュメント：** [GitHub Copilot CLIドキュメント](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)

## ライセンス

このプロジェクトはMITオープンソースライセンスの条件に基づいてライセンスされています。全文は[LICENSE](./LICENSE)ファイルを参照してください。
