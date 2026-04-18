import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Commander(Node):

    def __init__(self):
        super().__init__('commander')

        self.publisher = self.create_publisher(String, '/cmd', 10)

    def run(self):

        while rclpy.ok():

            command = input("Enter command (forward/backward/turn left/turn right): ")

            msg = String()
            msg.data = command

            self.publisher.publish(msg)

            self.get_logger().info(f"Command Sent: {command}")


def main(args=None):

    rclpy.init(args=args)

    node = Commander()

    node.run()

    node.destroy_node()

    rclpy.shutdown()
