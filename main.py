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

#inicializa o sensor de cores (verificar o port no robo)
color_sensor = ColorSensor(Port.D)

#posiçao inicial do robo
x = 0
y = 0
posicao_robo = [x,y] #falta denotar os limites do tabuleiro ou seja o X onde sai e o Y onde sai e tals
coordenadas_paredes = []
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

    #pseudo codigo
    while True:
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

    #verifica a cor
    if(color_sensor.color() == Color.BLACK)
        #regista que aquela borda nao é uma parede e volta para o centro do quadrado

    else if (color_sensor.color() == Color.YELLOW) #(dps mudar para a cor q vamos usar tho nao tem mts q podemos usar)
        #regista a parede ou seja a sua posiçao atual de X Y passa a ser uma parede
        #como guardar as posiçoes atuais? possivelmente num array not sure
        #volta para o centro do quadrado
        robot.straight(-200) #a distancia do meio do quadrado ate a parte preta no lugar do 200