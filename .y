# CircuitPython demo - NeoPixel
 
import time
import random
import board
import neopixel
 
pixel_pin = board.D1
num_pixels = 32
SPEED = 20000
 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False, pixel_order=(1, 0, 2, 3))

# COLORS 
RED = (255, 0, 0, 0)
YELLOW = (255, 150, 0, 0)
ORANGE = (255, 165, 0, 0)
GREEN = (0, 255, 0, 0)
WHITE = (255, 255, 255, 0)
CYAN = (0, 255, 255, 0)
BLUE = (0, 0, 255, 0)
SKYBLUE = (135, 206, 250, 0)
PURPLE = (180, 0, 255, 0)
BLACK = (0, 0, 0, 0)
INDIGO = (63, 81, 181, 0)
VIOLET = (238, 130, 238, 0)
LOWWHITE = (4, 4, 4, 4)
LOWRED = (4, 0, 0, 0)
LOWBLUE = (0, 0, 4, 0)

flippity = LOWRED

# COLOR PALLETS
LIGHTNING = [WHITE, CYAN, SKYBLUE, BLUE, PURPLE]
FIRE = [RED, YELLOW, BLACK, ORANGE]
USA = [LOWRED, LOWWHITE, LOWBLUE, BLACK]
CANADA = [LOWWHITE, LOWRED, BLACK]
RAINBOW = [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET]

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
    pixels[aPixel] = BLACK
    pixels.show

def manyMultiPalletBurst(aPallet):
    numColors = len(aPallet)
    
    for aColor in range(numColors):
        
        for i in range(len(pixels)):
            # select the "even" pixels
            if(i % 2 == 0):
                color = aPallet[random.randint(0, numColors-1)]
            else:
                color = aPallet[random.randint(0, numColors-1)]
            
            pixels[i] = color
            # print("pixel ", i, "is set to ", color)
            # time.sleep(.0625)

        # print("showing...")
        pixels.show()
        # time.sleep(.0078)
    
# MAIN LOOP (near as I can tell)
while True:
    # for anOrderedPixel in pixels:
    #    pixelPos = random.randint(0, (num_pixels-1))
    #    multiPalletBurst(pixelPos, USA)
    #manyMultiPalletBurst(FIRE)
    #manyMultiPalletBurst(CANADA)
    #manyMultiPalletBurst(LIGHTNING)
    manyMultiPalletBurst(USA)
    #manyMultiPalletBurst(RAINBOW)
    
