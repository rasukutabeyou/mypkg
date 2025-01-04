# SPDX-FileCopyrightText: 2025 Kouta Sakai
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point


rclpy.init()
node = Node("litener")
name="initial value"

def cb(coordinate):
    global node, name


    if coordinate.x == 43.0621:
        name = "札幌"
    elif coordinate.x == 38.2682:
        name = "仙台"
    elif coordinate.x == 35.6895:
        name = "東京"
    elif coordinate.x == 35.4437:
        name = "横浜"
    elif coordinate.x == 35.1815:
        name = "名古屋"
    elif coordinate.x == 34.6937:
        name = "大阪"
    elif coordinate.x == 35.0116:
        name = "京都"
    elif coordinate.x == 34.6901:
        name = "神戸"
    elif coordinate.x == 34.3853:
        name = "広島"
    elif coordinate.x == 33.5904:
        name = "福岡"
    elif coordinate.x == 0.0:
        pass
    else:
        name = "error"

    node.get_logger().info("%s:(%f,%f)" % (name,coordinate.x,coordinate.y))


def main():
    pub = node.create_subscription(Point, "point", cb, 8)
    rclpy.spin(node)
