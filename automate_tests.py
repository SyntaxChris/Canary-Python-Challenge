#!/usr/bin/python
import os
# This is where all tests can be automated
class FunctionalityTests:
    # define Ethernet runtest function
    def ethernet(self):
        print "===== Running Ethernet Tests ====="
        print "Attempting to connect..."
        if subprocess.call("python -m unittest canary_test_suite.EthTest.test_connect_up", shell=True) == 0:
            print "Attempting to disconnect..."
            if subprocess.call("python -m unittest canary_test_suite.EthTest.test_connect_down", shell=True) == 0:
                print "==== Ethernet Tests Successful! ===="

    # define Wifi runtest function
    # define Camera runtest function
    # define Microphone runtest function
    # define Ambient Light runtest function
    # define Temperature runtest function
    # define RTSP runtest function
    # define HLS runtest function
    # define IR LED runtest function
    # define RGB LED runtest function
    # define Siren runtest function
    # define Speaker runtest function
if __name__ == "__main__":
    FunctionalityTests().ethernet()
    #FunctionalityTests().camera()
    #FunctionalityTests().wifi()
    #FunctionalityTests().microphone()
    #FunctionalityTests().amb_light()
    #FunctionalityTests().temperature()
    #FunctionalityTests().rstp()
    #FunctionalityTests().hls()
    #FunctionalityTests().ir_led()
    #FunctionalityTests().rgb_led()
    #FunctionalityTests().siren()
    #FunctionalityTests().speaker()
