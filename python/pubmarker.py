#!/usr/bin/env python
'''
Code for placing a goal marker in rviz
The function is the important part - the main function is just for testin.
'''

import rospy
import visualization_msgs.msg
from math import *
from time import sleep
from random import random


def mark(pos,size=[1.0,1.0,0.5],frame_id="/my_frame",topic='visualization_marker'):
    mm = visualization_msgs.msg.Marker()
    mm.header.frame_id = frame_id
    #mm.header.frame_id = "/odom"
    mm.header.stamp = rospy.Time.now()
    mm.ns = "basic_shapes"
    mm.id = 0
    mm.type = visualization_msgs.msg.Marker.CUBE
    mm.action = visualization_msgs.msg.Marker.ADD
    pos = list(pos)
    while len(pos)<3:
        pos.append(0.0)
    mm.pose.position.x = pos[0]
    mm.pose.position.y = pos[1]
    mm.pose.position.z = pos[2]
    mm.scale.x = size[0]
    mm.scale.y = size[1]
    mm.scale.z = size[2]
    mm.color.r = 0.0
    mm.color.g = 1.0
    mm.color.r = 0.0
    mm.color.a = 0.5
    mm.lifetime = rospy.Duration()
    pub = rospy.Publisher(topic,
                          visualization_msgs.msg.Marker,queue_size=10)
    cnt = 0
    cntthresh =10
    dt = 0.1
    # It seems to take 50-200 ms for the publisher to establish a connection
    while ( (pub.get_num_connections() < 1) and (cnt < cntthresh) ):
        sleep(dt)
        cnt += 1
    if cnt == cntthresh:
        print("marker timeout! nothing subscribed to <%s>"%topic)
    else:
        sleep(0.5) # still need to sleep a bit even after making a connection!
        pub.publish(mm)
        print("mark sent. %d"%cnt)

def main():
    rospy.init_node('pubmarker',anonymous=True)
    r = rospy.Rate(1)
    while not rospy.is_shutdown():
        mark([5*random(),5*random()],frame_id = "/odom")
        print('mark.')
        r.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
