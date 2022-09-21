from time import sleep
from typing import List, Set
from digi.xbee.devices import XBeeDevice,XBeeNetwork,RemoteZigBeeDevice
from Remote import Remote
from digi.xbee.io import IOLine,IOValue

on_off = IOLine.DIO4_AD4
line_1 = IOLine.DIO12
line_2 = IOLine.DIO11_PWM1
line_3 = IOLine.DIO8
dim_lines = [line_1,line_2,line_3]
temperature = IOLine.DIO0_AD0
on = IOValue.HIGH
off = IOValue.LOW

class Coordinator:
    def __init__(self) -> None:
        self.local_device = XBeeDevice(baud_rate=9600,port="/dev/ttyUSB0")
        self.local_device.open()
        self.xbee_network : XBeeNetwork
        self.xbee_network = self.local_device.get_network()
        self.discover_nodes()

    def discover_nodes(self):
        self.nodes = []
        self.xbee_network.start_discovery_process()
        while self.xbee_network.is_discovery_running():
            sleep(0.1)
        for node in self.xbee_network.get_devices():
            print(node)
            try:
                self.nodes.append(Remote(node))
            except Exception as e:
                print(e.__class__)
                
    
    def print_nodes_info(self):
        for node in self.nodes:
            node.print_node_info()
    
    def light_on(self):
        for node in self.nodes:
            node.light_on()
    
    def light_off(self):
        for node in self.nodes:
            node.light_off()
    
    def dim_25(self):
        for node in self.nodes:
            node.dim_25()
    
    def dim_50(self):
        for node in self.nodes:
            node.dim_50()
    
    def dim_75(self):
        for node in self.nodes:
            node.dim_75()

    def dim_100(self):
        for node in self.nodes:
            node.dim_100()
    

    def print_current_temp(self):
        for node in self.nodes:
            node.getVal()
    
    
    
    

local = Coordinator()
while True:
    print(
        "1>Nodes Information",
        "2>Light ON",
        "3>Light OFF",
        "4>DIM 25",
        "5>DIM 50",
        "6>DIM 75",
        "7>DIM 100",
        "8>Temp Value",
        "9>Discover Nodes"
    )
    inp = int(input("Enter Number: "))
    if inp == 1:
        local.print_nodes_info()
    elif inp == 2:
        local.light_on()
    elif inp == 3:
        local.light_off()
    elif inp == 4:
        local.dim_25()
    elif inp == 5:
        local.dim_50()
    elif inp == 6:
        local.dim_75()
    elif inp == 7:
        local.dim_100()
    elif inp == 8:
        local.print_current_temp()
    elif inp == 9:
        local.discover_nodes()
    else:
        local.local_device.close()
        break
        
    

