from knight_armor.knight_emitter import KnightEmitter
import wpilib

#Knight
class KnightJoystick(KnightEmitter):
    #port is the port xbox controller is on
    def __init__(self, port):
        KnightEmitter.__init__(self)
        self.joystick = wpilib.XboxController(port)
        #methods to check for updates
        self.stateGetters = {
            "leftStickX": lambda: self.joystick.getX(0), "leftStickY" : lambda: self.joystick.getY(0),
            "rightStickX": lambda: self.joystick.getX(1), "rightStickY": lambda: self.joystick.getY(1),

            #self.joystick.getAButton, self.joystick.getBButton, self.joystick.getBackButton, self.joystick.getStartButton,
            #lambda: self.joystick.getStickButton(0), lambda: self.joystick.getStickButton(1),
            #lambda: self.joystick.getBumper(0), lambda: self.joystick.getBumper(1),
            #lambda: self.joystick.getTriggerAxis(0), lambda: self.joystick.getTriggerAxis(1)
            }
        #values of the
        self.controlState = {
            "leftStickX": 0.0, "leftStickY" : 0.0,
            "rightStickX": 0.0, "rightStickY": 0.0
        }

    #check for changes and update
    def update(self):
        for control in self.stateGetters:
            self.controlState[control] = self.stateGetters[control]()
        #send if a change occured
        self.emit(self.controlState)


