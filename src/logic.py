import narator
import temperature
import common


@common.dump_func(showarg=True)
def on_new_temperature(temperature):
    narator.play_temperature(temperature)


def init():
    narator.init()
    temperature.init()
    temperature.register_temperature_callback(on_new_temperature)
    temperature.get_temperature()


def loop():
    narator.loop()
    temperature.loop()
