# -*- coding: utf-8 -*-
import serial

"""
Python Interface for Massstream devices.

2010-2011 Robert Gieseke - robert.gieseke@gmail.com
See LICENSE.

Example usage:
    from massstream import Massstream
    # for a D-6310 at COM port 2
    # with max. flow rate of 1 ln/min and a value of 32000 representing 100%.
    massstream = Massstream('COM2', max_value=32000, max_volrate=1)

    print massstream.volrate()

Manual:
RS232 interface With FLOW-BUS protocol for digital
Mass Flow / Pressure instruments
"""

class Massstream(serial.Serial):
    def __init__(self, comport, max_value=32000, max_volrate=1):
        """
        Initialise Massstream.

            Example:
            # for a D-6310 at COM port 4
            # with max. flow rate of 1 ln/min and
            # a value of 32000 representing 100%.
            massstream = Massstream('COM2', max_value=32000, max_volrate=1)
        """
        serial.Serial.__init__(self, comport)
        self.baudrate = 38400
        self.bytesize = serial.EIGHTBITS
        self.parity = serial.PARITY_NONE
        self.stopbits = serial.STOPBITS_ONE
        self.timeout = 1
        self.max_value = max_value
        self.max_volrate = max_volrate

    def volrate(self):
        """
        Return volume rate in ln/min."""
        try:
            return self.max_volrate * self.value() / self.max_value
        except (ValueError, TypeError):
            return "NA"

    def value(self):
        """
        Return measured value, for example:
            Max.: 41942
            100% <=> 32000
        """
        self.write(':06030401210120\r\n')
        ans = self.read(17)
        try:
            return int(ans[11:15], 16)
        except ValueError:
            return "NA"
