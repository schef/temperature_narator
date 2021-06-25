from machine import Pin
from time import sleep
import common
import logic

led = common.create_output(25)

if __name__ == "__main__":
    print("Boot sequence start")
    led.on()
    sleep(1)
    led.off()
    logic.init()
    print("Boot sequence end")
    while True:
        logic.loop()