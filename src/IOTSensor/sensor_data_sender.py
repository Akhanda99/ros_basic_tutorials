#!/usr/bin/env python
import rospy
from ros_basics_tutorials.msg import IOTSensordata
import random

def talker():
    #create a new publisher. we specify the topic name, then type of message then the queue size
    pub = rospy.Publisher('Iot_sensor_topic', IOTSensordata, queue_size=10)
    #we need to initialize the node
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'talker' node 
    rospy.init_node('Sensor_data_publisher', anonymous=True)
    #set the loop rate
    rate = rospy.Rate(1) # 1hz
    #keep publishing until a Ctrl-C is pressed
    i = 0
    while not rospy.is_shutdown():
        sensor_data=IOTSensordata()
        sensor_data.id=1
        sensor_data.Sensor_name="Temparature Sensor"
        sensor_data.Temparature=30.45 + (random.random()*2)
        sensor_data.Humidity=50.43 + (random.random()*1.4)
        
        rospy.loginfo(sensor_data)
        pub.publish(sensor_data)
        rate.sleep()
        i=i+1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass