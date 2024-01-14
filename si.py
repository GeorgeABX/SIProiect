from machine import Pin
from machine import Timer
from ir_rx import NEC_16
import time
from neopixel import Neopixel

#Functie care citeste octetul primit prin senzorul infrarosu
def ir_callback(data, addr, ctrl):
    global ir_data
    global ir_addr
    if data > 0:
        ir_data = data
        ir_addr = addr
        print('Data {:02x} Addr {:04x}'.format(data, addr))
        
ir = NEC_16(Pin(17, Pin.IN), ir_callback)
ir_data = 0
ir_addr = 0
#Instanta a unui obiect de tip neopixel
pixels = Neopixel(5, 0, 16, "RGB")

curent = 0
leds_on = [0, 0, 0, 0, 0, 0]

while True:
    if ir_data > 0:
        
        #Cele 5 butoane care semnifica fiecare din cele 5 leduri
        if ir_data == 0x01:
            curent=1
            if(leds_on[curent]==0):
                leds_on[curent]=1
            else:
                leds_on[curent]=0
        if ir_data == 0x02:
            print("2")
            curent=2
            if(leds_on[curent]==0):
                leds_on[curent]=1
            else:
                leds_on[curent]=0
        if ir_data == 0x03:
            print("3")
            curent=3
            if(leds_on[curent]==0):
                leds_on[curent]=1
            else:
                leds_on[curent]=0
        if ir_data == 0x04:
            print("4")
            curent=4
            if(leds_on[curent]==0):
                leds_on[curent]=1
            else:
                leds_on[curent]=0
        if ir_data == 0x05:
            print("5")
            curent=5
            if(leds_on[curent]==0):
                leds_on[curent]=1
            else:
                leds_on[curent]=0
        
        #Butoanele care semnifica fiecare culoare disponibila
        if ir_data == 0x40:
            print("red")
            if(leds_on[curent]==1):
                pixels.set_pixel(curent-1, (0, 100, 0))
                print(leds_on[curent])
        if ir_data == 0x42:
            print("green")
            if(leds_on[curent]==1):
                pixels.set_pixel(curent-1, (100, 0, 0))
                print(leds_on[curent])
        if ir_data == 0x41:
            print("yellow")
            if(leds_on[curent]==1):
                pixels.set_pixel(curent-1, (100, 100, 0))
                print(leds_on[curent])
        if ir_data == 0x43:
            print("blue")
            if(leds_on[curent]==1):
                pixels.set_pixel(curent-1, (0, 0, 100))
                print(leds_on[curent])
        
        #Butoane care opresc ledurile
        if ir_data == 0x12:
            print("POWER off one")
            pixels.set_pixel(curent-1, (0, 0, 0))
            if(leds_on[curent]==1):
                leds_on[curent]=0
            else:
                leds_on[curent]=1
        if ir_data == 0x0f:
            print("POWER off")    
            for i in range(0,5):
                pixels.set_pixel(i, (0, 0, 0))
                leds_on[i+1]=0
            
        ir_data=0
    pixels.show()
    time.sleep(1)
    
    

