import adafruit_dht
import board
import os
import sys
import time

# Polls the sensor given a defined amount of time.
# Output stored in relative path data/db/dd-mm-yyyy.csv on a csv
# file named after the day the data is generated.
# Csv format: Time,Temperature,Humidity.
# Sensor polling errors are stored in local path data/errors.txt.

inputPin = board.D4
dhtSensor = adafruit_dht.DHT22( inputPin )
timeBetweenReads = 300 # seconds

currentDate = None
csvFile = None

while True:
    # if we have moved on a new day we need a new csv
    if currentDate != time.strftime( '%d-%m-%y' ):
        currentDate = time.strftime( '%d-%m-%y' )
        if csvFile != None:
            csvFile.close()
        path = 'data/db/' + currentDate + '.csv'
        csvFile = open( path, 'a' )

        # if the file is empty initialize with format header
        if os.stat( path ).st_size == 0:
            csvFile.write( 'Time,Temperature,Humidity\n' )

    try:
        # get data from the sensor
        temperature = dhtSensor.temperature
        humidity = dhtSensor.humidity
        csvFile.write('{0},{1:0.1f},{2:0.1f}\n'.format(
            time.strftime( '%H:%M' ), temperature, humidity ) )
    except:
        e = sys.exc_info()
        errorFile = open( 'data/errors.txt', 'a' )
        errorMsg = '{0},{1}:{2}\n'.format( currentDate, time.strftime( '%H:%M' ), e )
        errorFile.write( errorMsg )
        errorFile.close()

    time.sleep( timeBetweenReads )
