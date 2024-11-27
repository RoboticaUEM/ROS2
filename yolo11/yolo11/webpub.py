import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, CompressedImage
from cv_bridge import CvBridge
from std_msgs.msg import Header
import cv2

#https://docs.ros.org/en/indigo/api/cv_bridge/html/python/

class ImagePublisher(Node):

    def __init__(self):
        super().__init__('Webcam_publisher')
        self.publisher_ = self.create_publisher(CompressedImage, '/webcam/image/compressed', 1)
        #self.publisher_ = self.create_publisher(Image, '/webcam/image', 1)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("VideoCapture error!!")
            exit()
        self.br = CvBridge()
        self.sec_uint32 = 0;

    def timer_callback(self):
        ret, frame = self.cap.read()
        if not ret:
            return
        frame_compressed = self.br.cv2_to_compressed_imgmsg(frame, dst_format='jpeg')
        frame_compressed.format = "jpeg"
        frame_compressed.header = Header()
        #frame_compressed.header.seq = self.sec_uint32
        frame_compressed.header.stamp = self.get_clock().now().to_msg();
        frame_compressed.header.frame_id = "WebCam Compressed"
        self.publisher_.publish(frame_compressed)
        #self.publisher_.publish(self.br.cv2_to_imgmsg(frame, "bgr8"))
        self.get_logger().info('Publishing video frame')
        self.sec_uint32 += 1

def main(args=None):
    rclpy.init(args=args)
    image_publisher = ImagePublisher()
    rclpy.spin(image_publisher)
    image_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
