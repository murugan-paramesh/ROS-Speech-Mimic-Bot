#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import speech_recognition as sr

def speech_to_text():
    rospy.init_node('speech_listener', anonymous=True)
    pub = rospy.Publisher('/mimicbot/speech', String, queue_size=10)
    
    recognizer = sr.Recognizer()
    mic = sr.Microphone(device_index=0)
    
    while not rospy.is_shutdown():
        with mic as source:
            rospy.loginfo("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        
        try:
            text = recognizer.recognize_google(audio)
            rospy.loginfo(f"Recognized: {text}")
            pub.publish(text)
        except sr.UnknownValueError:
            rospy.logwarn("Could not understand the audio.")
        except sr.RequestError:
            rospy.logwarn("Speech recognition service unavailable.")

if __name__ == '__main__':
    try:
        speech_to_text()
    except rospy.ROSInterruptException:
        pass

