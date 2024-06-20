# Python code for GT-U7 GPS breakout board on Raspberry Pi 2
## Overview
The GT-U7 GPS board can be found [here](https://www.amazon.com/Navigation-Satellite-Compatible-Microcontroller-Geekstory/dp/B07PRGBLX7?th=1)

Two python scripts are provided to display some of the key GPS parameters read from a GT-U7 GPS breakout board attached to a Raspberry Pi 2:

- gps_basic.py: read NEMEA 0183 sentences from GT-U7 GPS breakout board, and display some of the key GPS pparameters in the console.
- gps_gui.py: read NEMEA 0183 sentences from GT-U7 GPS breakout board, and display some of the key GPS pparameters in a simple tkinter GUI.

The code is provided for proof of concept / starter code that can be used as a starting point for a users own development. It was developed using python 3.12.1, and tested on a PC running windows 11 and a Raspberry Pi 2.

    
Link to GPS Board:
https://www.amazon.fr/Seamuing-Lorawan-Consumption-compris-Attitude/dp/B0833TMYQ3/ref=sr_1_6?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=397V1ZT8N267S&dib=eyJ2IjoiMSJ9.QBvrmhQejNwS2Z99rBT8rZOJgGVB3LAmFq_OG5vQBSc4jCOj-M10TxwFLtZyvXiBO19ZK4m9PqoiM-LiUlKd7RCWecRh3ZfrOzbTm7fZ6qvJYjBO5fEtxGpCkDvXUthWmSglbu18mhVX2PIeU7jkDOc6VTutODXxut0t_xHJPuzDl7r8neLb7iq8uZ1plr3BDsR8pHwgjqEEQ1tm1g3tOETz-_Vw3pH7Bm1vK3OiJZhw2jxs576vpVU7rRe3p1EjsMjrnyPmuYypd2IZGPdpyejLsUp8iOm1FEgEGsL_-8k.43GgsGWPjLtScTjTkJWRnVRs-Z05J69yiliYxl95uqc&dib_tag=se&keywords=neo+GPS+Breakout+board&qid=1714577315&sprefix=neogps+breakout+board%2Caps%2C408&sr=8-6

See https://www.youtube.com/watch?v=bgOZLgaLa0g for use of Seamuing GPS Module Small GPS Receiver 

Low Power High Sensitivity with IPEX Antenna Compatible with NEO-6M for 51 STM32 UNO R3 Arduino Microcontroller
Library: http://arduiniana.org/libraries/tinygpsplus/

See https://github.com/inmcm/micropyGPS?tab=readme-ov-file for details of GPS library for python
