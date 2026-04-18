import rclpy
from rcply.node import Node

class chatnode(node):
def _init_(self):
	super()._init_("chat_node")
	self.get_logger().info("Node started successfully")

def main():
	rcply.init()
	node=chatnode()
	rcply.spin(node)
	node.destroy_node()
	rcply.shutdown()

if _nameN=="_main_":
	main()
