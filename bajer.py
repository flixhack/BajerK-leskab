import serial
import tkinter as tk


intNoBy = 1
byInt = 49


def bajer():
    arduinoSerialData = serial.Serial('COM3',9600)
    arduinoSerialData.write(byInt)
    arduinoSerialData.write({0})
    print(byInt)




window=tk.Tk()
window.title("BAJER!")
window.config(height=600, width=800)

bajerKnap = tk.Button(window, text="bajer", command=bajer)
bajerKnap.place(x=300, y=250)


window.mainloop()
