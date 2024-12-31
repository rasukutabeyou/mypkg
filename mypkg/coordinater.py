import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point

rclpy.init()
node = Node("coordinate")
pub = node.create_publisher(Point, "point", 10)

a = 1.0
b = 1.0
c = 1.0


def cb():
    global a, b, c
    coordinate = Point()
    coordinate.x = a
    coordinate.y = b
    coordinate.z = c
    pub.publish(coordinate)
    if a < 10.0:
        a += 1.0
    elif b < 10.0:
        b += 1.0
    elif c < 10.0:
        c += 1.0


def main():
    node.create_timer(0.5, cb)
    rclpy.spin(node)
