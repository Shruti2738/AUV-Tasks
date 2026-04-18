import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class RawPublisher(Node):

    def __init__(self):
        super().__init__('raw_publisher')

        self.publisher__ = self.create_publisher(Int32, '/raw_signal', 10)

        self.counter__ = 1

        self.timer__ = self.create_timer(1.0, self.publish_number)

    def publish_number(self):

        msg__ = Int32()

        msg__.data = self.counter__ * 2

        self.publisher__.publish(msg__)

        self.get_logger().info(f"Published: {msg__.data}")

        self.counter__ += 1


def main(args=None):

    rclpy.init(args=args)

    NodeObject__ = RawPublisher()

    rclpy.spin(NodeObject__)

    NodeObject__.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
