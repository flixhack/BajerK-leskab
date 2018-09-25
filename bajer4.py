from pyfirmata import Arduino, util
import tkinter as tk
import time

board = Arduino("COM3")

def skydBajer():
    board.digital[13].write(1)
    time.sleep(2)
    board.digital[13].write(0)
    time.sleep(0.5)



window = tk.Tk()

window.config(height=600, width=600)

skydBajerKnap = tk.Button(command=skydBajer, text="BAJER!")
skydBajerKnap.config(height=4, width=10)
skydBajerKnap.place(x=270, y=280)





window.mainloop()
