from random import uniform
# How much snow? [bigger number = more snowflakes]
SNOW_INTENSITY = 0.0002

# Change RGB colours here (RGB colour picker: https://g.co/kgs/k2Egjk )
BACKGROUND_COLOUR = [20, 22, 22]  # dim blue
SNOW_COLOUR = [200, 200, 200]  # bluish white

# how quickly current colour changes to target colour [1 - 255]
FADE_UP_SPEED = 255  # abrupt change for a snowflake
FADE_DOWN_SPEED = 1

current_leds = []
target_leds = []



def move_to_target(n):
    # nudge our current colours closer to the target colours
    for i in range(n):
        for c in range(3):  # 3 times, for R, G & B channels
            if current_leds[i][c] < target_leds[i][c]:
                current_leds[i][c] = min(current_leds[i][c] + FADE_UP_SPEED, target_leds[i][c])  # increase current, up to a maximum of target
            elif current_leds[i][c] > target_leds[i][c]:
                current_leds[i][c] = max(current_leds[i][c] - FADE_DOWN_SPEED, target_leds[i][c])  # reduce current, down to a minimum of target

def snow_setup(num_leds):
    global current_leds,target_leds
    # Create a list of [r, g, b] values that will hold current LED colours, for display
    current_leds = [[0] * 3 for i in range(num_leds)]
    # Create a list of [r, g, b] values that will hold target LED colours, to move towards
    target_leds = [[0] * 3 for i in range(num_leds)]

def snow(led_strip, num_leds,frame):

    for i in range(num_leds):
        # randomly add snow
        if SNOW_INTENSITY > uniform(0, 1):
            # set a target to start a snowflake
            target_leds[i] = SNOW_COLOUR
        # slowly reset snowflake to background
        if current_leds[i] == target_leds[i]:
            target_leds[i] = BACKGROUND_COLOUR
    move_to_target(num_leds)   # nudge our current colours closer to the target colours

    for i in range(num_leds):
        led_strip.set_rgb(i, current_leds[i][0], current_leds[i][1], current_leds[i][2])
