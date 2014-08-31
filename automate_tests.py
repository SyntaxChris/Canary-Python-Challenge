#!/usr/bin/python

# This is where all tests can be automated

import os

class FunctionalityTests:
    # define Ethernet runtest function
    def ethernet(self):
        print "Attempting to connect..."
        if os.system("python -m unittest canary_test_suite.EthTest.test_connect_up") == 0:
            print "Attempting to disconnect..."
            if os.system("python -m unittest canary_test_suite.EthTest.test_connect_down") == 0:
                print "Ethernet Test Successful!"

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
