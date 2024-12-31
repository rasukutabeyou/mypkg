import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point


rclpy.init()
node = Node("litener")


def cb(coordinate):
    global node
    node.get_logger().info("(x,y,z): %f,%f,%f" % (coordinate.x,coordinate.y,coordinate.z))


def main():
    pub = node.create_subscription(Point, "point", cb, 10)
    rclpy.spin(node)
