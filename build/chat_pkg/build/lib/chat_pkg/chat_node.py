import rclpy
from rclpy.node import Node

class chatNode(Node):
	def __init__(self):
		super().__init__("chat_node")
		self.get_logger().info("Node started successfully")

def main():
	rclpy.init()
	node=chatNode()	
	rclpy.spin(node)
	node.destroy_node()
	rclpy.shutdown()

if __name__=="__main__":
	main()
