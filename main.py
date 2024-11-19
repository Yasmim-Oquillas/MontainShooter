import pygame as pg

print('Setup start')
pg.init()
window = pg.display.set_mode(size=(600, 480))
print('Setup end')

print('Loop start')

while True:
    # Check for all events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()  # close window
            quit()  # end pygame
