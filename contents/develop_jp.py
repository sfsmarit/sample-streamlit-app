import streamlit as st

nl = "  "

st.set_page_config(page_title="開発のコツ")
st.title("開発のコツ")


st.subheader("いきなり UI を作らない", divider=True)
st.markdown(
    """
    ツールとして配布するアプリは、計算やデータ処理のロジックが本質です。
    **最初にロジックのコードを完成させ、その後にデータの入出力を行う UI を実装する**とよいです。

    UIから着手すると、次のような問題が起きます。
    - 実行に時間がかかる
    - ロジック・UI・イベント管理の 3 重デバッグ

    ただし、**UIが主目的のアプリ**では、
    最初にハリボテの UI を作っておくと関係者への説明に便利です。
    """
)

st.subheader("プロジェクトの管理", divider=True)
st.markdown(
    f"""
    ##### .gitignore でファイルを非公開にする
    機密情報を含むファイルや、開発環境と本番環境で分離したいファイルは **`.gitignore`** を使って Git 管理から除外します。
    
    1. プロジェクトフォルダ直下に `.gitignore` ファイルを作成
    2. 除外したいファイルやフォルダを記述
    ```
    .env
    .streamlit/secrets.toml
    __pycache__
    *.pptx
    !not_ignored.pptx
    ```

    ---

    ##### .env で環境を切り替える
    開発環境と本番環境で設定を切り替える場合、`.env`ファイルを使うと便利です。
    
    1. プロジェクト直下に `.env` ファイルを作成
    2. 環境変数を記述

    ```bash
    # 開発環境の .env
    DEBUG=True
    DB_HOST=localhost
    DB_USER=dev_user
    ```
    ```bash
    # 本番環境の .env
    DEBUG=False
    DB_HOST=prod-db.example.com
    DB_USER=prod_user
    ```
    
    3. Python で読み込むには`python-dotenv`を利用します。
    ```bash
    pip install python-dotenv
    ```
    ```python
    from dotenv import load_dotenv
    import os

    load_dotenv()  # .envを読み込む
    db_host = os.getenv("DB_HOST")
    debug_mode = os.getenv("DEBUG") == "True"
    ```

    ---
    
    ##### ブランチを分ける
    複数人での開発や、機能の追加／修正を安全に進めたい場合は、Git のブランチ戦略を使いましょう。
    > ブランチとは、Gitにおける「作業の分岐」であり、ひとつのリポジトリで複数の開発を同時に進めるための仕組みです。{nl}
    > 分岐したブランチの変更は他のブランチにマージすることができます。

    小規模開発におけるブランチ戦略の例
    |ブランチ名|役割|
    |---|---|
    |main|本番用|
    |develop|開発用|

    ブランチの作成
    ```bash
    # develop ブランチを作成して切り替える
    git checkout -b develop
    ```
    
    `main`と`develop`で Web ページを分ける
    ```bash
    # main
    git clone <repository_url>
    # develop
    git clone -b develop <repository_url>
    # データの更新方法は同じ
    git pull
    ```
    
    **ブランチ開発の流れ**{nl}
    `git`コマンドで説明しますが、VS Code の UI でも同じことができます。
    1. `develop`で開発
    ```bash
    git checkout develop
    # --- コード修正完了 ---
    git add .
    git commit -m "新機能の追加"
    git push origin develop
    ```
    2. `develop`の状態が安定したら`main`にマージ
    ```bash
    git checkout main
    git merge --no-ff develop
    git push origin main
    ```
    X. 緊急修正は`main`で直接行い、その後`develop`に取り込む
    ```bash
    git checkout main
    git pull
    # --- コード修正完了 ---
    git add .
    git commit -m "緊急対応: 認証バグ修正"
    git push origin main

    # develop に反映
    git checkout develop
    git merge --no-ff main
    git push origin develop
    ```
    """

)

st.subheader("コード量が増えてきたら", divider=True)
st.markdown(
    """
    """
)

st.subheader("Streamlit の独特な仕様", divider=True)
st.markdown(
    """
    """
)

st.subheader("UI", divider=True)
st.markdown(
    """
    """
)

st.subheader("マルチページを使う", divider=True)
st.markdown(
    """
    """
)

st.subheader("重い処理の対策", divider=True)
st.markdown(
    """
    """
)

st.subheader("データベースを活用する", divider=True)
st.markdown(
    """
    """
)

st.subheader("ログと監視", divider=True)
st.markdown(
    """
    """
)
