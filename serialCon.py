import time
import serial

class SerialCon:
    
    def __init__(self, serialport):
        self.con = serial.Serial(serialport, baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
        self.data = 0

    def send(self, data):
        self.con.write(data)

    def get(self):
        while True:
            if self.con.inWaiting() > 0:
                self.data = int(self.con.read())