# SPDX-FileCopyrightText: 2025 Kouta Sakai 　　　　　
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point

rclpy.init()
node = Node("coordinate")
pub = node.create_publisher(Point, "point", 8)


a = 0.0
b = 0.0
#c = 0.0
n = 0


def cb():
    global a, b, n
    coordinate = Point()
    coordinate.x = a
    coordinate.y = b
    #coordinate.z = c
    pub.publish(coordinate)
    if n == 0:#札幌
        a = 43.0621
        b = 141.3544
        n = 1
    elif n == 1:#仙台
        a = 38.2682
        b = 140.8694
        n = 2
    elif n == 2:#東京
        a = 35.6895
        b = 139.6917
        n = 3
    elif n == 3:#横浜
        a =35.4437
        b =139.6380
        n =4
    elif n == 4:#名古屋
        a =35.1815
        b =136.9066
        n =5
    elif n == 5:#大阪
        a =34.6937
        b =135.5023
        n =6
    elif n == 6:#京都
        a =35.0116
        b =135.7681
        n =7
    elif n == 7:#神戸
        a =34.6901
        b =135.1956
        n =8
    elif n == 8:#広島
        a = 34.3853
        b = 132.4553
        n = 9
    elif n == 9:#福岡
        a = 33.5904
        b = 130.4017
        n = 0


def main():
    node.create_timer(1.0, cb)
    rclpy.spin(node)
