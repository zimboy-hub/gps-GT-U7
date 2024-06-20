# 
## Overview

Python scripts to read NMEA 0183 sentences from a GT-U7 GPS breakout board, and display some of the key variables in the console.
micropyGPS is a full featured GPS NMEA sentence parser for use with MicroPython and the PyBoard embedded platform. It's also fully compatible with Python 3.x

Features:

    Parses and verifies most of the important NMEA-0183 output messages into easily handled data structures
    Provides helper methods to interpret, present, log, and manipulate the GPS data
    Written in pure Python 3.x using only the standard libraries available in Micropython
    Implemented as a single class within a single file for easy integration into an embedded project
    Parser written with a serial UART data source in mind; works on a single character at a time with robust error handling for noisy embedded environments
    Modeled after the great TinyGPS Arduino library

Install / uninstall
Link to GPS Board:
https://www.amazon.fr/Seamuing-Lorawan-Consumption-compris-Attitude/dp/B0833TMYQ3/ref=sr_1_6?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=397V1ZT8N267S&dib=eyJ2IjoiMSJ9.QBvrmhQejNwS2Z99rBT8rZOJgGVB3LAmFq_OG5vQBSc4jCOj-M10TxwFLtZyvXiBO19ZK4m9PqoiM-LiUlKd7RCWecRh3ZfrOzbTm7fZ6qvJYjBO5fEtxGpCkDvXUthWmSglbu18mhVX2PIeU7jkDOc6VTutODXxut0t_xHJPuzDl7r8neLb7iq8uZ1plr3BDsR8pHwgjqEEQ1tm1g3tOETz-_Vw3pH7Bm1vK3OiJZhw2jxs576vpVU7rRe3p1EjsMjrnyPmuYypd2IZGPdpyejLsUp8iOm1FEgEGsL_-8k.43GgsGWPjLtScTjTkJWRnVRs-Z05J69yiliYxl95uqc&dib_tag=se&keywords=neo+GPS+Breakout+board&qid=1714577315&sprefix=neogps+breakout+board%2Caps%2C408&sr=8-6

See https://www.youtube.com/watch?v=bgOZLgaLa0g for use of Seamuing GPS Module Small GPS Receiver 

Low Power High Sensitivity with IPEX Antenna Compatible with NEO-6M for 51 STM32 UNO R3 Arduino Microcontroller
Library: http://arduiniana.org/libraries/tinygpsplus/

See https://github.com/inmcm/micropyGPS?tab=readme-ov-file for details of GPS library for python
