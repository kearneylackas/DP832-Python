from DP832 import *

try:
    PSU = DP832()
    print(PSU.status())
except:
    print("Connection Failed, Script Ended")

PSU.toggle_output(1, 0)
PSU.set_voltage(1, 13.333)
print(PSU.measure_current(1))
