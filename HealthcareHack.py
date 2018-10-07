import serial
import time
from Adafruit_IO import Client, Feed, Data
aio = Client('roshea','5a036c274def42da94fb866f11030bea')
ser = serial.Serial('/dev//ttyUSB0',9600)
counter = 0

feed1 = Feed(name='heartrate')
feed2 = Feed(name='incident')
feed3 = Feed(name='incidentlocation')
incidentlocationdata = Data(value =1)

while True:
    incidentdata = Data(value =0)
    data = Data(value = int(ser.readline()))
    print(data.value)
    if data==2000:
        counter += 1
        incidentdata = Data(value =counter)
        incidentlocationdata = Data(value =0)
    else :
        time.sleep(1.5)
        aio.create_data('heartrate',data)

        
    time.sleep(1.5)
    aio.create_data('incident',incidentdata)
    time.sleep(1.5)
    aio.create_data('incidentlocation', incidentlocationdata)
    time.sleep(1.5)
