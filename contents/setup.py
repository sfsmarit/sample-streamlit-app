import streamlit as st
from PIL import Image


st.set_page_config(page_title="環境構築")
st.title("環境構築")


st.subheader("開発環境", divider=True)
st.image(Image.open("data/development_environment.png"))
st.markdown(
    """
    開発環境は主に次の3つで構成されます。

    - ローカル環境
      自分の PC でアプリを作成・テストする場所です。ここでコードを書き、動作確認を行います。
      Streamlit をインストールし、ブラウザでアプリを確認できるようにします。

    - GitHub
      コードを安全に管理・共有するためのサービスです。
      バージョン管理ができるので、誰がどの変更をしたか追跡できます。
      また、後で Web サーバに公開する際にも GitHub のリポジトリを利用します。

    - Web サーバ
      作成したアプリを公開するための環境です。
      機密情報を扱う場合はイントラネット上のサーバ、そうでなければ Streamlit Community Cloud を使うとよいです。

    #### 環境構築の流れ
    1. ローカル環境を準備
       Python と Streamlit をインストールし、アプリを開発できる状態にします。
       統合開発環境として Visual Studio Code を使用します。
    2. GitHub でコード管理
       GitHub のアカウントを作成し、リポジトリを作成後、コードを GitHub にアップロードします。
    3. Webサーバで公開
       完成したアプリを社内サーバやクラウドにデプロイして利用できるようにします。
    """
)


st.subheader("ローカル環境の構築", divider=True)
st.markdown(
    """
    #### Visual Studio Code のインストール (初回のみ)
    Visual Studio Code (VS Code) とは、Microsoft が提供する無料のコードエディタです。
    軽量でありながら拡張機能が豊富で、Python の開発に広く利用されています。

    **インストール手順**  
    1. **下記リンクから VS Code をダウンロードしてインストール**
    https://azure.microsoft.com/ja-jp/products/visual-studio-code

    2. **VS Code を起動して、次の拡張機能を追加**
    - **Japanese Language Pack for Visual Studio Code** (日本語表示)
    - **Python**
    - **Pylance** (コード補完と型チェック)
    - **autopep8** (コード自動整形)
    """
)
st.image(Image.open("data/vscode_extention.png"),
         caption="VS Code 拡張機能")

st.markdown(
    """
    #### Streamlit のインストール (初回のみ)
    Streamlit は Python のデフォルトにはインストールされていないため、pip コマンドでインストールする必要があります。

    1. **VSCode のターミナルを起動**
    """
)

st.image(Image.open("data/vscode_terminal.png"),
         caption="VS Code 拡張機能")

st.markdown(
    """
    2. **ターミナルに次のコマンドを入力**
    ```sh
    pip install streamlit
    ```
    """
)


st.markdown(
    """
    #### プロジェクトの作成
    アプリケーションごとのコードやデータファイルの集合をプロジェクトと呼びます。
    Streamlit でアプリを作る場合、ひとつのプロジェクトがひとつのアプリに対応します。

    1. **プロジェクトフォルダの作成**  
    ここでは例として、フォルダ名を`sample-app`とします。
    プロジェクト名が複数単語からなる場合、GitHub の慣用表現にならって、_(アンダースコア) ではなく -(ハイフン) で繋ぎます。

    2. **VS Code でプロジェクトを開く**  
    『ファイル > フォルダーを開く』で`sample-app`フォルダを指定します。
    すると、プロジェクト全体が VS Code の管理下に置かれ、エクスプローラにファイルやフォルダが表示されます。

    3. **アプリの作成**  
    アプリ本体となる Python スクリプト `main.py` を作ります。
    """
)
st.image(Image.open("data/create_script.png"),
         caption="スクリプトの作成",)

st.markdown(
    """
    `main.py`に以下を記述します。
    ```python
    import streamlit as st

    if st.button("Say Hello"):
        st.write("Hello!")
    ```    

    4. **アプリの起動**  
    VS Code のターミナルに次のコマンドを入力します。
    ```sh
    streamlit run main.py
    ```
    ブラウザに 'Say Hello' と書かれたボタンが表示されたら成功です。

    5. **アプリの終了**  
    ターミナル上で Ctrl + C を押すと強制終了します。

    以上が、プロジェクトを作成してアプリを起動するまでの基本的な手順です。

    #### 開発の効率化
    1. **autopep8 の有効化**  
    PEP8 とは、Python コードの可読性を高めるための公式スタイルガイドです。  
    インデント、空白、行の長さ、命名規則などの基本的なルールを定義しています。  
    autopep8 を有効にすると、PEP8 に準拠するようにコードが自動でフォーマットされます。

    **設定手順**  
    プロジェクトフォルダの直下に`.vscode`フォルダを作成します。  
    その下に`settings.json`ファイルを作成し、以下を記述します。
    ```json
    {
        "[python]": {
            "editor.defaultFormatter": "ms-python.autopep8",
            "editor.formatOnSave": true,
        },
        "autopep8.args": [
            "--max-line-length=120"
        ]
    }
    ```
    `--max-line-length=120`で一行の文字数を定義しています。PEP8 は 79 文字を推奨していますが、長すぎなければ自由に決めてよいです。

    2. F5 キーでアプリを起動する

    """
)
