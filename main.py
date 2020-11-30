#!/usr/bin/env python3
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

#inicializacao dos motores
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Write your program here.
ev3.speaker.beep()

#drive base 
roboot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
#verificar as medidas das rodas 


while True:
    int ovelhas 
    #anda a 200milimetros por segundo
    robot.drive(200, 0)

        while obstacle_sensor.distance() > 300:
            wait(10)
            ev3.speaker.beep()
            ovelhas++;
    
    #robot anda para tras 200mm
    robot.straight(-200)
    #vira 90 graus para verificar a sua direita
    robot.turn(90)
     #blabla