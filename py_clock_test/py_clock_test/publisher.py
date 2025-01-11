import rclpy
from rclpy.node import Node

from std_msgs.msg import Header
from rclpy.time import Time

class ClockPublisher(Node):

    def __init__(self):
        super().__init__('publisher', enable_rosout=False, namespace="py_clocktest")
        qos_policy = rclpy.qos.QoSProfile(reliability=rclpy.qos.ReliabilityPolicy.BEST_EFFORT,
                                          history=rclpy.qos.HistoryPolicy.KEEP_LAST,
                                          depth=1)
        self.publisher_ = self.create_publisher(Header, '/py_clock/tiempo', qos_profile=qos_policy)
        timer_period = 0.33  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Header()
        msg.stamp = self.get_clock().now().to_msg()
        msg.frame_id = "clock_type=ROS_TIME"
        self.publisher_.publish(msg)
        self.get_logger().info('send: {}'.format(msg.stamp))
        '''
        print("self.get_clock().now().to_msg():", self.get_clock().now().to_msg())
        print("self.get_clock().now():", self.get_clock().now())
        print("Time.from_msg(self.get_clock().now().to_msg()).nanoseconds:", Time.from_msg(self.get_clock().now().to_msg()).nanoseconds)
        dif = Time.from_msg(self.get_clock().now().to_msg()) - self.get_clock().now()
        print("diferencia:", type(dif), dif)
        '''

def main(args=None):
    rclpy.init(args=args)

    clock_publisher = ClockPublisher()

    rclpy.spin(clock_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    clock_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

