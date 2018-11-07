import wpilib.command

from knight_armor.knight_port_registry import KnightPortyRegistry

class KnightSubsystem(wpilib.command.Subsystem):
    #all registered subsystem names
    allSubsystemNames = []

    #register the subsytem name
    def __init__(self, name):
        self.name = name
        if name in KnightSubsystem.allSubsystemNames:
            raise Exception("Subsystem name " + self.name + " is already in use.")
        KnightSubsystem.allSubsystemNames.append(self.name)

    #claim a port with KnightPortRegistry
    def claimPort(self, port, portType):
        KnightPortyRegistry.register(port, portType, self.name)