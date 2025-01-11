#!/usr/bin/env python3
 
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, CompressedImage
from std_msgs.msg import String
from cv_bridge import CvBridge
from ultralytics import YOLO
from std_msgs.msg import Header

import cv2
#import datetime
    
#GREEN = (0, 255, 0)
#ANTIGUEDAD_IMG = rospy.Duration(0.1)

class YoloProcessCompressed(Node):

    def __init__(self):
        super().__init__('YoloProcessCompressed')
        self.model = YOLO("/home/mixi/yolo11/yolo11n.pt", verbose=True)
        self.subscription_img = self.create_subscription(CompressedImage,'/webcam/image/compressed',self.callback,1)
        self.subscription_img  # prevent unused variable warning
        self.publisher_json = self.create_publisher(String, '/yolo/inference', 1)
        self.publisher_json
        self.publisher_img = self.create_publisher(CompressedImage, '/yolo/image/compressed', 1)
        self.publisher_img
        self.br = CvBridge()

    def callback(self, msg):
        '''
        if((rospy.Time.now() - data.header.stamp) > ANTIGUEDAD_IMG):
        return
        '''
        msg_json = String()
        # run the YOLO model on the frame
        result = self.model.predict(self.br.compressed_imgmsg_to_cv2(msg), verbose=False, classes=[0,39])[0]
        self.get_logger().info('result: "%s" ' % result.verbose())
        self.get_logger().info("tiempo: [{}]".format(self.get_clock().now().seconds))
        frame_compressed = self.br.cv2_to_compressed_imgmsg(result.plot(), dst_format='jpeg')
        frame_compressed.format = "jpeg"
        frame_compressed.header = Header()
        #frame_compressed.header.seq = self.sec_uint32
        frame_compressed.header.stamp = self.get_clock().now().to_msg()
        frame_compressed.header.frame_id = "Image Compressed"
        self.publisher_img.publish(frame_compressed)
        msg_json.data = result.to_json(normalize=True, decimals=6)
        #msg_json.data = str(result.summary(normalize=True, decimals=6))
        self.publisher_json.publish(msg_json)


def main(args=None):
    rclpy.init(args=args)

    yoloProcess = YoloProcessCompressed()

    rclpy.spin(yoloProcess)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    yoloProcess.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


