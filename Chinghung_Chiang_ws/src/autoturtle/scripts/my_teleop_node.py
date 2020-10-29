#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

import os
import sys
import termios
import fcntl
#function : input without using enter
def getch():
  fd = sys.stdin.fileno()

  oldterm = termios.tcgetattr(fd)
  newattr = termios.tcgetattr(fd)
  newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
  termios.tcsetattr(fd, termios.TCSANOW, newattr)

  oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
  fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

  try:
    while 1:
      try:
        c = sys.stdin.read(1)
        break
      except IOError: 
	pass
  finally:
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
  return c

def my_teleop_node():
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
    rospy.init_node('my_teleop_node', anonymous=True)
    rate = rospy.Rate(10)
    print('w: forward, s: backward, a: rotate counterclockwise, d: rotate clockwise, ctrl+c will cease the process and press anykey to leave')
    while not rospy.is_shutdown():
        control_cmd=getch()
	move_cmd=Twist()
	#Linear speed in x in units/second: positive value implies forward/ negative value implies backward
	if control_cmd=='w':
	    move_cmd.linear.x=0.3
	elif control_cmd=='s':
	    move_cmd.linear.x=-0.3
	elif control_cmd=='a':
	    move_cmd.angular.z=0.5
	elif control_cmd=='d':
	    move_cmd.angular.z=-0.5
	else:
	    move_cmd.linear.x=0
	    move_cmd.angular.z=0
	pub.publish(move_cmd)
	rate.sleep()


if __name__=='__main__':
    try:
	my_teleop_node()
    except rospy.ROSInterruptException:
	pass
