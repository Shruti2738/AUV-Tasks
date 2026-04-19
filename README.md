AUV SOFTWARE SUBSYSTEM- TASKS

Overview
This repository contains my completed AUV Club recruitment ROS 2 assignment consisting of 4 tasks covering 2-way communication between 2 nodes, 3 node topic interactions with signal processing, position tracking with input movement and output direction, and computer vision object tracking.
All tasks were implemented, tested, and demonstrated as required.

Workspace Setup

Requirements
•	Ubuntu
•	ROS 2 installed
•	Python 3
•	colcon build tools
•	OpenCV (for Task 4)

Build Instructions:
cd ~/ros_ws
colcon build
source install/setup.bash

Task 1 – The Comm-Link (ROS 2 Pub/Sub)

Description
Implemented two ROS 2 nodes namely Invictus and Hawcker communicating through publisher/subscriber architecture.

Run

Terminal 1:
•	cd ~/ros_ws
•	colcon build
•	source install/setup.bash
•	ros2 run chat_pkg chat_node Hawcker

Terminal 2:
•	cd ~/ros_ws
•	colcon build
•	source install/setup.bash
•	ros2 run chat_pkg chat_node Invictus

Task 2 – Signal Processing Pipeline
Description
Implemented 3 nodes communicating through ROS 2 topics.

Run

Terminal 1:
•	cd ~/ros_ws
•	colcon build
•	source install/setup.bash
•	ros2 run chat_pkg raw_publisher

Terminal 2:
•	cd ~/ros_ws
•	colcon build
•	source install/setup.bash
•	ros2 run chat_pkg processor_node

Terminal 3:
•	cd ~/ros_ws
•	colcon build
•	source install/setup.bash
•	ros2 run chat_pkg output_node


Task 3 – Dead Reckoning System (Custom Interfaces)

Description
Implemented terminal-based inputs that update bot pose values dynamically using ROS 2 topics/custom messages.

Run

Terminal 1:
•	cd ~/ros_ws
•	colcon build
•	source install/setup.bash
•	ros2 run nav_pkg commander

Terminal 2:
•	cd ~/ros_ws
•	colcon build
•	source install/setup.bash
•	ros2 run nav_pkg navigator


Task 4 – Operation Visual Lock (Vision + FSM)

Description
Implemented webcam object tracking using a colored object. Filters/effects change depending on object position:
•	Left zone (left 1/3rd)- Grayscale Filter
•	Center zone (center 1/3rd) – Normal unfiltered video
•	Right zone (right 1/3rd) - Edge Detection (Canny) Filter
•	Off-screen- Negative Filter

Run on Terminal
•	cd ~/ros_ws
•	colcon build
•	source install/setup.bash
•	ros2 run vision_pkg visual_lock

Issues Faced During Development
•	ROS 2 executables were not detected initially due to incomplete setup.py configuration.
•	Python module import errors occurred in the navigation package and were resolved by correcting package structure.
•	The navigation task was improved by redesigning logic into a formal state machine.
•	Two-way chat communication initially failed because terminal input blocked message reception- it was fixed using Python threading.
•	Computer vision detection required tuning of color thresholds and screen-zone logic to reach close to perfect output.
•	Minor Python indentation and runtime errors were fixed throughout development.

Video Demonstration
The demonstration videos include:
•	Task 1: Two terminals communicating
•	Task 2: All 3 nodes simultaneously updating values 
•	Task 3: Terminal input (forward, backward, left, right)with changing bot_pose output
•	Task 4: Webcam object movement triggering filters

Submission
GitHub repository link and videos submitted through google form as required.

Author
Shruti Ravikumar
CS25B1001
