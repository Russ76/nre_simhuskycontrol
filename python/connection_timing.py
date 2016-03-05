#!/usr/bin/env python
'''
How long does it take to make a connection in ROS
'''

import rospy
import visualization_msgs.msg
import time



def timeconnect():
    print "Testing Connetion Time"
    topic='visualization_marker'
    t1 = time.time()
    pub = rospy.Publisher(topic,visualization_msgs.msg.Marker,queue_size=10)
    t2 = time.time()
    while (pub.get_num_connections() < 1):
        pass
    te = time.time()
    print("%5.2f - %5.2f"%((te-t1)*1e3,(te-t2)*1e3))


rospy.init_node('pubmarker',anonymous=True,disable_signals=True)

timeconnect()

    
                          
