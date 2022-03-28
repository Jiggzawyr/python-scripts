# Simple pygame program

import math 
import pygame as pg
pg.init()

# Set up the drawing window
screen = pg.display.set_mode([200, 200])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))


    # Draw a solid blue circle in the center    
    pg.draw.polygon(screen, pg.Color("red"), [(50, 100), (100, 50), (150, 100), (100,150)])

    r = 50 * math.sqrt(2) / 2

    pg.draw.circle(screen, pg.Color("red"), (75,75), r)
    pg.draw.circle(screen, pg.Color("red"), (125,75), r)

    # Flip the display
    pg.display.flip()

# Done! Time to quit.
pg.quit()