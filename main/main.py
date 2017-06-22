#! /usr/bin/env python
# information Clerk Robot
# 2017-06-22 Masaki Yamamoto @ FabLab Kannai

# Import Python libraries
import time
import speek

#
# InfoClerkRobot
#
class InfoClerkRobot():
	NOTRACK = 0
	TRACKING = 0
	
	def getTrackingState(self):
		
	def cameraStart(self):

	def cameraStop(self):

# end of class

# main
print "start informationClerkRobot"
TIME_INTERVAL = 0.1 # 0.1 sec

# initialize
infoClerk = InfoClerkRobot()

infoClerk.cameraStart()

# endless loop
try:
	while True:
		trackingState = infoClerk.getTrackingState()	
		if trackingState == InfoClerkRobot.TRACKING:
			speek.speek('ファブラボかんないへようこそ')  
		elif trackingState == InfoClerkRobot.NOTRACK:		
		else:
		time.sleep(TIME_INTERVAL) 
except KeyboardInterrupt:
	pass 
# end of loop
infoClerk.cameraStop()

# end of main
