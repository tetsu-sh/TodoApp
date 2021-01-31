# TodoApp


## 技術決定
- オニオンアーキテクチャで以下の4層構成の実装を行った。一般的にはapplication層とされる部分に関してはusecaseと表現している。その方が感覚的にわかりやすいため
    - domain
    - repository
    - presentation
    - usecase
- serverはFastApiを使用。Flaskでも良いが、open-apiの自動生成による確認、デバッグが容易である。
- 参照系はリポジトリクラスに直接記載せず、クエリとして分離して、リポジトリクラスの肥大化、複雑化を防いだ。置き場としてはリポジトリ層ないにクエリクラスを配置



## 使い方
- todo直下で、以下を実行して、tableを作成する。
```
python create_db.py
```
- serverを実行
```
uvicorn presentation.server:app --reload
```