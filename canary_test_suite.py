#!/usr/bin/python

import unittest
from canary_test_logic import connect_up, connect_down #import additional test logic functions

# Ethernet Tests
class EthTest(unittest.TestCase):

    def test_connect_up(self):
        file = open('/var/log/syslog')
        self.assertEquals(connect_up(file), True)


    def test_connect_down(self):
        file = open('/var/log/syslog')
        self.assertEquals(connect_down(file), True)

# === Additional Classes ===
# WifiTests
# CameraTests
# MicrophoneTests
# AmbientLightTests
# RealTimeStreamingProtocolTests
# HTTPLiveStreamingTests
# InfraredLEDTests
# RGBLEDTests
# SirenTests
# SpeakerTests

if __name__ == '__main__':
    unittest.main()
