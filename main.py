import pygame as py
import tkinter

py.init()
screen = py.display.set_mode((960, 700))
timer = py.time.Clock()

text = py.font.Font(None, 36)


def create_board():
    py.draw.rect(screen, 'black', (200 - 2, 0, 564, 562), 2)
    for i in range(4):
        py.draw.rect(screen, (227, 177, 89), (200, 140*i, 70, 70))
    
        py.draw.rect(screen, (227, 177, 89), (340, 140*i, 70, 70))
    
        py.draw.rect(screen, (227, 177, 89), (480, 140*i, 70, 70))
    
        py.draw.rect(screen, (227, 177, 89), (620, 140*i, 70, 70))
    
        py.draw.rect(screen, (227, 177, 89), (270, 70+ 140*i, 70, 70))

        py.draw.rect(screen, (227, 177, 89), (410, 70+ 140*i, 70, 70))

        py.draw.rect(screen, (227, 177, 89), (550, 70+ 140*i, 70, 70))

        py.draw.rect(screen, (227, 177, 89), (690, 70+ 140*i, 70, 70))
        
    


running = True
while running:
    timer.tick(60)
    screen.fill((115, 73, 31))
    create_board()



    for event in py.event.get():
        if event.type == py.QUIT:
            running = False


    py.display.flip()



py.quit()