# mypkg

## 概要

2024年度　ロボットシステム学における練習、課題提出用
主にros2システムの使いかたを学ぶ。

パブリッシャを持つノード`coordinater.py`、サブスクライバを持つノード（テスト用）`listener.py`を持つパッケージとなっている。
また、`coordinater.py`、`listener.py`に対応するlaunchファイル`coordinate_listen.launch.py`が実装されている。

## ダウンロード、ビルド

以下の手順に従ってください

```
#ワークスペースの用意
$ mkdir -p ros2_ws/src
#ディレクトリの移動
$ cd ~/ros2_ws/src
#リポジトリをクローン
$ git clone https://github.com/rasukutabeyou/mypkg.git
  （略）
#ビルド
$ cd ~/ros2_ws
$ colcon build
　（略）
#ソース
$ source ~/ros2_ws/install/setup.bash #必要に応じて~/.bashrcに書き込んでください
$ source ~/ros2_ws/install/local_setup.bash #必要に応じて~/.bashrcに書き込んでください
$ source ~/.bashrc
```

## ノードについて

### coordinater

- 基本動作

X,Y,Zについての座標をトピックに出します。
初期値を(x,y,z)=(1,1,1)として送信ごとにx,y,zの順番に1ずつ10の値になるまで加算されます。
また、送信の間隔は0.5秒です。

- トピックについて
  - トピック名:`point`
  - メッセージ型:`Point`（ROS2標準メッセージ型`geometry_msgs.msg.Point`に対応）

- 利用方法

`ros2 run mypkg coordinater`で実行

- 実行例

以下の例はlaunchファイルを`coordinate_listen.launch.py`利用し、`listener.py`を用いてトピックを受け取ったものです。

```
$ ros2 launch mypkg coordinate_listen.launch.py
  （一部省略）
[listener-2] [INFO] [1735808583.853801749] [litener]: (x,y,z): 1.000000,1.000000,1.000000
[listener-2] [INFO] [1735808584.344710696] [litener]: (x,y,z): 2.000000,1.000000,1.000000
[listener-2] [INFO] [1735808584.844767324] [litener]: (x,y,z): 3.000000,1.000000,1.000000
[listener-2] [INFO] [1735808585.344536770] [litener]: (x,y,z): 4.000000,1.000000,1.000000
[listener-2] [INFO] [1735808585.845726287] [litener]: (x,y,z): 5.000000,1.000000,1.000000
[listener-2] [INFO] [1735808586.345044407] [litener]: (x,y,z): 6.000000,1.000000,1.000000
[listener-2] [INFO] [1735808586.845282940] [litener]: (x,y,z): 7.000000,1.000000,1.000000
[listener-2] [INFO] [1735808587.344697432] [litener]: (x,y,z): 8.000000,1.000000,1.000000
[listener-2] [INFO] [1735808587.844839128] [litener]: (x,y,z): 9.000000,1.000000,1.000000
[listener-2] [INFO] [1735808588.346453332] [litener]: (x,y,z): 10.000000,1.000000,1.000000
[listener-2] [INFO] [1735808588.845629218] [litener]: (x,y,z): 10.000000,2.000000,1.000000
  （一部省略）
[listener-2] [INFO] [1735808595.845030099] [litener]: (x,y,z): 10.000000,10.000000,7.000000
[listener-2] [INFO] [1735808596.345242118] [litener]: (x,y,z): 10.000000,10.000000,8.000000
[listener-2] [INFO] [1735808596.844691855] [litener]: (x,y,z): 10.000000,10.000000,9.000000
[listener-2] [INFO] [1735808597.344285554] [litener]: (x,y,z): 10.000000,10.000000,10.000000
[listener-2] [INFO] [1735808597.844549066] [litener]: (x,y,z): 10.000000,10.000000,10.000000
  （略）
```

## 必要なソフトウェア
- Python
  - テスト済みバージョン:3.7~3.10

## テスト環境
- ubuntu-22.04

## その他
 - このソフトウェアは、3条項BSDライセンスの下、再頒布および使用が許可されます。

 - © 2025 Kouta Sakai
