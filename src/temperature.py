import machine
import onewire
import ds18x20
import common

ds_pin = machine.Pin(22)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
roms = ds_sensor.scan()
read_timestamp = common.get_millis()
read_timeout = 1000
temperature = -100.0
temperature_callback = None
temperature_callback_timestamp = 0
temperature_callback_timeout = 10000

def get_temperature():
    ds_sensor.convert_temp()
    for rom in roms:
        return(ds_sensor.read_temp(rom))
        
def register_temperature_callback(callback):
    global temperature_callback
    temperature_callback = callback
        
def loop():
    global read_timestamp, temperature, temperature_callback_timestamp
    if (common.millis_passed(read_timestamp) >= read_timeout):
        read_timestamp = common.get_millis()
        new_temperature = get_temperature()
        print("temperature read: %f" % (new_temperature))
        if (abs(temperature - new_temperature) >= 1.0) or (int(temperature) != int(new_temperature) and common.millis_passed(temperature_callback_timestamp) >= temperature_callback_timeout):
            print("temperature change %f->%f" % (temperature, new_temperature))
            temperature_callback_timestamp = common.get_millis()
            temperature = new_temperature
            if temperature_callback:
                temperature_callback(int(temperature))
                
def loop_test():
    while True:
        loop()