## malpac_ros ROS Package
Collection of Proof-of-concept packages intended to target ROS directly

### Proof of Concepts
Here are the various proof of concepts each script / package is attempting to show

#### Broken Authentication in ROS, using Publisher / Subscribers
  ![ROS PoC](https://raw.githubusercontent.com/ZachR0/Security-For-Robotics/master/ros_packages/malpac_ros/documentation/POC_auth_proof.png)
  * ros1.py - PoC Broken Authentication 1 - Sets up a publisher on the attacker machine, and a subscriber on the victim machine. Showing that communication can occur between the two, without any authentication.

  * ros2.py - PoC Broken Authentication 2 - Sets up a publisher on the victim machine, and a subscriber on the attacker machine. Showing that communication can occur between the two, without any authentication.

#### Process Communication (Publisher / Subscriber Model)
    ![ROS PoC](https://raw.githubusercontent.com/ZachR0/Security-For-Robotics/master/ros_packages/malpac_ros/documentation/ros_fuzz_1.png)
    ![ROS PoC](https://raw.githubusercontent.com/ZachR0/Security-For-Robotics/master/ros_packages/malpac_ros/documentation/ros_fuzz_2.png)
  * ros3.py - Will pull all the active subscribers on the victim machine; All of the subscribers will be flooded with random data (Basiclly a ROS Fuzzy Tester)
  Might be able to integrate with american fuzzy lop (http://lcamtuf.coredump.cx/afl/)

  * ros4.py - Will pull all active publishers on the victim machine; all of the publishers will have their data logged for later review (maybe integrate with ROS bag?)


### Other PoC Ideas
  * Figure out way to install ROS packages on victim machine from an attacker machine -- Doing this will allow us to push our own malicious packages remotely.
  * ROS Shell Package - uses the Publisher / Subscriber model to allow for a Linux shell on the victim machine.
  * More to come...

### Notes
  * These will be put into an actual ROS / catkin package at another time
