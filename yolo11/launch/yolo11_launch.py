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
            executable='websupprocess',
            name='view_imgprocess'
        ),
        Node(
            package='yolo11',
            namespace='yoloprocess',
            executable='yolo_test',
            name='yolo_test'
        )
    ])
