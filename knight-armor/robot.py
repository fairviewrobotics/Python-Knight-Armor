#Main robot file
import wpilib

class Robot(wpilib.IterativeRobot):
    '''Main robot class'''

    def robotInit(self):
        '''Robot-wide initialization code should go here'''

        self.lstick = wpilib.Joystick(0)
        self.rstick = wpilib.Joystick(1)

        self.lr_motor = wpilib.Jaguar(1)
        self.rr_motor = wpilib.Jaguar(2)
        self.lf_motor = wpilib.Jaguar(3)
        self.rf_motor = wpilib.Jaguar(4)

        self.robot_drive = wpilib.RobotDrive(self.lf_motor, self.lr_motor,
                                             self.rf_motor, self.rr_motor)

        # Position gets automatically updated as robot moves
        self.gyro = wpilib.AnalogGyro(1)

    def disabled(self):
        '''Called when the robot is disabled'''
        while self.isDisabled():
            wpilib.Timer.delay(0.01)

    def autonomousPeriodic(self):
        '''Called when autonomous mode is enabled'''

        timer = wpilib.Timer()
        timer.start()

        while self.isAutonomous() and self.isEnabled():

            if timer.get() < 0.5:
                self.robot_drive.arcadeDrive(-1.0, 0.0)
            elif timer.get() < 1.0:
                self.robot_drive.arcadeDrive(-1.0, -0.7)
            else:
                self.robot_drive.arcadeDrive(0, 0)

            wpilib.Timer.delay(0.01)

    def teleopPeriodic(self):
        '''Called when operation control mode is enabled'''

        while self.isOperatorControl() and self.isEnabled():

            self.robot_drive.arcadeDrive(self.lstick.getY(), self.lstick.getX() * 0.7)

            wpilib.Timer.delay(0.04)


if __name__ == '__main__':
    wpilib.run(Robot, physics_enabled=True)
