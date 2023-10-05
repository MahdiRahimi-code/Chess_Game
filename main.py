import pygame as py
import tkinter

py.init()
screen = py.display.set_mode((960, 700))
timer = py.time.Clock()

text = py.font.Font(None, 36)


def create_board():
    py.draw.rect(screen, 'black', (200 - 2, 0, 564, 562), 2)
    py.draw.line(screen, 'black', (198, 560), (198, 700), 2)
    py.draw.line(screen, 'black', (760, 560), (760, 700), 2)
    for i in range(4):
        py.draw.rect(screen, (227, 177, 89), (200, 140*i, 70, 70))
        py.draw.rect(screen, (227, 177, 89), (340, 140*i, 70, 70))
        py.draw.rect(screen, (227, 177, 89), (480, 140*i, 70, 70))
        py.draw.rect(screen, (227, 177, 89), (620, 140*i, 70, 70))
        py.draw.rect(screen, (227, 177, 89), (270, 70+ 140*i, 70, 70))
        py.draw.rect(screen, (227, 177, 89), (410, 70+ 140*i, 70, 70))
        py.draw.rect(screen, (227, 177, 89), (550, 70+ 140*i, 70, 70))
        py.draw.rect(screen, (227, 177, 89), (690, 70+ 140*i, 70, 70))
        
    

def load_images():
    global white_castle
    white_castle = py.image.load("C:\\Users\\Acer\\Desktop\\Python\\Chess\\images\\white castle.png")
    white_castle = py.transform.scale(white_castle, (60, 60))
    


def draw_pieces():
    screen.blit(white_castle, (200, 490))



running = True
while running:
    timer.tick(60)
    screen.fill((115, 73, 31))
    create_board()
    load_images()
    



    for event in py.event.get():
        if event.type == py.QUIT:
            running = False


    py.display.flip()



py.quit()