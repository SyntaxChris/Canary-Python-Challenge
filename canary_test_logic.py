#!/usr/bin/python

import time, os

# Ethernet connect test: Could check additional connection logs and implement counter
# once counter reaches desired number of checks, return true
def connect_up(syslog):
    os.system("sudo ifconfig eth0 up")
    while 1:
        where = syslog.tell()
        line = syslog.readline()
        if not line:
            syslog.seek(where)
        else:
            if "{0}".format(time.strftime("%b %d %H:%M:%S")) in line:
                if "NetworkManager state is now CONNECTED_GLOBAL" in line:
                    return True
                    break

def connect_down(syslog):
    os.system('sudo ifconfig eth0 down')
    while 1:
        where = syslog.tell()
        line = syslog.readline()
        if not line:
            syslog.seek(where)
        else:
            if "{0}".format(time.strftime("%b %d %H:%M:%S")) in line:
                if "NetworkManager state is now DISCONNECTED" in line:
                    return True
                    break


#=== OUTLINE ===

# Wifi Tests
    # similar implementation as ethernet
    # check syslog for keyword "ath0"
    # test functionality with mobile app

# Camera Tests
    # activate port where camera is assigned to
    # check for video logs on assigned port
    # check recorded video files for quality and functionality
    # print to console with an input for confirmation

# Microphone Tests
    # activate port that microphone is assigned to
    # varify with scope that microphone is picking up sound waves
    # test edge cases making sure microphon is not distorting and
    # can pick up low level sound waves
    # print to console with an input for confirmation

# Ambient Light Tests
    # activate lights and print to console an input for confirmation

# Real Time Streaming Protocol Tests
    # activate video via app and check syslog for keyword "vlc"
    # test functionality of video with mobile app
    # print to console with an input for confirmation

# HTTP Live Streaming Tests
    # make GET and POST requests to server via httplib
    # monitor and GET and POST requests in syslog
    # confirm in log that requests made from mobile app are present

# Infrared LED Tests
    # activate port that LEDs are assigned to
    # visually inspect for LED functionality
    # check video functionality with LED's
    # print to console with an input for confirmation

# RGB LET Tests
    # activate port that LED is assinged to
    # vary voltage on port to change LED colors
    # visually inspect for color variation
    # print to console with an input for confirmation

# Siren Tests
    # activate/deactivate port that siren is assigned to
    # use mobile app to activate and deactivate siren

# Speaker Tests
    # activate/deactivate port that speaker is assigned to
    # use mobile app to activate and deactivate speaker
    # check that speaker doesn't destort at high output
    # print to console with an input for confirmation
