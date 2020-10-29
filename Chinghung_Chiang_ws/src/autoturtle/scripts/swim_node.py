#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import random

x=0
y=0
the=0
def change(data):
    global x
    global y
    global the
    x=data.x
    y=data.y
    the=data.theta
    x=round(x,2)
    y=round(y,2)
    the=round(the,2)

def swim_node():
    rospy.init_node('swim_node', anonymous=True)
    sub = rospy.Subscriber('/turtle1/pose', Pose, change)
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
    
    rate = rospy.Rate(10)
    
    vel=round(random.uniform(0.3,0.4),1)
    angle=round(random.uniform(0.3,0.4),1)

    print 'start!'
    print 'linear velocity is ',vel
    print 'Angular velocity is ',angle
    while not rospy.is_shutdown():	
	move_cmd=Twist()
	move_cmd.linear.x=vel
	move_cmd.angular.z=angle
	if (x-5.54)**2<0.0002 and (y-5.54)**2<0.0002:
	    angle = -angle
	pub.publish(move_cmd)
	rate.sleep()


if __name__=='__main__':
    try:
	swim_node()
    except rospy.ROSInterruptException:
	pass
