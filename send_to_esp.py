import serial
import time

# Make sure this matches your port (ls /dev/ttyUSB* will confirm)
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
time.sleep(2) 

try:
    while True:
        msg = input("Enter message for ESP32: ")
        ser.write((msg + '\n').encode('utf-8'))
except KeyboardInterrupt:
    ser.close()
