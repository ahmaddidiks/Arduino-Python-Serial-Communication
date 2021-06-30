#!/usr/bin/env python3

import serial
from time import sleep
from struct import unpack, pack

ser = serial.Serial('/dev/ttyACM0', 57600)  # open serial port

def sendData(data1, data2, data3):
    dataPacket = pack("hhh", data1, data2, data3)
    ser.write(dataPacket)

while True:
    dataRaw = ser.read(6) #6 ===> 2 x 3 of short data types (2 Bytes)
    print(dataRaw)
    data1, data2, data3 = unpack("hhh", dataRaw) #hhh for short ===> int (in arduino [atmel microprocessors]) = short in python, they have same size, 2 Bytes
    print(f"data1: {data1}")
    print(f"data2: {data2}")
    print(f"data3: {data3}")

    sendData(3, 5, 7)

    sleep(0.1)

