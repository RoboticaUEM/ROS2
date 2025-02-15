from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'yolo11'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mixi',
    maintainer_email='mixi@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'webpub = yolo11.webpub:main',
            'yolo_test = yolo11.yolo_test:main',
            'view_imgprocess = yolo11.websupprocess:main',
            'yolo_process = yolo11.yolo_process:main',
        ],
    },
)
