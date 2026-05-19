# Universal Python Boilerplate

`Docker (Dev Containers)` と `uv` を採用した、OSに依存しない高速なPython開発環境テンプレートです。

## 開発の始め方

### 1. 前提条件
ホストマシンに以下がインストールされている必要があります。
- Docker Desktop（または独自のDocker環境）
- VS Code または Cursor
- VS Code 拡張機能: `Dev Containers`

### 2. コンテナの起動
1. 本リポジトリを VS Code / Cursor で開きます。
2. 画面右下に表示される「コンテナで開く (Reopen in Container)」をクリックします。
3. 自動的に Docker イメージのビルドと `uv sync`（パッケージインストール）が走ります。

### 3. 用途に応じた環境の切り替え
コンテナ内のターミナルで以下のタスクを実行することで、用途別のパッケージが追加同期されます。

- **Webアプリ開発の場合:** `uv run task sync-web`
- **データ分析・機械学習の場合:** `uv run task sync-data`

## 主要コマンド（タスクランナー）

すべてコンテナ内のターミナルで実行します。

- **コードの自動修正 (Lint/Format):** `uv run task lint` / `uv run task format`
- **テストの実行:** `uv run task test`