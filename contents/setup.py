import streamlit as st
from PIL import Image


st.set_page_config(page_title="環境構築")
st.title("環境構築")

st.markdown(
    """
    このページでは、Streamlit の開発環境をゼロから構築する手順について説明します。
    """
)

st.subheader("開発環境", divider=True)
st.image(Image.open("data/development_environment.png"))
st.markdown(
    """
    開発環境は主に次の3つで構成されます。

    - **ローカル環境**\n
    アプリを作成する場所です。通常は自分の PC でコードを書き、動作確認を行います。
    Streamlit をインストールし、ブラウザでアプリを確認できるようにします。
    統合開発環境として Visual Studio Code を使用します。

    - **GitHub**\n
    コードを安全に管理・共有するためのサービスです。
    コードのバージョンを管理し、誰がどの変更をしたか追跡できます。
    また、後で Web サーバに公開する際にも GitHub のリポジトリを使います。
    GitHub を利用するにはアカウント登録が必要です。

    - **Web サーバ**\n
    作成したアプリを公開するための環境です。
    機密情報を扱う場合は社内サーバを、そうでなければ Streamlit Community Cloud を使うとよいです。

    次に、これらの環境を上から順に構築していきます。
    """
)


st.subheader("ローカル環境の構築", divider=True)
st.markdown(
    """
    #### Visual Studio Code のインストール (初回のみ)
    Visual Studio Code (VS Code) とは、Microsoft が提供する無料のコードエディタです。
    軽量でありながら拡張機能が豊富で、Python の開発に広く利用されています。

    **インストール手順**
    1. **ダウンロードしてインストールする**\n
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
    ---

    #### Streamlit のインストール (初回のみ)
    Streamlit はデフォルトでは Python にインストールされていないため、pip コマンドでインストールする必要があります。

    1. **VSCode のターミナルを起動**
    """
)

st.image(Image.open("data/vscode_terminal.png"),
         caption="VS Code 拡張機能")

st.markdown(
    """
    2. **ターミナルに次のコマンドを入力**
    ```bash
    pip install streamlit
    ```
    """
)


st.markdown(
    """
    ---

    #### プロジェクトの作成
    アプリケーションごとのコードやデータファイルの集合をプロジェクトと呼びます。
    Streamlit でアプリを作る場合、ひとつのプロジェクトがひとつのアプリに対応します。

    1. **プロジェクトフォルダの作成**\n
    ここでは例として、フォルダ名を`sample-app`とします。
    プロジェクト名が複数単語からなる場合、GitHub の慣用表現にならって、_(アンダースコア) ではなく -(ハイフン) で繋ぎます。

    2. **VS Code でプロジェクトを開く**\n
    『ファイル > フォルダーを開く』で`sample-app`フォルダを指定します。
    すると、プロジェクト全体が VS Code の管理下に置かれ、エクスプローラにファイルやフォルダが表示されます。

    3. **アプリの作成**\n
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

    4. **アプリの起動**\n
    VS Code のターミナルに次のコマンドを入力します。
    ```bash
    streamlit run main.py
    ```
    ブラウザに 'Say Hello' と書かれたボタンが表示されたら成功です。

    5. **アプリの終了**\n
    ターミナル上で Ctrl + C を押すと強制終了します。

    ---

    #### 開発の効率化
    1. **autopep8 の有効化**\n
    PEP8 とは、Python コードの可読性を高めるための公式スタイルガイドです。
    インデント、空白、行の長さ、命名規則などの基本的なルールを定義しています。
    autopep8 を有効にすると、PEP8 に準拠するようにコードが自動でフォーマットされます。

    **設定手順**\n
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

    2. **F5 キーで Streamlit を起動する**\n
    起動のたびに`streamlit run main.py`と入力すると時間がかかるので、VS Code のデバッグモード (F5) で起動できるように設定します。
    `.vscode`フォルダの下に`launch.json`を作成します。
    ```json
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Streamlit",
                "type": "debugpy",
                "request": "launch",
                "module": "streamlit",
                "args": [
                "run",
                "main.py"
                ]
            }
        ]
    }
    ```
    このように設定すると、VS Code で現在編集しているファイルに関わらず、F5 キーを押すと`streamlit run main.py`がデバッグモードで実行されます。
    一方で、プロジェクトの他のスクリプトを F5 キーで実行できなくなります。
    スクリプト名を`main.py`から変更する場合は`args`も修正してください。
    """
)

