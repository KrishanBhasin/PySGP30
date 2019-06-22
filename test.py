from smbus2 import SMBusWrapper
from sgp30 import SGP30
import time
with SMBusWrapper(1) as bus:
    sgp = SGP30(bus)
    print("resetting all i2c devices")
    sgp.i2c_general_call()
    print(sgp.read_features())
    print(sgp.read_serial())
    sgp.init_sgp()
    for i in range(300):
        print(sgp.read_measurements())
        time.sleep(0.1)
    sgp.store_baseline()
