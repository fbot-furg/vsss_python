import time

from classes.Communication import Communication

comm = Communication()

time.sleep(0.5)
print(comm.environment())
time.sleep(1)
print(comm.environment())

comm.stop()