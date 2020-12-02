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

#inicializacao dos sensores 
touch_sensor = TouchSensor(Port.S1)
color_sensor = ColorSensor(Port.S2)

# Write your program here.
#ev3.speaker.beep()

#drive base 
roboot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
#verificar as medidas das rodas 


def ovelhas():
    int ovelhas
    while obstacle_sensor.distance() < 300:
        wait(10)
        ev3.speaker.beep()
        ovelhas += 1

def run():
    while True:
        cor = color_sensor.color()
        int limites_cacifo
        int parede

        #anda a 200milimetros por segundo
        robot.drive(200, 0)
        #enquanto nao verificou os 4 limites de um cacifo
        while (limites_cacifo != 4):
            #verifica a cor do limite, se for preto, nao tem parede
            if (cor = Color.BLACK):
                ovelhas()
                #robot anda para tras 200mm
                robot.straight(-200)
                limites_cacifo += 1
                #vira 90 graus para verificar a sua direita
                robot.turn(90)
        
            elif (cor = Color.BLUE): #ESCOLHER CORES PRIMARIAS PARA SER MAIS FACIL O ROBO IDENTIFICAR
                ovelhas()
                robot.straight(-200)
                parede += 1
                robot.turn(90)
            
            else:



            
