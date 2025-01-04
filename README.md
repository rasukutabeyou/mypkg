# mypkg

![test](https://github.com/rasukutabeyou/mypkg/actions/workflows/test.yml/badge.svg)

## 概要

ROS2のパッケージ

以下のノードが実装されている。
  - パブリッシャ:`coordinater.py`
  - サブスクライバ:`listener.py`

また、`coordinater.py`、`listener.py` に対応するlaunchファイル`coordinate_listen.launch.py`が実装されている。

## ノードについて

### coordinater

- 基本動作

日本の都市圏の位置する緯度、経度についてをトピックに出します。

札幌、仙台、東京、横浜、名古屋、大阪、京都、神戸、広島、福岡の都市に対応しています。

- トピックについて
  - トピック名:`point`
  - メッセージ型:`Point`（ROS2標準メッセージ型`geometry_msgs.msg.Point`に対応）

- 利用方法

`ros2 run mypkg coordinater`で実行

- 実行例

以下の例はlaunchファイル`coordinate_listen.launch.py`を利用し、`listener.py`を用いてトピックを受け取ったものです。

```
$ ros2 launch mypkg coordinate_listen.launch.py
  （一部省略）
[listener-2] [INFO] [1736008652.307243181] [litener]: 札幌:(43.062100,141.354400)
[listener-2] [INFO] [1736008652.807296222] [litener]: 仙台:(38.268200,140.869400)
[listener-2] [INFO] [1736008653.307704238] [litener]: 東京:(35.689500,139.691700)
[listener-2] [INFO] [1736008653.808216321] [litener]: 横浜:(35.443700,139.638000)
[listener-2] [INFO] [1736008654.307794456] [litener]: 名古屋:(35.181500,136.906600)
[listener-2] [INFO] [1736008654.807953782] [litener]: 大阪:(34.693700,135.502300)
[listener-2] [INFO] [1736008655.307945609] [litener]: 京都:(35.011600,135.768100)
[listener-2] [INFO] [1736008655.807486924] [litener]: 神戸:(34.690100,135.195600)
[listener-2] [INFO] [1736008656.308700466] [litener]: 広島:(34.385300,132.455300)
[listener-2] [INFO] [1736008656.807823705] [litener]: 福岡:(33.590400,130.401700)
```

- その他

一秒ごとにトピックに出力します。

札幌~福岡が一巡となり、福岡の次は札幌に戻り、座標を出力します。

## 必要なソフトウェア
- Python
  - テスト済みバージョン:3.7~3.10
- ROS2
  - テスト済みディストリビューション:Humble Hawksbill

## テスト環境
- ubuntu-22.04

## その他
 - このソフトウェアは、3条項BSDライセンスの下、再頒布および使用が許可されます。

 - © 2025 Kouta Sakai
