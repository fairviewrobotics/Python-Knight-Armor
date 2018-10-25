import enum

#types of ports
PortType = enum.Enum("PortType", "DIGITAL_IO PULSE_WIDTH_MODULATION")
#a class that registers ports and makes sure two subsytems don't use the same one
class _KnightPortyRegistryClass:

    class RIOPort:
        def __init__(self, portNum, portType, subsystem):
            self.portNum = portNum
            self.type = portType
            self.subsytem = subsystem

    def __init__(self):
        self.ports = []

    def register(self, portNumber, portType, subsystem):
        #check that the port isn't in use
        if any(port.portNum == portNumber for port in self.ports):
            raise Exception("Port number %i is already in use, but subsystem %s tried to register it" % (portNumber, subsystem))
        else:
            #add the port
            self.ports.append(self.RIOPort(portNumber, portType, subsystem))

#The singelton object
KnightPortyRegistry = _KnightPortyRegistryClass()


