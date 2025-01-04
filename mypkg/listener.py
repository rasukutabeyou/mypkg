import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point


rclpy.init()
node = Node("litener")
n = "name"


def cb(coordinate):
    global node
    #print (n)
    node.get_logger().info(": %f,%f" % (coordinate.x,coordinate.y))


def main():
    pub = node.create_subscription(Point, "point", cb, 8)
    rclpy.spin(node)
