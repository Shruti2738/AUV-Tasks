import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class OutputNode(Node):

    def __init__(self):

        super().__init__('output_node')

        self.subscription__ = self.create_subscription(
            Int32,
            '/processed_signal',
            self.final_output,
            10
        )

    def final_output(self, msg__):

        result__ = msg__.data + 10

        self.get_logger().info(f"Final Output: {result__}")


def main(args=None):

    rclpy.init(args=args)

    NodeObject__ = OutputNode()

    rclpy.spin(NodeObject__)

    NodeObject__.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
