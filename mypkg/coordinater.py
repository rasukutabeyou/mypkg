import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point

x = 0.0
y = 0.0
#z = 0.0

rclpy.init()
node = Node("coordinate")
pub = node.create_publisher(Point, "point", 10)


def cb():
    coordinate = Point()
    coordinate.x = x
    coordinate.y = y
    #coordinate.z = z
    pub.publish(coordinate)


def main():
    global x,y#,z

    a = input()
    b = input()
    #c = input()

    x = float(a)
    y = float(b)
    #z = float(c)


    node.create_timer(0.5, cb)
    rclpy.spin(node)
