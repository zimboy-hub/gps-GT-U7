# Python code for GT-U7 GPS breakout board on Raspberry Pi 2
## Overview
This code reads data from a GT-U7 GPS breakout board in NMEA-0183 format using the Raspberry Pi serial port. The serial data is converted into python object data and displayed. Two python scripts are provided to display some of the key GPS parameters:

- **gps_basic.py:** reads NMEA 0183 sentences from the GT-U7 GPS breakout board, and displays some of the key GPS parameters in the console. This is a minimal script that can be used to verify that basic communication has been established between the RPi and the breakout board. To run it use:

  `sudo python3 gps_basic.py`
  
- **gps_gui.py:** reads NMEA 0183 sentences from the GT-U7 GPS breakout board, and displays some of the key GPS parameters in a simple tkinter GUI. This is a slightly more user friendly script than gps_basic.py that can be used to demonstrate how to display data from the breakout board in a minimal UI. To run it use:

  `sudo python3 gps_gui.py`

This code is provided for proof of concept or as starter code. It provides minimal functionality that can be used as a starting point for your own development. It was developed using:

- python 3.12.1 on win 11
- python 3.9.2 on RPi2

The RPi2 OS was:

`linux raspberrypi 6.1.21-v7+ #1642 SMP Mon Apr  3 17:20:52 BST 2023 armv7l GNU/Linux.`

I was unable to receive any GPS signals inside my apartment, but it worked fine outdoors.

## Resources
### Breakout board
Details of the GT-U7 GPS board can be found [here](https://www.amazon.com/Navigation-Satellite-Compatible-Microcontroller-Geekstory/dp/B07PRGBLX7?th=1.)

### NMEA 0183
Details of the protocol can be found [here](https://www.sparkfun.com/datasheets/GPS/NMEA%20Reference%20Manual-Rev2.1-Dec07.pdf)

### micropyGPS
This library converts the NMEA-0183 serial data from the breakout board into python object variables that can be accessed from the code. See [here](https://github.com/inmcm/micropyGPS) for details.

To install:

`pip install git+https://github.com/inmcm/micropyGPS.git`

### tkinter
tkinter is a GUI framework for python that is built into the python standard library. See [here](https://realpython.com/python-gui-tkinter/) for an excellent tutorial.

To install:

The tkinter library is built in to python, so if you have python installed, you should have access.

### threads
tkinter is an event driven application that runs in its own process. A python thread, separate from the tkinter main process, is needed to read GPS data from the serial port of the RPi2, format it, and send it to tkinter. See [here](https://realpython.com/intro-to-python-threading/) for an excellent tutorial.

To install:

The threads library is built in to python, so if you have python installed, you should have access.

### pyserial
This library is used to get the NMEA-0183 data from the breakout board using the RPi2 serial port . 

**Note:** The older **serial** library is deprecated. If it is installed, you should uninstall it otherwise you may encounter conflicts with pyserial.

To install pyserial:

`pip install pyserial`

## Notes
The excellent micropyGPS library (finding this made this project viable) provides the GPS data in several different access formats:
- methods with parameters,
- methods without parameters,
- simple properties,
- properties that return python dictionaries.

As a result of these different formats, quite a bit of data manipulation is required to get the data into a format suitable for display in the tkinter GUI. 

## To Do
- Add an additional frame to the gps_gui.py GUI to stop the screen from scrolling up as the satellite_data key:value pairs are rendered.
- Create a wrapper for the micropyGPS library to enable a uniform access method for all data attributes.
