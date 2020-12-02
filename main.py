#!/usr/bin/env python3
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,InfraredSensor, UltrasonicSensor, GyroSensor)
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



#posiçao inicial do robo
int x = 0
int y = 0
posicao_robo = [x,y] #falta denotar os limites do tabuleiro ou seja o X onde sai e o Y onde sai e tals
coordenadas_paredes = [] #vai conter arrays com 2 inteiros cada, representando o X e Y das paredes

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


        robo.straight(200) #andou 200 no sentido positivo do eixo do Y
        posicao_robo[1] = posicao_robo[1] + 200
        #encontra cor preta ou parede e regista
        robo.straight(-200)
        posicao_robo[1] = posicao_robo[1] - 200
        #vira para a direita e anda no sentido positivo do eixo do X
        robo.turn(90)
        robo.straight(200)
        posicao_robo[0] = posicao_robo[0] + 200
        #encontra cor preta ou parede e regista
        posicao_robo[0] = posicao_robo[0] - 200
        #repete o acima no sentido negativo de X e Y (ou seja vira mais 90 graus anda 200 e a posicao no eixo do Y passa a ser o q era -200 blah blah)
        #como registar as paredes para o robo se lembrar? podemos guardar a posiçao X e Y da parede mas vamos guardar essas posiçoes onde?
        #podemos ter um array de arrays que guarda as paredes maybe
        #integrar a verificaçao das cores, o python tem mains? dava jeito ser outra funçao separada


        #anda a 200milimetros por segundo
        robot.drive(200, 0)
        #enquanto nao verificou os 4 limites de um cacifo
        while (limites_cacifo != 4):
            #verifica a cor do limite, se for preto, nao tem parede
            if (cor == Color.BLACK):
                ovelhas()
                #robot anda para tras 200mm
                robot.straight(-200)
                limites_cacifo += 1
                #vira 90 graus para verificar a sua direita
                robot.turn(90)
        
            elif (cor == Color.YELLOW): 
                #regista a parede ou seja a sua posiçao atual de X Y passa a ser uma parede
                ovelhas()
                robot.straight(-200)
                #volta para o centro do quadrado
                parede += 1
                robot.turn(90)
            
            else:



            


