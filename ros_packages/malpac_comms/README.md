## malpac_comms ROS Package
The purpose of this package is to compromise communications on a ROS based system. There will be several
methods enclosed in this "package", which will be described as they are developed.

### Methods
  * nc_drop.py -- Netcat Backdoor Service Dropper. Will attempt to spin up netcat as a background process,
  accepting incoming connections across any available communication interfaces.

  Netcat will attempt to be ran if it is already on the system, or will try to run / compile a copy of Netcat
  in memory, at run time.

### Notes
  * These will be put into an actual ROS / catkin package at another time
