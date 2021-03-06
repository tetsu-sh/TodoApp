# TodoApp


## 技術決定
- オニオンアーキテクチャで以下の4層構成の実装を行った。一般的にはapplication層とされる部分に関してはusecaseと表現している。その方が感覚的にわかりやすいため。
    - domain
    - repository
    - presentation
    - usecase
- serverはFastApiを使用。Flaskでも良いが、open-apiの自動生成による確認、デバッグが容易である。Flaskと比べ多機能なため、仕様の変更に耐えられる可能性が高い。また、ドキュメント生成が非常に便利で外部公開や管理が効率的になる。
- 参照系はリポジトリクラスに直接記載せず、クエリとして分離することで、リポジトリクラスの肥大化及び複雑化を防いだ。置き場としてはリポジトリ層内にクエリクラスを配置
- ユーザー, タスク共に重複を許さない仕組みは実装しないとした。
- Enumを用いて状態や優先度を表現した。order_byがnameのアルファベットでソートされるため、「a:メンバー値」という形式で実装した。apiの返り値やコード上ではメンバー値で取り扱われ、意味を持つ単語で表記されるので、感覚的に見ることができる。
- testはコマンド系のみ記述した。test用DBの準備や、クエリ系のモック化等は時間の短縮化のために省略。また、inmemory_repositoryを用いたusecaseのテストのみとした。
- insert_datas.pyを用いて大量にuser, task投入し、クエリを実行した。未完了タスク一覧が若干時間を要する（2secほど）。それ以外は違和感のない速度であった。



## 使い方
- 必要ライブラリはrequirements.txtに記載
- todo直下で、以下を実行して、tableを作成する。
```
python create_table.py
```
- serverを実行
```
uvicorn presentation.server:app --reload
```
- http://localhost:8000　にサーバーが立ち上がる
- http://localhost:8000/docs# 　でswaggarが立ち上がるので、そちらでAPIの確認及び実行をできる
- タスク作成時、priorityは"high", "middle", "low"のいずれかを入力する。
