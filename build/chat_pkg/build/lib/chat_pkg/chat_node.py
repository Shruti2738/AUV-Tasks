
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import sys


class ChatNode(Node):

    def __init__(self, username):
        super().__init__('chat_node')

        self.username = username

        # publisher
        self.publisher = self.create_publisher(String, 'chat', 10)

        # subscriber
        self.subscription = self.create_subscription(
            String,
            'chat',
            self.receive_message,
            10
        )

        self.get_logger().info(f"{self.username} is online")

    def send_message(self):
        message = input(f"[{self.username}]: ")

        # simple funny default if empty
        if message.strip() == "":
            if self.username == "Invictus":
                message = "I'm drowning... send help 😭"
            else:
                message = "You ARE a submarine bro 🤦‍♂️"

        msg = String()
        msg.data = f"{self.username}:{message}"

        self.publisher.publish(msg)

    def receive_message(self, msg):
        sender, message = msg.data.split(":", 1)

        if sender != self.username:
            print(f"[{sender}]: {message}")


def main():
    rclpy.init()

    if len(sys.argv) < 2:
        print("Usage: ros2 run chat_pkg chat_node Invictus/Hawcker")
        return

    username = sys.argv[1]

    node = ChatNode(username)

    # simple loop instead of timer (easier to understand)
    while rclpy.ok():
        node.send_message()

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
