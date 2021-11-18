import serial
import os
import time

data = open("Input.txt", "w")
ser = serial.Serial('COM6', 115200, timeout=100)  # open serial port

if ser:
    print("Serial Port opened on : " + ser.name)
else :
    print("Use python -m serial.tools.list_ports to check the correct port and modify the code")

ser.write(b'M564 S0 H0\r\n')
time.sleep (0.02)
ser.write(b'M111 S1 P6\r\n')
time.sleep (0.02)
ser.write(b'M111 S1 P4\r\n')

counter = 0
while (1):
    response = ser.readline().decode('utf-8')
    print(response)
    data.write(response)
    if response == "":
        break

time.sleep(1)
data.close()
