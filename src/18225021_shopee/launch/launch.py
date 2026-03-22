from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='18225021_shopee',
            executable='publisher_node',
            name='publisher_node',
            output='screen'
        ),
        Node(
            package='18225021_shopee',
            executable='subscriber_node',
            name='subscriber_node',
            output='screen'
        )
    ])