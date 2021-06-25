import narator
import temperature
import common


@common.dump_func(showarg=True)
def on_new_temperature(temperature):
    narator.play_temperature(temperature)


@common.dump_func()
def init():
    temperature.init()
    temperature.register_temperature_callback(on_new_temperature)
    temperature.get_temperature()
    narator.init()


def loop():
    narator.loop()
    temperature.loop()
