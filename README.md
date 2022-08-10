# learning_python_01

Python Boot Camp Text
https://pycamp.pycon.jp/index.html
で学習。

まねして、ワッフル用ミックス粉のメーカーと商品名をスクレイピング。改行は何もコントロールしていない…。

## 学習メモ

### シーケンス型
順序を持つ、繰り返し可能な型。文字列もその一つ。

`for 変数名 in シーケンス（シーケンスのオブジェクト）`

### リスト内包表記

### シーケンス型から複数変数への代入

### かっこを省略したタプルの宣言

### None
Pythonの組み込み定数。何も値がないことを表す。

### 集合型（set）
1つの集合内には同じ値は1つしか存在できない。一意な値を管理するのに便利。

### 関数を直接インポートする方法
from スクリプト import 関数名

### 正規表現モジュールのre
groupがちょっとわかってない・・・

### PyPI
パイピーアイ

### 仮想環境の共有
https://pycamp.pycon.jp/textbook/6_venv.html

`pip freeze > requirements.txt`

venvを作って、アクティベイトして、

`pip install -r requirements.txt`

で環境を共有できる

### スクリプトが実行されたときに、指定した関数を実行する
```
if __name__ == '__main__':
    関数名()
```
