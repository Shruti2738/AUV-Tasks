cmake_minimum_required(VERSION 3.8)
project(nav_pkg)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(std_msgs REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/BotPose.msg"
)

ament_export_dependencies(rosidl_default_runtime)

ament_package()

