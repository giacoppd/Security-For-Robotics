## malpac_ros ROS Package
Collection of Proof-of-concept packages intended to target ROS directly

### Proof of Concepts
Here are the various proof of concepts each script / package is attempting to show

#### Broken Authentication in ROS, using Publisher / Subscribers
  * ros1.py - PoC Broken Authentication 1 - Sets up a publisher on the attacker machine, and a subscriber on the victim machine. Showing that communication can occur between the two, without any authentication.

  * ros2.py - PoC Broken Authentication 2 - Sets up a publisher on the victim machine, and a subscriber on the attacker machine. Showing that communication can occur between the two, without any authentication.

#### Publisher / Subscriber Process Communication
  * ros3.py - Will pull all the active publishers and subscribers on the victim machine. All of the subscribers will be flooded with random data (fuzzing?), and all of the publishers will have their data logged for later review (maybe integrate with ROS bag?)

### Notes
  * These will be put into an actual ROS / catkin package at another time
