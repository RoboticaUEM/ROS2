import rclpy
from rclpy.node import Node

from std_msgs.msg import Header
from rclpy.time import Time

class ClockSubscriber(Node):

    def __init__(self):
        super().__init__('subscriber', enable_rosout=False, namespace="py_clocktest")
        qos_policy = rclpy.qos.QoSProfile(reliability=rclpy.qos.ReliabilityPolicy.BEST_EFFORT,
                                          #reliability=rclpy.qos.ReliabilityPolicy.RELIABLE,
                                          history=rclpy.qos.HistoryPolicy.KEEP_LAST,
                                          depth=1)
        self.subscription = self.create_subscription(Header, '/py_clock/tiempo', self.listener_callback, qos_profile=qos_policy)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('recived: {}'.format(msg.stamp))
        dif = self.get_clock().now() - Time.from_msg(msg.stamp)
        print("  -->  diferencia:", dif, ",", dif.nanoseconds/1000000000, "seconds")

def main(args=None):
    rclpy.init(args=args)

    clock_subscriber = ClockSubscriber()

    rclpy.spin(clock_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    clock_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
