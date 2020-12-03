#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog

from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


left_motor = Motor(Port.D)
right_motor = Motor(Port.C)

robot = DriveBase(left_motor,right_motor,wheel_diameter=50, axle_track=90)

# Write your program here.
robot.straight(100)
robot.turn(90)
robot.straight(100)
robot.turn(90)
robot.straight(100)
robot.turn(90)
robot.straight(100)
robot.turn(90)
