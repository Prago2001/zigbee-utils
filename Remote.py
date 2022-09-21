from digi.xbee.devices import RemoteZigBeeDevice
from digi.xbee.io import IOLine,IOValue,IOMode


on_off = IOLine.DIO4_AD4
line_1 = IOLine.DIO12
line_2 = IOLine.DIO11_PWM1
line_3 = IOLine.DIO8
dim_lines = [line_1,line_2,line_3]
temperature = IOLine.DIO0_AD0
on = IOValue.HIGH
off = IOValue.LOW

class Remote(RemoteZigBeeDevice):
    
    def __init__(self,remote_device:RemoteZigBeeDevice):
        self.remote_device = remote_device
        self.pan_id = self.remote_device.get_64bit_addr()
        self.remote_device.set_io_configuration(temperature,IOMode.ADC)
        self.remote_device.set_io_configuration(on_off,IOMode.DIGITAL_OUT_LOW)
        for line in dim_lines:
            self.remote_device.set_io_configuration(line,IOMode.DIGITAL_OUT_LOW)
    
    def light_on(self):
        self.remote_device.set_dio_value(on_off,on)
    
    def light_off(self):
        self.remote_device.set_dio_value(on_off,off)

    def getVal(self):
            print(self.remote_device.get_adc_value(temperature))

    def dim_25(self):
        self.remote_device.set_dio_value(line_1,on)
        self.remote_device.set_dio_value(line_2,off)
        self.remote_device.set_dio_value(line_3,off)
    
    def dim_50(self):
        self.remote_device.set_dio_value(line_1,on)
        self.remote_device.set_dio_value(line_2,on)
        self.remote_device.set_dio_value(line_3,off)
    
    def dim_75(self):
        self.remote_device.set_dio_value(line_1,on)
        self.remote_device.set_dio_value(line_2,off)
        self.remote_device.set_dio_value(line_3,on)
    
    def dim_100(self):
        self.remote_device.set_dio_value(line_1,on)
        self.remote_device.set_dio_value(line_2,on)
        self.remote_device.set_dio_value(line_3,on)


    def print_line_value(self,line:IOLine):
        return self.remote_device.get_dio_value(line)
    
    def print_node_info(self):
        print(self.pan_id)
        print(f"{on_off}: {self.print_line_value(on_off)}")
        for line in dim_lines:
            print(f"{line} : {self.print_line_value(line)}")


    