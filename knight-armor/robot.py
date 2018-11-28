#Main robot file
import wpilib, ctre
import wpilib.drive

import knight_armor


#A very incomplete drive train subsytem
class DriveTrain(knight_armor.KnightSubsystem):

    def __init__(self, emitter):
        super().__init__("DriveTrain")
        #add listener for controllign emitter
        emitter.addListener(self.recive)

        #claim ports
        self.claimPort(3, knight_armor.PortType.PULSE_WIDTH_MODULATION)
        self.claimPort(0, knight_armor.PortType.PULSE_WIDTH_MODULATION)
        #motors
        self.l_motor = ctre.WPI_TalonSRX(0)
        self.r_motor = ctre.WPI_TalonSRX(3)

        self.robot_drive = wpilib.drive.DifferentialDrive(self.l_motor, self.r_motor)

    def recive(self, msg):
        #currently arcadeDrive, but a more versatile driver should be implemented
        print("Speed: " + str(msg["speed"]) + ", Turn: " + str(msg["turn"]))
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
        DriveTrain(self.driveTrainEmitter)
        #register our joystick reciver
        self.joystick.addListener(self.receiveJoystick)

    def receiveJoystick(self, state):
        self.driveTrainEmitter.emit({"speed": state["leftStickY"] * -0.4, "turn": state["leftStickX"] * 0.4})

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
