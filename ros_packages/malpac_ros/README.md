## malpac_ros ROS Package
Collection of Proof-of-concept packages intended to target ROS directly

### Proof of Concepts
Here are the various proof of concepts each script / package is attempting to show

#### Broken Authentication in ROS, using Publisher / Subscribers
  * ros1.py - PoC Broken Authentication 1 - Sets up a publisher on the attacker machine, and a subscriber on the victim machine. Showing that communication can occur between the two, without any authentication.

  * ros2.py - PoC Broken Authentication 2 - Sets up a publisher on the victim machine, and a subscriber on the attacker machine. Showing that communication can occur between the two, without any authentication.

### Notes
  * These will be put into an actual ROS / catkin package at another time
