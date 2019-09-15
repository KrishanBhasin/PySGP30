from smbus2 import SMBus
from sgp30 import SGP30

if __name__ == "__main__":
    bus = SMBus(1)
    sensor = SGP30(bus)
    print(sensor.read_features())
    print(sensor.read_serial())
    sensor.init_sgp()
    for i in range(300):
        print(sensor.read_measurements())
        time.sleep(0.1)
    sensor.store_baseline()
    bus.close()