import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import sys
import pyfirmata2


class FirmataSuscriber(Node):

    def __init__(self):
        super().__init__('arduinoPin13')
        self.board = None
        try:
            self.board = pyfirmata2.Arduino(pyfirmata2.Arduino.AUTODETECT)
            # self.board = pyfirmata2.Arduino('/dev/ttyACM0')
        except Exception as inst:
            self.get_logger().error('Error arduino: "%s"' % inst.args)
            sys.exit(-1)
        self.pin13 = self.board.get_pin('d:13:o')
        self.subscription = self.create_subscription(Bool, 'arduino_pin13', self.listener_callback, 1)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%i"' % msg.data)
        self.pin13.write(msg.data)
        
    def __del__(self):
        if self.board is not None:
            self.board.exit()


def main(args=None):
    rclpy.init(args=args)

    firmata_suscriber = FirmataSuscriber()

    rclpy.spin(firmata_suscriber)

    firmata_suscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
