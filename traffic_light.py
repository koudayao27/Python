from machine import Pin
import time

button = Pin(14, Pin.IN, Pin.PULL_DOWN)

ledR = Pin(2, Pin.OUT)
ledY = Pin(3, Pin.OUT)
ledG = Pin(4, Pin.OUT)
blink = 0
ledR.off()
ledY.off()
ledG.off()

while True:
    ledY.off()
    ledR.on()
    if button.value():
        time.sleep(3)
        ledR.off()
        ledG.on()
        time.sleep(5)
        while blink < 20:
            ledG.toggle()
            blink += 1
            time.sleep(0.5)
        ledG.off()
        ledY.on()
        time.sleep(3)
