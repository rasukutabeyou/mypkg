import rclpy
from rclpy.node import Node
from mypkg.msg import Person


rclpy.init()
node = Node("litener")


def cb(msg):
    global node
    node.get_logger().info("Listen: %d" % msg)


def main():
    pub = node.create_subscription(Person, "person", cb, 10)
    rclpy.spin(node)
