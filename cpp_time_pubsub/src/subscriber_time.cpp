#include <chrono>
#include <functional>
#include <memory>
#include <iostream>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/u_int64.hpp"

class MinimalSubscriber : public rclcpp::Node{

public:
  MinimalSubscriber() : Node("timeCpp_subscriber") {
    subscription_ = this->create_subscription<std_msgs::msg::UInt64>("tiempoCpp", 1, std::bind(&MinimalSubscriber::topic_callback, this, std::placeholders::_1));
  }

private:
  
  inline uint64_t timeMicrosecons() {
    return std::chrono::round<std::chrono::microseconds>(std::chrono::system_clock::now().time_since_epoch()).count();
  }
  
  void topic_callback(const std_msgs::msg::UInt64 & msg) {
    uint64_t ahora = timeMicrosecons();
    float dif = (ahora - msg.data ) / 1000.0;
    std::cout << "Tiempo: [" << ahora << " - " << msg.data << " = ] " << dif << std::endl;
    //RCLCPP_INFO(this->get_logger(), "I heard: '%lu'", msg.data);
  }
  
  rclcpp::Subscription<std_msgs::msg::UInt64>::SharedPtr subscription_;

};

int main(int argc, char * argv[]) {
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalSubscriber>());
  rclcpp::shutdown();
  return 0;
}
