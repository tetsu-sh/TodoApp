# TodoApp


## 技術決定
- オニオンアーキテクチャで以下の4層構成の実装を行った。一般的にはapplication層とされる部分に関してはusecaseと表現している。その方が感覚的にわかりやすいため
    - domain
    - repository
    - presentation
    - usecase
- serverはFastApiを使用。Flaskでも良いが、open-apiの自動生成による確認、デバッグが容易である。Flaskと比べ多機能なため、仕様の変更に耐えられる可能性が高い
- 参照系はリポジトリクラスに直接記載せず、クエリとして分離して、リポジトリクラスの肥大化、複雑化を防いだ。置き場としてはリポジトリ層ないにクエリクラスを配置
- user, task共に重複を許さない仕組みは実装しない
- testはコマンド系のみ記述した。test用DBの準備や、クエリ系のモック化等は時間の短縮化のために、省略。また、inmemory_repositoryを用いたusecaseのテストのみとした。
- insert_datas.pyを用いて大量にuser, task投入し、クエリを実行した。未完了タスク一覧が若干時間を要する（2secほど）が、10000のタスク量で直列クエリの中では用途に耐えられるレベルである。



## 使い方
- todo直下で、以下を実行して、tableを作成する。
```
python create_db.py
```
- serverを実行
```
uvicorn presentation.server:app --reload
```