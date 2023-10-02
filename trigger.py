from machine import ADC
from machine import Pin

# use ADC #2
adc = ADC(28)
pin = Pin(22, Pin.OUT, Pin.PULL_UP, value=0)



def trigger(value=14500):
    global adc
    num_samps = 0
    pin.off()
    while True:
        if num_samps >= 3:
            pin.on()
            print("Trigger ",num_samps)
            break
    
        v = adc.read_u16()
        
        if num_samps >= 3 and v < 2000:
            num_samps = 0

        if v >= value:
            num_samps = num_samps + 1

