from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from dataclasses import dataclass 

class Pastor:
    def __init__(self,posicao,direcao): 
        self.posicao = posicao
        self.direcao = direcao

paredes = [] #array com as paredes 

ev3=EV3Brick()
encontrou_parede = 0
motor_esquerdo = Motor(Port.B)
motor_direito = Motor(Port.C)

sensor_toque = TouchSensor(Port.S1)
sensor_cor = ColorSensor(Port.S2)

robot = DriveBase(motor_esquerdo, motor_direito, wheel_diameter = 55.5, axle_tracker = 104)

informacao = Pastor(1,0)  #Informação sobre o robot

def adiciona_parede():
    x_parede = informacao.posicao
    if(informacao.direcao==0): # Virado para cima
        y_parede = x_parede + 6
    elif(informacao.direcao==90): # Virado para a direita
        y_parede = x_parede + 1
    elif(informacao.direcao==180): # Virado para baixo
        y_parede = x_parede - 6
    elif(informacao.direcao==270): # Virado para a esquerda
        y_parede = x_parede -1

    if(len(paredes)<6):
        paredes.append([x_parede,y_parede])


def andar():
    while(sensor_cor.color()== Color.WHITE):
        robot.drive(10,0)
    robot.stop()
    if(sensor_cor.color()==Color.BLACK): #Encontra limite do cacifo
        robot.straigh(20) #Anda até o centro do cacifo adjacente  $$$$$$$$$$$$$$$$$$$$ Verificar valor
        if(informacao.direcao==0):                          #Virado para cima
            informacao.posicao = informacao.posicao + 6
        elif(informacao.direcao==90):                       #Virado para a direita
            informacao.posicao = informacao.posicao + 1
        elif(informacao.direcao==180):                      #Virado para baixo
            informacao.posicao = informacao.posicao - 6
        elif(informacao.direcao==270):                      #Virado para a esquerda
            informacao.posicao = informacao.posicao - 1
    elif(sensor_cor.color()==Color.RED): #Encontra parede $$$$$$$$$$$$$$$$$$ Verificar cor
        encontrou_parede = 1;
        robot.straigh(-20) # Retorna ao centro do cacifo de onde saiu
       


def main():
    andar()
    if(encontrou_parede):
        adiciona_parede()
        encontrou_parede = 0


if __name__ == "__main__":
    main() 