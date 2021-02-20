#!/usr/bin/env python
import rospy
import random
from geometry_msgs.msg import Twist

def intoxicated_turtle():
    # Starts a new node
    rospy.init_node('intoxicated_turtle', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    while not rospy.is_shutdown():
        vel_msg = Twist()
        vel_msg.linear.x = random.uniform(0.0,2.0)
        vel_msg.angular.z = random.uniform(-5.0,5.0)
        vel_msg.linear.y = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.linear.z = 0

        #Publish the velocity
        velocity_publisher.publish(vel_msg)
        rospy.Rate(10).sleep()


if __name__ == '__main__':
    try:
        #Testing our function
        intoxicated_turtle()
    except rospy.ROSInterruptException: pass