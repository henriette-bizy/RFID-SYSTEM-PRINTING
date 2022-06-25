#!/usr/bin/env python3
import requests
import serial
ser = serial.Serial(
    port='COM3',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
ser.flush()
if __name__ == '__main__':
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            f=open("transactions.txt","a")
            f.write(line)
            f.write("\n")
            f.close()
            print(line)
            url = 'http://localhost:5000/uploadedData'
            obj = {'newTransaction': line}
            x = requests.post(url, obj)
            print(x.text)
            ser.write("Data uploaded")


