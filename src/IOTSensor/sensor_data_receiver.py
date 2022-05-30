#!/usr/bin/env python
import rospy
from ros_basics_tutorials.msg import IOTSensordata

def sensor_callback(message):
    #get_caller_id(): Get fully resolved name of local node
    rospy.loginfo("Received Sensor Data:\nSensor_id:%d\nSensor_name:%s\nTemparature:%f, Humidity:%f", message.id, message.Sensor_name, message.Temparature, message.Humidity)
    
def sensor_data_reception():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('Sensor_data_publisher', anonymous=True)

    rospy.Subscriber("Iot_sensor_topic", IOTSensordata, sensor_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    sensor_data_reception()