st.subheader("GitHub リポジトリの作成", divider=True)
st.markdown(
    """
    GitHub とは、バージョン管理システム「Git」を利用してコードを管理・共有する Web サービスです。
    後でアプリを Web サーバにデプロイする時にも、GitHub を経由してソースコードをアップロードします。
    GitHub は非常に多機能なツールですが、ここではデプロイまでに最低限必要な手続きについて説明します。\n

    :warning: **注意**\n
    GitHub にアップロードしたソースコードは、設定によっては全世界に公開されます。
    コードに機密情報が含まれる場合は、取り扱いに最新の注意を払ってください。

    ---

    #### Git のインストール (初回のみ)
    https://git-scm.com/

    ---

    #### GitHub アカウント登録 (初回のみ)
    https://github.co.jp/

    ---

    #### GitHub リポジトリの作成
    GitHub のホームページから New をクリックします。
    リポジトリ作成画面で次のように入力します。
    """
)

st.image(Image.open("data/create_repository.png"))

st.markdown(
    """
    Create repository をクリックすると、sample-app という名前の空のリポジトリが作成されます。

    **Visibility について**\n
    `Public`にすると、アップロードしたファイルが全員に公開されます。
    機密情報を含む場合など、特定の相手にだけ公開するには`Private`を選択します。

    ---

    #### ソースコードのアップロード
    ローカルのプロジェクトをGitHub のリポジトリに紐づけて、コードを GitHub にアップロードします。

    :warning: **注意**  
    Git 初見の方にとっては、しばらく意味不明な操作が続きます。  
    まずこのブロック全体を流し読みして、仕組みを把握してから手を動かすとよいです。

    **Git の初期化**  
    VS Code のソース管理画面からリポジトリを初期化します。
    """
)

st.image(Image.open("data/git_init.png"))

st.markdown(
    """
    **GitHub リポジトリを指定**  
    1.「リモート > リモートの追加」をクリックする。  
    2. GitHub リポジトリの URL`https://github.com/<ユーザー名>/sample-app.git`を入力する。  
    3. リモート名は`origin`とする。
    """
)

st.image(Image.open("data/git_add_remote.png"))

st.markdown(
    """
    **変更のステージング・コミット**  
    コミットをクリックします。コミットメッセージは適当でよいです。
    """
)

st.image(Image.open("data/first_commit.png"))

st.markdown(
    """
    **コミット内容のアップロード**  
    VS Code のソース管理画面で「Branchの発行」をクリックすると、コミットした内容が GitHub リポジトリにアップロードされます。
    ブラウザで GitHub の画面を更新すると、`main.py`がアップロードされていることが確認できます。

    **アプリを修正して再アップロード**  
    `main.py`に例えば 'Say Good Bye' ボタンを追加します。  
    変更を保存すると、変更が検知されて再びコミットできるようになります。
    「コミットしてプッシュ」を選択すると、すべての変更がステージング → コミット → プッシュされ、直ちに GitHub に反映されます。
    """
)

st.image(Image.open("data/git_push_update.png"))

st.markdown(
    """
    **git コマンドによる操作**  
    ここまでの一連の手続きはすべてターミナル上でも実行できます。

    ```bash
    # Git 初期化
    git init
    
    # リモートの追加
    git remote add origin https://github.com/<ユーザー名>/sample-app.git
    
    # 変更のステージング
    git add .
    
    # 変更のコミット
    git commit -m 'First commit'
    
    # ブランチの作成 (一度だけ)
    git branch -M main
    
    # アップロード
    git push -u origin main
    ```
    
    **gitはいったい何をしているのか**  
    """
)
