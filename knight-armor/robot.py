#Main robot file
import wpilib

import knight_armor


#A very incomplete drive train subsytem
class DriveTrain(knight_armor.KnightSubsystem):

    def __init__(self, emitter):
        super().__init__("DriveTrain")
        #add listener for controllign emitter
        emitter.addListener(self.recive)

        #claim ports
        self.claimPort(1, knight_armor.PortType.PULSE_WIDTH_MODULATION)
        self.claimPort(2, knight_armor.PortType.PULSE_WIDTH_MODULATION)
        self.claimPort(3, knight_armor.PortType.PULSE_WIDTH_MODULATION)
        self.claimPort(4, knight_armor.PortType.PULSE_WIDTH_MODULATION)
        #motors
        self.lr_motor = wpilib.Talon(1)
        self.rr_motor = wpilib.Talon(2)
        self.lf_motor = wpilib.Talon(3)
        self.rf_motor = wpilib.Talon(4)

        self.robot_drive = wpilib.RobotDrive(self.lf_motor, self.lr_motor,
                                             self.rf_motor, self.rr_motor)

    def recive(self, msg):
        #currently arcadeDrive, but a more versatile driver should be implemented
        self.robot_drive.arcadeDrive(msg["speed"], msg["turn"])


#example subsystem
class MainSubsystem(knight_armor.KnightSubsystem):
    def __init__(self):
        super().__init__("MainSubsystem")
        #Joystick object
        self.joystick = knight_armor.KnightJoystick(0)
        #emitter for drive train subsytem
        self.driveTrainEmitter = knight_armor.KnightEmitter()
        #drive train subsytem
        self.driveTrain = DriveTrain(self.driveTrainEmitter)

        #register our joystick reciver
        self.joystick.addListener(self.receiveJoystick)

    def receiveJoystick(self, state):
        self.driveTrainEmitter.emit({"speed": state["leftStickY"] * -0.5, "turn": state["leftStickX"] * 0.5})

    def run(self):
        self.joystick.update()

class Robot(wpilib.IterativeRobot):
    '''Main robot class'''

    def robotInit(self):
        '''Robot-wide initialization code should go here'''
        self.sub = MainSubsystem()

    def disabled(self):
        '''Called when the robot is disabled'''
        while self.isDisabled():
            wpilib.Timer.delay(0.01)

    def teleopPeriodic(self):
        '''Called when operation control mode is enabled'''
        while self.isOperatorControl() and self.isEnabled():
            self.sub.run()

if __name__ == '__main__':
    wpilib.run(Robot, physics_enabled=True)
