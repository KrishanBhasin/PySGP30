from smbus2 import SMBusWrapper
from sgp30 import Sgp30
import time
with SMBusWrapper(1) as bus:
    sgp=Sgp30(bus)
    print("resetting all i2c devices")
    sgp.i2c_geral_call()
    print(sgp.read_features())
    print(sgp.read_serial())
    sgp.init_sgp()
    print(sgp.read_measurements())