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
            self.command_callback,
            10)

        self.publisher = self.create_publisher(BotPose, '/bot_pose', 10)

        self.x = 0.0
        self.y = 0.0
        self.direction = "North"

        self.get_logger().info("Navigator started at (0,0) facing North")

    def command_callback(self, msg):
        command = msg.data.lower()

        # -------- STATE MACHINE --------

        if command == "turn right":
            if self.direction == "North":
                self.direction = "East"
            elif self.direction == "East":
                self.direction = "South"
            elif self.direction == "South":
                self.direction = "West"
            elif self.direction == "West":
                self.direction = "North"

        elif command == "turn left":
            if self.direction == "North":
                self.direction = "West"
            elif self.direction == "West":
                self.direction = "South"
            elif self.direction == "South":
                self.direction = "East"
            elif self.direction == "East":
                self.direction = "North"

        elif command == "forward":
            if self.direction == "North":
                self.y += 1
            elif self.direction == "South":
                self.y -= 1
            elif self.direction == "East":
                self.x += 1
            elif self.direction == "West":
                self.x -= 1

        elif command == "backward":
            if self.direction == "North":
                self.y -= 1
            elif self.direction == "South":
                self.y += 1
            elif self.direction == "East":
                self.x -= 1
            elif self.direction == "West":
                self.x += 1

        # -------- Publish BotPose --------

        pose = BotPose()
        pose.x = self.x
        pose.y = self.y
        pose.facing_direction = self.direction

        self.publisher.publish(pose)

        self.get_logger().info(
            f"Position: ({self.x}, {self.y}) Facing: {self.direction}"
        )


def main(args=None):
    rclpy.init(args=args)

    node = Navigator()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
