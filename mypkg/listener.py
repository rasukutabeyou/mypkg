import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point


rclpy.init()
node = Node("litener")


def cb(coordinate):
    global node
    node.get_logger().info("(緯度,経度):%f,%f" % (coordinate.x,coordinate.y))


def main():
    pub = node.create_subscription(Point, "point", cb, 8)
    rclpy.spin(node)
