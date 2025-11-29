from random import random, uniform

def fire(led_strip, num_leds,frame):
    for i in range(num_leds):
        led_strip.set_hsv(i, uniform(0.0, 50 / 360), 1.0, random() % 0.3)