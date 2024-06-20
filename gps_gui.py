
# Basic python script to read NEMEA 0183 sentences from GT-U7 GPS breakout board, 
# and display some of the key variables in a simple tkinter GUI.
from tkinter import Canvas, Frame, Tk, BOTH,StringVar,Label, Button
from threading import Thread
from micropyGPS import MicropyGPS
import serial

# Define serial port properties
ser = serial.Serial(
        # port='COM3',            # For PC
        port='/dev/ttyAMA0',  	  # For RPi 2
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
        )

# Instantiate a MicropyGPS object to hold the data parsed
# from the serial port.
my_gps = MicropyGPS()

# Map MicropyGPS methods and properties to tkinter.
# This enables an arbitrary number of MicropyGPS 
# methods and properties to be used by simply adding
# to or subtracting from the list. The order in which 
# they are declared in the list is the order they will be displayed in the gui.
# Element 1: Label text for tkinter gui element
# Element 2: Units text for tkinter gui element
# Element 3: MicropyGPS method or property that the tkinter display element is bound to
# Element 4: MicropyGPS method or property type
#            'none': Uses MicropyGPS method that does not take a parameter
#            'attr': Uses MicropyGPS property
#            'kv': Uses MicropyGPS property formatted as key value pairs
#            'some value': Uses parameter for MicropyGPS method
l1=[['Date and Time','',my_gps.date_string,'long'],
    ['Latitude','',my_gps.latitude_string,'none'],
    ['Longitude','',my_gps.longitude_string,'none'],
    ['Speed:','kmh',my_gps.speed_string,'kph'],
    ['Speed:','mph',my_gps.speed_string,'mph'],
    ['Speed:','knots',my_gps.speed_string,'knot'],
    ['Date:','(Long Format)',my_gps.date_string,'long'],
    ['Date:','D/M/Y',my_gps.date_string,'s_dmy'],
    ['Date:','M/D/Y',my_gps.date_string,'s_mdy'],
    ['Horizontal Dilution of Precision:','(hdop)','hdop','attr'],
    ['Position Dilution of Precision:','(pdop)','pdop','attr'],
    ['Vertical Dilution of Precision:','(vdop)','vdop','attr'],
    ['# satellites in view:','','satellites_in_view','attr'],
    ['# satellites in use:','','satellites_in_use','attr'],
    ['Satellites used:','','satellites_used','attr'],
    ['Satellite Data:','(Elevation, Azimuth,SNR)','satellite_data','kv']
    ]

# Copy the raw serial data into the MicropyGPS object
def parse_sentence(sentence):        
    for i in range(len(sentence)):
        my_sentence = sentence[i]
        for k in my_sentence:
            my_gps.update(k)

# tkinter initialization
class App(Frame):
    def __init__(self, master):
        self.master = master
        Frame.__init__(self, self.master)

        # Initialize gui apperance
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.master.title("GPS data")
        self.master.geometry('1000x900')

        self.display = Canvas(self, bd=0, highlightthickness=0)        
        self.display.grid(row=0)
        
        self.pack(fill=BOTH, expand=1)
        font_= ('veranda',12)

        # StringVars for communicating data values from the serial port thread to the gui.
        self.strData = {}

        # Create main window widgets by iterating through values from the l1 list
        for rowcount, (g_label, g_unit, g_target, g_type) in enumerate(l1): # get each row of the list as data 

            # Label for the GPS attribute
            i_label=Label(self.display,text=g_label,font=font_)
            i_label.grid(row=rowcount,column=0,padx=10,pady=5, sticky="w")

            # tkinter string variables (StringVar) are used to communicate values between
            # a python script and a tkinter gui data element. The strData dictionary creates a 
            # mapping from the data values in MicropyGPS to the corresponding
            # tkinter gui data element.
            sv = StringVar()
            i_label=Label(self.display,textvariable=sv,font=font_)
            i_label.grid(row=rowcount,column=1,padx=10,pady=5, sticky="nw", rowspan=1)
            self.strData[rowcount] = (i_label, sv)

            # Unit for the GPS attribute
            i_label=Label(self.display,text=g_unit,font=font_)
            i_label.grid(row=rowcount,column=2,padx=10,pady=5, sticky="w")

        # Add an "Exit" button to the main form
        self.exit_button = Button(self, text='Exit', command=self.close_win,font=font_, padx=5, pady=5, relief='raised')
        self.exit_button.grid(row=2, column=0)

        # Kill everything when it's time to exit
        self.loop_running= True
        self.master.protocol('WM_DELETE_WINDOW', self.close_win)

        # Clear the serial buffer
        ser.readline()
        
        # Start the thread to read the serial buffer
        self.thread = Thread(target= self.read_serial)
        self.thread.start()

    # Kill everything when it's time to exit 
    def close_win(self):
        self.loop_running= False
    
    # Function to read the serial port, unpack the data data into the MicropyGPS object,
    # and then display the data in the tkinter gui. This runs in a separate thread from tkinter.
    # The MicropyGPS data is provided in a variety of formats, so some manipulation is 
    # required to get it in a decent format.
    def read_serial(self):
        if self.loop_running:
            my_sentence = ser.readline().decode("utf-8")    # Get data from the serial port 
            parse_sentence(my_sentence)                     # Populate the MicropyGPS data structure

            for i in range(1, len(l1)):                     # Skip the zero element. It will be populated via g_datetime
                if (l1[i][3]) =='none':                     # Display MicropyGPS methods that don't take a parameter
                    text = str( l1[i][2]() )
                elif(l1[i][3]) =='attr':                     # Display MicropyGPS properties
                    text = getattr( my_gps, l1[i][2] )
                elif(l1[i][3]) =='kv':                       # Display MicropyGPS key value properties
                    temp1 = getattr( my_gps, l1[15][2] )
                    text = ''
                    for key, value in temp1.items():        # Display 
                        temp2 = str(key) + ': ' + str(value)
                        text = text + '\n' + str(temp2)
                else:                                       # Display MicropyGPS methods that take a parameter
                    text = l1[i][2] ( l1[i][3] )
                    if l1[i][3] in ('kph', 'mph', 'knot'):
                        text = round(float(text[:-5]), 3)
                sv = self.strData[i][1]
                sv.set(text)

            # Concatenate date and time and display in first item in the gui list
            g_datetime = f"{my_gps.date_string('long')} {my_gps.timestamp[0]:02d}:{my_gps.timestamp[1]:02d}:{int(my_gps.timestamp[2]):02d}"
            sv = self.strData[0][1]
            sv.set(g_datetime)
            self.display.update()
            self.display.after(100,self.read_serial)
        else:
            try:
                self.master.destroy()
                
            except:
                pass

if __name__ == '__main__':
    root = Tk()
    App(root)
    root.mainloop()