import serial
arduinoSerialData = serial.Serial('COM3',9600)
arduinoSerialData.write({1})
print({1})
