#include <chrono>
#include <functional>
#include <memory>
#include <string>
#include <iostream>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/u_int64.hpp"

class MinimalPublisher : public rclcpp::Node {

public:

  MinimalPublisher() : Node("timeCpp_publisher") {
    publisher_ = this->create_publisher<std_msgs::msg::UInt64>("tiempoCpp", 1);
    timer_ = this->create_wall_timer(std::chrono::milliseconds(500), std::bind(&MinimalPublisher::timer_callback, this));
  }

private:

  // LLamando el reloj del sistema a trabes de C++
  inline uint64_t timeMicrosecons() {
    return std::chrono::round<std::chrono::microseconds>(std::chrono::system_clock::now().time_since_epoch()).count();
  }
  
  // Llamando al relog de ROS
  //std::cout << "** now(): " << std::fixed << now().seconds() << std::endl;

  void timer_callback() {
    std_msgs::msg::UInt64 message;
    message.data = timeMicrosecons();
    //message.data = now().seconds();
    std::cout << "tiempo: " << message.data << std::endl;
    //std::cout << "** now(): " << std::fixed << now().seconds() << std::endl;
    //RCLCPP_INFO(this->get_logger(), "Publishing: %lu", message.data);
    publisher_->publish(message);
  }
  
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<std_msgs::msg::UInt64>::SharedPtr publisher_;

};

int main(int argc, char * argv[]){
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalPublisher>());
  rclcpp::shutdown();
  return 0;
}
