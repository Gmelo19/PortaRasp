import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

PORTA3 = 37

GPIO.setup(PORTA3, GPIO.OUT)

try:
    
    GPIO.output(PORTA3, GPIO.LOW)
    print("Porta travada")
    time.sleep(2)
    
    GPIO.output(PORTA3, GPIO.HIGH)
    print("Porta Liberada")
    time.sleep(1)
    
except KeyboardInterrupt:
    GPIO.cleanup()