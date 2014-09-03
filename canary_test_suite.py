#!/usr/bin/python
import unittest
from canary_test_logic import connect_up, connect_down #import additional test logic functions
# Ethernet Tests
class EthTest(unittest.TestCase):
    def test_connect_up(self):
        with open('/var/log/syslog') as f:
          self.assertEquals(connect_up(f), True)
    def test_connect_down(self):
        with open('/var/log/syslog') as f:
          self.assertEquals(connect_down(f), True)

if __name__ == "__main__":
    while 1:
        run_tests = raw_input("This is the test suite. Run automated tests? (y/n) ")
        if run_tests == 'y':
            execfile('automate_tests.py')
            break
        elif run_tests == 'n':
            sys.exit()
            break

# === Additional Classes ===
# class WifiTests
# class CameraTests
# class MicrophoneTests
# class AmbientLightTests
# class RealTimeStreamingProtocolTests
# class HTTPLiveStreamingTests
# class InfraredLEDTests
# class RGBLEDTests
# class SirenTests
# class SpeakerTests
