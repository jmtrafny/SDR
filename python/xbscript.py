from digi.xbee.devices import XBeeDevice

device = XBeeDevice("/dev/ttyUSB0", 9600)
device.open()
device.send_data_broadcast("Hello World!")
device.close()