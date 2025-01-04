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

日本の都市圏の位置する緯度と経度についてをトピックに出します。

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
[listener-2] [INFO] [1736010611.306853687] [litener]: 札幌:(43.062100,141.354400)
[listener-2] [INFO] [1736010612.307445267] [litener]: 仙台:(38.268200,140.869400)
[listener-2] [INFO] [1736010613.308143962] [litener]: 東京:(35.689500,139.691700)
[listener-2] [INFO] [1736010614.307367505] [litener]: 横浜:(35.443700,139.638000)
[listener-2] [INFO] [1736010615.307755592] [litener]: 名古屋:(35.181500,136.906600)
[listener-2] [INFO] [1736010616.307993965] [litener]: 大阪:(34.693700,135.502300)
[listener-2] [INFO] [1736010617.307512668] [litener]: 京都:(35.011600,135.768100)
[listener-2] [INFO] [1736010618.308153659] [litener]: 神戸:(34.690100,135.195600)
[listener-2] [INFO] [1736010619.308164341] [litener]: 広島:(34.385300,132.455300)
[listener-2] [INFO] [1736010620.308121517] [litener]: 福岡:(33.590400,130.401700)
[listener-2] [INFO] [1736010621.307313356] [litener]: 札幌:(43.062100,141.354400)
[listener-2] [INFO] [1736010622.307836753] [litener]: 仙台:(38.268200,140.869400)
```

- その他

札幌から福岡までを一巡とし、福岡の次は札幌に戻り座標を出力します。

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
