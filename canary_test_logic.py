#!/usr/bin/python
import subprocess, sys, time

def time_now():
  if time.strftime("%d")[0] == '0':
    day = time.strftime("%d")[1]
    return time.strftime("%b  {0} %H:%M:%S".format(day))
  else:
    return time.strftime("%b %d %H:%M:%S")
# Ethernet connect test: Could check additional connection logs and implement counter
# once counter reaches desired number of log checks, return true
def connect_up(syslog):
    subprocess.call("sudo ifconfig eth0 up", shell=True)
    while 1:
        where = syslog.tell()
        line = syslog.readline()
        if not line:
            syslog.seek(where)
        else:
            if time_now() in line:
                if "NetworkManager state is now CONNECTED_GLOBAL" in line:
                    return True
                    break

def connect_down(syslog):
    subprocess.call('sudo ifconfig eth0 down', shell=True)
    while 1:
        where = syslog.tell()
        line = syslog.readline()
        if not line:
            syslog.seek(where)
        else:
            if time_now() in line:
                if "NetworkManager state is now DISCONNECTED" in line:
                    return True
                    break

if __name__ == "__main__":
    run_tests = raw_input("This is the test logic file. Run automated tests instead? (y/n) ")
    while 1:
      if run_tests == 'y':
        execfile('automate_tests.py')
        break
      elif run_tests == 'n':
        sys.exit()
        break
      else:
        run_tests = raw_input("please choose: y or n ")

#=== OUTLINE ===

# Wifi Tests
    # similar implementation as ethernet
    # check syslog for keyword "ath0"
    # test functionality with mobile app

#SSH/Serial Console Tests
    # check for connection log on port assigned to SSH ex: "connection from 128.11.22.33 port 1022"
    # search for logs with 'RSA', 'SSH1', 'SSH2', 'OpenSSH'
    # varify in logs that RSA key generation complete
    # send data via SSH to test functionality

# Camera Tests
    # activate port where camera is assigned to
    # check for video logs on assigned port
    # check recorded video files for quality and functionality
    # print to console with an input for confirmation

# Microphone Tests
    # activate port that microphone is assigned to
    # varify with scope that microphone is picking up sound waves
    # test edge cases making sure microphone is not distorting and
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
    # confirm that Canary is communicating with app by monitoring server and checking database for changes

# Infrared LED Tests
    # activate port that LEDs are assigned to
    # visually inspect for LED functionality
    # check video functionality with LED's
    # print to console with an input for confirmation

# RGB LED Tests
    # activate port that LED is assinged to
    # vary voltage/current on port to change LED colors
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
