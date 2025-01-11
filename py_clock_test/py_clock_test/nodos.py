
import rclpy

global_node = None

def main(args=None):
    global global_node
    rclpy.init(args=args)

    global_node = rclpy.create_node('testNodes')

    loop_rate = global_node.create_rate(1, global_node.get_clock())  # 1 Hz
    while rclpy.ok():
        rclpy.spin_once(global_node)
        print("=========================================================================")
        print(global_node.get_node_names_and_namespaces_with_enclaves())
        loop_rate.sleep()  # commenting this line makes the callback work

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    global_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
