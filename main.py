import time
from demos.sparkles import sparkles
from demos.rainbow import rainbow
from demos.fire import fire
from demos.snow import snow, snow_setup
from machine import Pin
from pimoroni import RGBLED, Button
import plasma

FPS = 60 
NUM_LEDS = 300
BRIGHTNESS = 0.3

# set up the Pico W's onboard LED
#pico_led = Pin('LED', Pin.OUT)
led = RGBLED("LED_R", "LED_G", "LED_B")
led.set_rgb(0, 0, 0)
button_a = Button("BUTTON_A", repeat_time=0)

# set up the WS2812 / NeoPixel™ LEDs
led_strip = plasma.WS2812(NUM_LEDS, color_order=plasma.COLOR_ORDER_GRB)
led_strip.clear()
# start updating the LED strip
led_strip.start()
frame = 0
mode = 0
snow_setup(NUM_LEDS)

while True:
    if(button_a.read()):
        print("button pressed")
        led_strip.clear()
        mode = (mode+1) % 4
    
    if(mode==0):
        rainbow(led_strip,NUM_LEDS,frame)
    elif(mode==1):
        snow(led_strip,NUM_LEDS,frame)
    elif(mode==2):
        fire(led_strip,NUM_LEDS,frame)
    else:
        sparkles(led_strip,NUM_LEDS,frame)
       
    frame = (frame+1)%1000
    time.sleep(1.0 / FPS)


def hex_to_rgb(hex):
    # converts a hex colour code into RGB
    h = hex.lstrip('#')
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return r, g, b


