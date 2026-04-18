import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ChatNode(Node):

    def __init__(self):
        super().__init__('chat_node')

        self.publisher = self.create_publisher(String, 'chat', 10)
        self.timer = self.create_timer(2.0, self.send_message)

        self.get_logger().info("Chat node started")

    def send_message(self):
        msg = String()
        msg.data = "Hello from node"
        self.publisher.publish(msg)

        self.get_logger().info("Message sent")


def main():
    rclpy.init()
    node = ChatNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

