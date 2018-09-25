from pyfirmata import Arduino, util
import time as t

board = Arduino("COM3")
#
# board.digital[13].write(1)
for i in range(1):
    board.digital[13].write(1)
    t.sleep(2)
    board.digital[13].write(0)
    # board.digital[13].write(1)
    # board.digital[13].write(0)
