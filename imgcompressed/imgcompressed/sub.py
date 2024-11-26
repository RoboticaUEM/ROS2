import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, CompressedImage
from cv_bridge import CvBridge
import cv2
  
class ImageSubscriber(Node):
  
  def __init__(self):
    super().__init__('Webcam_subscriber')
    self.subscription = self.create_subscription(CompressedImage, '/webcam/image_raw/compressed', self.listener_callback, 1)
    self.subscription # prevent unused variable warning
    self.br = CvBridge()
    
  def listener_callback(self, data):
    self.get_logger().info('Receiving video frame')
    current_frame = self.br.compressed_imgmsg_to_cv2(data)
    cv2.imshow("camera", current_frame)
    cv2.waitKey(1)
   
def main(args=None):
  rclpy.init(args=args)
  image_subscriber = ImageSubscriber()
  rclpy.spin(image_subscriber)
  image_subscriber.destroy_node()
  rclpy.shutdown()
   
if __name__ == '__main__':
  main()

