# Basic python script to read NEMEA 0183 sentences from GT-U7 GPS breakout board, 
# and display some of the key variables in the console.
import time
import serial
from micropyGPS import MicropyGPS

ser = serial.Serial(
        port='/dev/ttyAMA0',
        # port='COM3',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
        )

def parse_sentence(sentence):        
    for i in range(len(sentence)):
        my_sentence = sentence[i]
        for k in my_sentence:
            my_gps.update(k)
            
    print('')
    print(sentence)
    print('Latitude:', my_gps.latitude_string())
    print('Longitude:', my_gps.longitude_string())
    print('Speed:', my_gps.speed_string('kph'), 'or', my_gps.speed_string('mph'), 'or', my_gps.speed_string('knot'))
    print('Date (Long Format):', my_gps.date_string('long'))
    print('Date (Short D/M/Y Format):', my_gps.date_string('s_dmy'))
    print('Date (Short M/D/Y Format):', my_gps.date_string('s_mdy'))
    print('Time hh:mm:ss: %2d:%2d:%2d' %(my_gps.timestamp[0], my_gps.timestamp[1], my_gps.timestamp[2]))
    print('Satellites in use:', my_gps.satellites_in_use)
    print('Satellites in view:', my_gps.satellites_in_view)
    print('Satellites Used:', my_gps.satellites_used)
    print(type(my_gps.satellites_used))
    print('Satellite Data (Elevation, Azimuth,SNR):\n\r', my_gps.satellite_data)
    print('Horizontal Dilution of Precision:', my_gps.hdop)
    print('Position Dilution of Precision:', my_gps.pdop)
    print('Vertical Dilution of Precision:', my_gps.vdop)

my_gps = MicropyGPS()

# Clear the serial buffer
ser.readline()

i = 0
while 1:
    my_sentence = ser.readline().decode("utf-8")
    print(str(i))
    print(my_sentence)
    parse_sentence(my_sentence)
    i += 1
