
def rainbow(led_strip, num_leds,frame):
    for i in range(num_leds):
        hue = float(i) / num_leds
        offset = float(frame/500.0) # lower = faster
        led_strip.set_hsv(i, (hue + offset) % 1.0, 1.0, 0.3)