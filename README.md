# STREAMLITRY

## 環境構築

### グローバルインストール

```sh
brew install mise direnv uv
```

### python

```sh
mise use -g python@3.12.3
```

### 仮想環境

```sh
uv venv
```

### direnv　有効化

```sh
direnv allow
```

mise を使えば direnv はいらないかも…

### fabric

```sh
uv pip install fabric
```

fabric だけ pip install が必要なのをどうにかしたい。 fabric から mise の tasks に移行したいが、 tasks に arg を渡す方法がわからず、移行を保留した。

### パッケージインストール

```sh
fab sync
```
