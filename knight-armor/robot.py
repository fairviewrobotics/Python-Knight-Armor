#Main robot file
import wpilib

from knight_armor.knight_joystick import KnightJoystick

class Robot(wpilib.IterativeRobot):
    '''Main robot class'''

    def robotInit(self):
        '''Robot-wide initialization code should go here'''

        self.lr_motor = wpilib.Talon(1)
        self.rr_motor = wpilib.Talon(2)
        self.lf_motor = wpilib.Talon(3)
        self.rf_motor = wpilib.Talon(4)

        self.robot_drive = wpilib.RobotDrive(self.lf_motor, self.lr_motor,
                                             self.rf_motor, self.rr_motor)

        #Joystick object
        self.joystick = KnightJoystick(0)

        #register the joystick reciver
        self.joystick.addListener(lambda msg: self.joystick_drive(msg))

    def joystick_drive(self, state):
        self.robot_drive.arcadeDrive(state["leftStickY"], state["leftStickX"])

    def disabled(self):
        '''Called when the robot is disabled'''
        while self.isDisabled():
            wpilib.Timer.delay(0.01)

    def teleopPeriodic(self):
        '''Called when operation control mode is enabled'''

        while self.isOperatorControl() and self.isEnabled():

            self.joystick.update()




if __name__ == '__main__':
    wpilib.run(Robot, physics_enabled=True)
