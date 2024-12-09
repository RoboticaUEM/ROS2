from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='yolo11',
            namespace='yoloprocess',
            executable='webpub',
            name='webpub'
        ),
        Node(
            package='yolo11',
            namespace='yoloprocess',
            executable='view_imgprocess',
            name='view_imgprocess'
        ),
        Node(
            package='yolo11',
            namespace='yoloprocess',
            executable='yolo_process',
            name='yolo_process'
        )
    ])
