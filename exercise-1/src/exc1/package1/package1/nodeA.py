import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32


class NodeA(Node):

    def __init__(self):
        super().__init__('nodeA')

        self.publisher = self.create_publisher(
            Int32,
            '/yu',
            10
        )

        self.k = 4

        self.timer = self.create_timer(
            0.05,
            self.timer_callback
        )

    def timer_callback(self):
        msg = Int32()
        msg.data = self.k

        self.publisher.publish(msg)

        self.get_logger().info(f'Publishing: {msg.data}')

        self.k += 4


def main(args=None):
    rclpy.init(args=args)

    node = NodeA()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()