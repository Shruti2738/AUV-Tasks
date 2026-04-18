import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class ProcessorNode(Node):

    def __init__(self):

        super().__init__('processor_node')

        self.subscription__ = self.create_subscription(
            Int32,
            '/raw_signal'
            self.process_number,
            10
        )

        self.publisher__ = self.create_publisher(
            Int32
            '/processed_signal',
            10
        )

    def process_number(self, msg__):

        new_msg__ = Int32()

        new_msg__.data = msg__.data * 5

        self.publisher__.publish(new_msg__)

        self.get_logger().info(f"Processed: {new_msg__.data}")


def main(args=None):

    rclpy.init(args=args)

    NodeObject__ = ProcessorNode()

    rclpy.spin(NodeObject__)

    NodeObject__.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
