import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point

rclpy.init()
node = Node("coordinate")
pub = node.create_publisher(Point, "point", 10)


def cb():
    msg = Point()
    msg.x = 1.0
    msg.y = 1.0
    msg.z = 1.0
    pub.publish(msg)


def main():
    node.create_timer(0.5, cb)
    rclpy.spin(node)
