## ROS Packages
This directory contains ROS packages related to our project. 

### Malicious ROS Packages
  * malpac - Has 4 packages in total. The "exercise*" packages are Vee's class assignments. These have been added for reference purposes. The more important node package is malpac. This is Dominic's first malicious package. It sends a value and gets added. There are 2 subscribers, so one essentally eavesdrops. In the same package, there is a redirect.py script that is able to kill another node.
	
  * malpac2 - This a basic ROS forkbomb. Running it spawns a bunch of clones of itself that does some rather unpleasant math. Currently gets my laptop's cpu to 100% usage of 2 cores in about 2 minutes, at which point I killed it. Run it with 'rosrun malpac2 bomb.py' after doing the regular sourcing.

  * malpac3 - This package disables all network interfaces and re-enables them after 5 seconds.
