import machine
import onewire
import ds18x20
import common

ds_pin = machine.Pin(22)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
roms = ds_sensor.scan()
read_timestamp = common.get_millis()
read_timeout = 1000
temperature = -100
temperature_callback = None

def get_temperature():
    ds_sensor.convert_temp()
    for rom in roms:
        return(ds_sensor.read_temp(rom))
        
def register_temperature_callback(callback):
    global temperature_callback
    temperature_callback = callback
        
def loop():
    global read_timestamp, temperature
    if (common.millis_passed(read_timestamp) >= read_timeout):
        read_timestamp = common.get_millis()
        new_temperature = get_temperature()
        print("temperature read: %f" % (new_temperature))
        if temperature != int(new_temperature):
            print("temperature change %d->%d" % (temperature, new_temperature))
            temperature = int(new_temperature)
            if temperature_callback:
                temperature_callback(temperature)
                
def loop_test():
    while True:
        loop()