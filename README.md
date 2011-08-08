# Python Interface for Massstream Devices

2010-2011 Robert Gieseke - robert.gieseke@gmail.com

MIT license, see LICENSE.

### Example usage:
Example usage:
    from massstream import Massstream

    # for a D-6310 at COM port 2
    # with max. flow rate of 1 ln/min and a value of 32000 representing 100%.
    massstream = Massstream('COM2', max_value=32000, max_volrate=1)

    print massstream.volrate()

### Requirements:
pySerial - <http://pyserial.sourceforge.net/>

### Note
This has been developed using a D-6310 mass flow device, but should easily be
extended for other models.

### Manual for interface description:
RS232 interface With FLOW-BUS protocol for digital
Mass Flow / Pressure instruments
