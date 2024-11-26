import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, CompressedImage
from cv_bridge import CvBridge
import cv2
  
#https://docs.ros.org/en/indigo/api/cv_bridge/html/python/
  
class ImagePublisher(Node):
  
  def __init__(self):
    super().__init__('Webcam_publisher')
    self.publisher_ = self.create_publisher(CompressedImage, '/webcam/image_raw/compressed', 1)
    timer_period = 0.333
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.cap = cv2.VideoCapture(0)
    if not self.cap.isOpened():
    	print("VideoCapture error!!")
    	exit()
    self.br = CvBridge()
    
  def timer_callback(self):
    ret, frame = self.cap.read()
    if ret == True:
      self.publisher_.publish(self.br.cv2_to_compressed_imgmsg(frame, dst_format='jpg'))
      #self.publisher_.publish(self.br.cv2_to_compressed_imgmsg(frame, "bgr8"))
    self.get_logger().info('Publishing video frame')
   
def main(args=None):
  rclpy.init(args=args)
  image_publisher = ImagePublisher()
  rclpy.spin(image_publisher)
  image_publisher.destroy_node()
  rclpy.shutdown()
   
if __name__ == '__main__':
  main()

