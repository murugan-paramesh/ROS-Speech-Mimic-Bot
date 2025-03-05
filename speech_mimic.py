#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def callback(msg):
    rospy.loginfo(f"Mimicking: {msg.data}")
    speak(msg.data)

def speech_mimic():
    rospy.init_node('speech_mimic', anonymous=True)
    rospy.Subscriber('/mimicbot/speech', String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        speech_mimic()
    except rospy.ROSInterruptException:
        pass

