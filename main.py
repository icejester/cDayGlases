# CircuitPython demo - NeoPixel
 
import time
import random
import board
import neopixel
 
pixel_pin = board.D1
num_pixels = 32
SPEED = 20000

EVENS = True
 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=.03125, auto_write=False, pixel_order=(1, 0, 2, 3))

# COLORS 
RED = (255, 0, 0, 0)
YELLOW = (255, 150, 0, 0)
ORANGE = (255, 165, 0, 0)
GREEN = (0, 255, 0, 0)
DARKGREEN = (0, 135, 27, 0)
WHITE = (255, 255, 255, 0)
CYAN = (0, 255, 255, 0)
BLUE = (0, 0, 255, 0)
SKYBLUE = (135, 206, 250, 0)
PURPLE = (90, 0, 127, 0)
BLACK = (0, 0, 0, 0)
INDIGO = (63, 81, 181, 0)
VIOLET = (238, 130, 238, 0)
LOWWHITE = (60, 60, 60, 60)
LOWRED = (60, 0, 0, 0)
LOWBLUE = (0, 0, 127, 0)
PINK = (150, 0, 150, 22)
MAGENTA = (250, 0, 255, 0)

flippity = LOWRED

# COLOR PALLETS
LIGHTNING = [WHITE, CYAN, SKYBLUE, BLUE, PURPLE]
FIRE = [RED, YELLOW, BLACK, ORANGE]
USA = [LOWRED, LOWWHITE, LOWBLUE, BLACK]
CANADA = [RED, WHITE, RED, WHITE, RED, WHITE, RED]
LOWCANADA = [LOWRED, LOWWHITE, LOWRED, LOWWHITE, LOWRED, LOWWHITE, LOWRED]
RAINBOW = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
LUNA = [RED, DARKGREEN, ORANGE, BLUE, PURPLE, PINK, MAGENTA]

# functions
def burst(aPixel):
    # print("  Entering function: burst")
    pixels[aPixel] = WHITE
    time.sleep(0.0125)
    pixels.show()
    pixels[aPixel] = CYAN
    time.sleep(0.0125)
    pixels.show()
    pixels[aPixel] = BLUE
    time.sleep(0.0125)
    pixels.show()
    # pixels[aPixel] = LOWWHITE
    # time.sleep(0.0125)
    # pixels.show()

def palletBurst(aPixel, aPallet):
    # print("  Entering function: palletBurst")
    # print('aPixel is ', aPixel)
    # print('aPallet is ', aPallet)
    # aColor = random.randint(0, len(aPallet) -1)
    aColor = random.randint(0, len(aPallet) - 1)
    # print('aColor is', aColor)
    pixels[aPixel] = aPallet[aColor]
    pixels.show()
    # time.sleep(0.0125)

def multiPalletBurst(aPixel, aPallet):
    # print("  Entering function: multiPalletBurst")
    # total duration of burst
    # burstDuration = .0625
    
    # how many colors in the pallet?
    numColors = len(aPallet)
    # print('numColors is ', numColors)
    # miniBurst = burstDuration/numColors
    # print('  miniBurst is', miniBurst)
    # for total number of colors in pallet, choose a random one
    for i in range(numColors):
        aColor = random.randint(0, numColors-1)
        pixels[aPixel] = aPallet[aColor]
        pixels.show()
        # time.sleep(miniBurst)
    # pixels[aPixel] = BLACK
    pixels.show

def manyMultiPalletBurst(aPallet):
    numColors = len(aPallet)
    
    for aColor in range(1):
        
        for i in range(len(pixels)):
            # select the "even" pixels
            if EVENS == True:
                if(i % 2 == 0):
                    color = aPallet[random.randint(0, numColors-1)]
                else:
                    color = BLACK
            else:
                if(i % 2 == 0):
                    color = BLACK
                else:
                    color = aPallet[random.randint(0, numColors-1)]
                    
            
            pixels[i] = color
            
        pixels.show()
        
# MAIN LOOP (near as I can tell)
while True:
    # manyMultiPalletBurst(FIRE)
    # manyMultiPalletBurst(LOWCANADA)
    # manyMultiPalletBurst(CANADA)
    manyMultiPalletBurst(USA)
    # manyMultiPalletBurst(LIGHTNING)
    # manyMultiPalletBurst(LUNA)
    # manyMultiPalletBurst(RAINBOW)
    if EVENS == True:
        EVENS = False
    else:
        EVENS = True
    
