import machine
import time 
from machine import Pin, PWM

# Configuración de los pines para el motor del eje X
pin1_X = machine.Pin(4, machine.Pin.OUT)
pin2_X = machine.Pin(5, machine.Pin.OUT)
pin3_X = machine.Pin(6, machine.Pin.OUT)
pin4_X = machine.Pin(7, machine.Pin.OUT)

# Configuración de los pines para el motor del eje Y
pin1_Y = machine.Pin(0, machine.Pin.OUT)
pin2_Y = machine.Pin(1, machine.Pin.OUT)
pin3_Y = machine.Pin(2, machine.Pin.OUT)
pin4_Y = machine.Pin(3, machine.Pin.OUT)

#Se configura el Pin 8 para el servo que controla el eje Z
servoZ = PWM(Pin(8))
servoZ.freq(50) #T=20ms

#Se crea una variable button y se configura en el Pin 9
#como una entrada y con resistencia de Pull Up
button1 = Pin(9, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(10, Pin.IN, Pin.PULL_DOWN)

#Función para mapear en eje Z
def map(x):
    return int((x-0) * (2500000-500000) / (180-0) + 500000)

#Función para los grados del Servo en Z
def grs(grados):
    m = map(0)
    servoZ.duty_ns(m)
    time.sleep(0.1) #Tiempo entre cada sentido
    m = map(grados)
    servoZ.duty_ns(m)
    time.sleep(0.0001)

# Secuencia de pasos para el motor paso a paso en sentido horario
secuencia_pasos = [
    [1, 0, 1, 0],  # Paso 1
    [0, 1, 1, 0],  # Paso 2
    [0, 1, 0, 1],  # Paso 3
    [1, 0, 0, 1]   # Paso 4
]

# Secuencia de pasos para el motor paso a paso en sentido antihorario
secuencia_pasos_antihorario = [
    [1, 0, 0, 1],  # Paso 1
    [0, 1, 0, 1],  # Paso 2
    [0, 1, 1, 0],  # Paso 3
    [1, 0, 1, 0]   # Paso 4
]


# Función para avanzar un paso en el eje X en sentido horario
def avanzar_X_sentido_horario():
    for paso in secuencia_pasos:
        pin1_X.value(paso[0])
        pin2_X.value(paso[1])
        pin3_X.value(paso[2])
        pin4_X.value(paso[3])
        time.sleep(0.001)  # Retardo entre pasos

# Función para avanzar un paso en el eje Y en sentido horario
def avanzar_Y_sentido_horario():
    for paso in secuencia_pasos:
        pin1_Y.value(paso[0])
        pin2_Y.value(paso[1])
        pin3_Y.value(paso[2])
        pin4_Y.value(paso[3])
        time.sleep(0.001)  # Retardo entre pasos

# Función para avanzar un paso en el eje X en sentido antihorario
def avanzar_X_sentido_antihorario():
    for paso in secuencia_pasos_antihorario:
        pin1_X.value(paso[0])
        pin2_X.value(paso[1])
        pin3_X.value(paso[2])
        pin4_X.value(paso[3])
        time.sleep(0.001)  # Retardo entre pasos

# Función para avanzar un paso en el eje Y en sentido antihorario
def avanzar_Y_sentido_antihorario():
    for paso in secuencia_pasos_antihorario:
        pin1_Y.value(paso[0])
        pin2_Y.value(paso[1])
        pin3_Y.value(paso[2])
        pin4_Y.value(paso[3])
        time.sleep(0.001)  # Retardo entre pasos

# Función para mover la plataforma en el eje X en sentido horario
def mover_plataforma_X_sentido_horario(pasos):
    for _ in range(pasos):
        avanzar_X_sentido_horario()

# Función para mover la plataforma en el eje Y en sentido horario
def mover_plataforma_Y_sentido_horario(pasos):
    for _ in range(pasos):
        avanzar_Y_sentido_horario()

# Función para mover la plataforma en el eje X en sentido antihorario
def mover_plataforma_X_sentido_antihorario(pasos):
    for _ in range(pasos):
        avanzar_X_sentido_antihorario()

# Función para mover la plataforma en el eje Y en sentido antihorario
def mover_plataforma_Y_sentido_antihorario(pasos):
    for _ in range(pasos):
        avanzar_Y_sentido_antihorario()

# Función para mover la plataforma completa
#nveces = Número de veces que se quiere mover la plataforma.
def mover_Simulador(nveces):
    for _ in range(nveces):
        #Mover Eje X a la derecha
        mover_plataforma_X_sentido_antihorario(62)
        #Mover Eje Y hacia arriba
        mover_plataforma_Y_sentido_antihorario(51)
        #Mover Eje X a la izquierda
        mover_plataforma_X_sentido_horario(60)
        #Mover Eje Y hacia abajo
        mover_plataforma_Y_sentido_horario(51)
        
        #Detener el motor del eje X
        pin1_X.value(0)
        pin2_X.value(0)
        pin3_X.value(0)
        pin4_X.value(0)

        # Detener el motor del eje Y
        pin1_Y.value(0)
        pin2_Y.value(0)
        pin3_Y.value(0)
        pin4_Y.value(0)
        
        #Mover eje Z
        grs(90)

def mover_SimuladorOsc(nveces):
    for _ in range(nveces):
        #Mover Eje X a la derecha
        mover_plataforma_X_sentido_antihorario(62)
        #Mover Eje Y hacia arriba
        mover_plataforma_Y_sentido_antihorario(51)
        #Mover Eje X a la izquierda
        mover_plataforma_X_sentido_horario(60)
        #Mover Eje Y hacia abajo
        mover_plataforma_Y_sentido_horario(51)
        
        #Detener el motor del eje X
        pin1_X.value(0)
        pin2_X.value(0)
        pin3_X.value(0)
        pin4_X.value(0)

        # Detener el motor del eje Y
        pin1_Y.value(0)
        pin2_Y.value(0)
        pin3_Y.value(0)
        pin4_Y.value(0)

# Se crea una condición para hacer mover el simulador una vez se apriete
# un push button
while True:
    if button1.value():
        mover_Simulador(8)
    if button2.value():
        mover_SimuladorOsc(10)

