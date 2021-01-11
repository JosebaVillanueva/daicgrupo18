import RPi.GPIO as GPIO
import time

def LeerFicherotxt():
    with open ('resultado.txt', 'r') as doc:
        contenido = doc.read()
        ComprobarMascarilla(contenido)
            
def EncenderAltavoz1():
    GPIO.setup(24, GPIO.OUT)
    pin_pwm2 = GPIO.PWM(24, 100)
    pin_pwm2.start(0)
    pin_pwm2.ChangeDutyCycle(35)
    input_value1 = 0
    while (input_value1 != 1):
        input_value1 = GPIO.input(5)
        if (input_value1 == 1):
            pin_pwm2.stop()
            break
    
def EncenderAltavoz2():
    GPIO.setup(18, GPIO.OUT)
    pin_pwm3 = GPIO.PWM(18, 100)
    pin_pwm3.start(0)
    pin_pwm3.ChangeDutyCycle(35)
    time.sleep(1)
    pin_pwm3.stop()
    
def EncenderVibrador():
    GPIO.setup(22, GPIO.OUT)
    pin_pwm1 = GPIO.PWM(22, 100)
    pin_pwm1.start(0)
    pin_pwm1.ChangeDutyCycle(50)
    time.sleep(3)
    pin_pwm1.stop()

def ComprobarID1():
    print("Introduzca su 1º ID:")
    nombre = input()
    if (nombre == "0008335430"):
        print("Introduzca su 2º ID:")
        ComprobarID2(nombre)
    elif (nombre == "0008293420"):
        print("Introduzca su 2º ID:")
        ComprobarID2(nombre)
    else:
        print("El codigo introducido no es valido!")
        ComprobarID1()

def ComprobarID2(nombre):
    if (nombre == "0008335430"):
        nombre1 = input()
        if (nombre1 == "0008293420"): 
            EncenderAltavoz2()
            time.sleep(1)
            EncenderAltavoz2()
        else:
            print("El código introducido no es valido!")
            ComprobarID1()
    elif (nombre == "0008293420"):
        nombre1 = input()
        if (nombre1 == "0008335430"): 
            EncenderAltavoz2()
            time.sleep(1)
            EncenderAltavoz2()
        else:
            print("El código introducido no es valido!")
            ComprobarID1()

def ComprobarMascarilla(estadoMascarilla):
    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    if (estadoMascarilla == "True"):
        EncenderAltavoz2()
        time.sleep(1)
        EncenderAltavoz2()
    else:
        EncenderAltavoz1()
        ComprobarID1()

def main():
    # Establecimiento del modo
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    #Inicializaciones
    GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    #Variables principales:
    input_value = 0
    
    print ("Para arrancar el coche pulse el botón")
          
    while input_value !=1:
        input_value = GPIO.input(26)
        if (input_value == 1):
            EncenderVibrador()
            print("Coche arrancado")
            break
    LeerFicherotxt()

    # Limpieza de estado
    GPIO.cleanup()

if __name__ == "__main__":
    main()

