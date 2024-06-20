# Python code for GT-U7 GPS breakout board on Raspberry Pi 2
## Overview
Details of the GT-U7 GPS board can be found [here](https://www.amazon.com/Navigation-Satellite-Compatible-Microcontroller-Geekstory/dp/B07PRGBLX7?th=1)

Two python scripts are provided to display some of the key GPS parameters read from a GT-U7 GPS breakout board attached to a Raspberry Pi 2:

- gps_basic.py: reads NEMEA 0183 sentences from GT-U7 GPS breakout board, and display some of the key GPS pparameters in the console.
- gps_gui.py: reads NEMEA 0183 sentences from GT-U7 GPS breakout board, and display some of the key GPS pparameters in a simple tkinter GUI.

The code is provided for proof of concept or starter code. It provides minimal functionality that can be used as a starting point for your own development. It was developed using python 3.12.1, and tested on a PC running windows 11 and a Raspberry Pi 2.

I was unable to receive any GPS signals inside my apartment, but it worked well when outdoors.

## Resources
### NMEA 0183
Details of the protocol can be found [here](https://www.sparkfun.com/datasheets/GPS/NMEA%20Reference%20Manual-Rev2.1-Dec07.pdf)

### micropyGPS
This library converts the serial data from the breakout board into a python list that can be accessed from the code. See [here](https://github.com/inmcm/micropyGPS) for details.

To install:

`pip install git+https://github.com/inmcm/micropyGPS.git`

### tkinter
tkinter is a GUI framework for python that is built into the python standard library. See [here](https://realpython.com/python-gui-tkinter/) for an excellent tutorial.

To install:

The tkinter library is built in to python, so if you have python installed, you should have access.

### Threads
tkinter is an event driven application that runs in its own process. A python thread, separate from the tkinter main process, is used to read GPS data from the serial port of the Raspberry Pi, format it, and send it to tkinter. See [here](https://realpython.com/intro-to-python-threading/) for an excellent tutorial.

To install:

The threads library is built in to python, so if you have python installed, you should have access.

### pyserial
This library to read the serial port from the Raspberry pi. Note that theolder serial library is deprecated, and you should uninstall it otherwise yo may encounter problems with serial communication.

To install:

`pip install pyserial`
