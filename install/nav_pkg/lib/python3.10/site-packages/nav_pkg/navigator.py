import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from nav_interfaces.msg import BotPose


class Navigator(Node):

    def __init__(self):

        super().__init__('navigator')

        self.subscription = self.create_subscription(
            String,
            '/cmd',
            self.cmd_callback,
            10
        )

        self.publisher = self.create_publisher(
            BotPose,
            '/bot_pose',
            10
        )

        self.x = 0.0
        self.y = 0.0
        self.direction = "North"

        self.directions = ["North", "East", "South", "West"]

    def turn_right(self):

        index = self.directions.index(self.direction)
        self.direction = self.directions[(index + 1) % 4]

    def turn_left(self):

        index = self.directions.index(self.direction)
        self.direction = self.directions[(index - 1) % 4]

    def move_forward(self):

        if self.direction == "North":
            self.y += 1

        elif self.direction == "South":
            self.y -= 1

        elif self.direction == "East":
            self.x += 1

        elif self.direction == "West":
            self.x -= 1

    def move_backward(self):

        if self.direction == "North":
            self.y -= 1

        elif self.direction == "South":
            self.y += 1

        elif self.direction == "East":
            self.x -= 1

        elif self.direction == "West":
            self.x += 1

    def cmd_callback(self, msg):

        command = msg.data

        if command == "turn right":
            self.turn_right()

        elif command == "turn left":
            self.turn_left()

        elif command == "forward":
            self.move_forward()

        elif command == "backward":
            self.move_backward()

        pose = BotPose()

        pose.x = float(self.x)
        pose.y = float(self.y)
        pose.facing_direction = self.direction

        self.publisher.publish(pose)

        self.get_logger().info(
            f"Bot Position: ({self.x}, {self.y}) Facing: {self.direction}"
        )


def main(args=None):

    rclpy.init(args=args)

    node = Navigator()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()
