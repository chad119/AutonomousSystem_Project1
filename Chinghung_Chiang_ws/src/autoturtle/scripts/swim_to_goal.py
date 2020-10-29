#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

x=0
y=0
the=0
def value(data):
    global x
    global y
    global the
    x=data.x
    y=data.y
    the=data.theta
    x=round(x,4)
    y=round(y,4)
    the=round(the,4)

def distance(goal_x,goal_y):
    error_pos = math.sqrt((goal_x-x)**2+(goal_y-y)**2)
    error_ang = math.atan2((goal_y-y),(goal_x-x))
    error_ang = error_ang-the
    if error_pos<0.5:
	error_pos=0
	error_ang=0
    return error_pos,error_ang

def swim_to_goal():
    goal_x=input('Please enter your x of your goal:')
    goal_y=input('Please enter your y of your goal:')
    rospy.init_node('swim_to_goal', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
    sub = rospy.Subscriber('/turtle1/pose', Pose, value)
    
    rate = rospy.Rate(10)
    print('start!')
    
    
    while not rospy.is_shutdown():
	move_cmd=Twist()
	pos,ang=distance(goal_x,goal_y)
	move_cmd.linear.x=pos*1.5
	move_cmd.angular.z=ang*4
	pub.publish(move_cmd)
        if pos==0 and ang==0:
	    goal_x=input('Please enter your x of your goal:')
    	    goal_y=input('Please enter your y of your goal:')
	    print('start!')
        rate.sleep()

if __name__=='__main__':
    try:
	swim_to_goal()
    except rospy.ROSInterruptException:
	pass
