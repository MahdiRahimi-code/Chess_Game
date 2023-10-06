import pygame as py
import tkinter

py.init()
screen = py.display.set_mode((960, 700))
timer = py.time.Clock()

text = py.font.Font(None, 30)


def create_board():
    # black lines around the board
    py.draw.rect(screen, 'black', (198, 67, 564, 566), 3)
    py.draw.line(screen, 'black', (198, 0), (198, 700), 2)
    py.draw.line(screen, 'black', (760, 0), (760, 700), 2)

    # left and right rects
    py.draw.rect(screen, (99, 97, 90), (2, 2, 194, 698))
    py.draw.rect(screen, 'white', (764, 0, 194, 698))

    #corner texts
    screen.blit(text.render("White Lost Pieces", True, 'black'), (10, 20))
    screen.blit(text.render("Black Lost Pieces", True, 'black'), (770, 20))
    py.draw.line(screen, 'black', (0, 70), (960, 70), 2)

    for i in range(4):
        py.draw.rect(screen, (227, 177, 89), (200, 70+ 140*i, 70, 70))
        py.draw.rect(screen, (227, 177, 89), (340, 70+ 140*i, 70, 70))
        py.draw.rect(screen, (227, 177, 89), (480, 70+ 140*i, 70, 70))
        py.draw.rect(screen, (227, 177, 89), (620, 70+ 140*i, 70, 70))
        py.draw.rect(screen, (227, 177, 89), (270, 140+ 140*i, 70, 70))
        py.draw.rect(screen, (227, 177, 89), (410, 140+ 140*i, 70, 70))
        py.draw.rect(screen, (227, 177, 89), (550, 140+ 140*i, 70, 70))
        py.draw.rect(screen, (227, 177, 89), (690, 140+ 140*i, 70, 70))
        



def load_images():
    global white_castle, white_horse, white_elephant, white_queen, white_king, white_soldier
    white_castle = py.image.load("C:\\Users\\Acer\\Desktop\\Python\\Chess\\images\\white castle.png")
    white_castle = py.transform.scale(white_castle, (60, 60))
    white_horse = py.image.load("C:\\Users\\Acer\\Desktop\\Python\\Chess\\images\\white horse.png")
    white_horse = py.transform.scale(white_horse, (60, 60))
    white_elephant = py.image.load("C:\\Users\\Acer\\Desktop\\Python\\Chess\\images\\white elephant.png")
    white_elephant = py.transform.scale(white_elephant, (60, 60))
    white_queen = py.image.load("C:\\Users\\Acer\\Desktop\\Python\\Chess\\images\\white queen.png")
    white_queen = py.transform.scale(white_queen, (60, 60))
    white_king = py.image.load("C:\\Users\\Acer\\Desktop\\Python\\Chess\\images\\white king.png")
    white_king = py.transform.scale(white_king, (60, 60))
    white_soldier = py.image.load("C:\\Users\\Acer\\Desktop\\Python\\Chess\\images\\white soldier.png")
    white_soldier = py.transform.scale(white_soldier, (60, 60))

    global black_castle, black_horse, black_elephant, black_queen, black_king, black_soldier
    black_castle = py.image.load("C:\\Users\\Acer\\Desktop\\Python\\Chess\\images\\black castle.png")
    black_castle = py.transform.scale(black_castle, (60, 60))
    black_horse = py.image.load("C:\\Users\\Acer\\Desktop\\Python\\Chess\\images\\black horse.png")
    black_horse = py.transform.scale(black_horse, (60, 60))
    black_elephant = py.image.load("C:\\Users\\Acer\\Desktop\\Python\\Chess\\images\\black elephant.png")
    black_elephant = py.transform.scale(black_elephant, (60, 60))
    black_queen = py.image.load("C:\\Users\\Acer\\Desktop\\Python\\Chess\\images\\black queen.png")
    black_queen = py.transform.scale(black_queen, (60, 60))
    black_king = py.image.load("C:\\Users\\Acer\\Desktop\\Python\\Chess\\images\\black king.png")
    black_king = py.transform.scale(black_king, (60, 60))
    black_soldier = py.image.load("C:\\Users\\Acer\\Desktop\\Python\\Chess\\images\\black soldier.png")
    black_soldier = py.transform.scale(black_soldier, (60, 60))

    


def draw_pieces():
    screen.blit(white_castle, (200, 565))
    screen.blit(white_horse, (275, 565))
    screen.blit(white_elephant, (345, 565))
    screen.blit(white_queen, (415, 565))
    screen.blit(white_king, (485, 565))
    screen.blit(white_elephant, (555, 565))
    screen.blit(white_horse, (625, 565))
    screen.blit(white_castle, (695, 565))
    for i in range(8):
        screen.blit(white_soldier, (200+ 70*i, 495))

    screen.blit(black_castle, (200, 75))
    screen.blit(black_horse, (275, 75))
    screen.blit(black_elephant, (345, 75))
    screen.blit(black_queen, (415, 75))
    screen.blit(black_king, (485, 75))
    screen.blit(black_elephant, (555, 75))
    screen.blit(black_horse, (625, 75))
    screen.blit(black_castle, (695, 75))
    for i in range(8):
        screen.blit(black_soldier, (200+ 70*i, 145))



running = True
while running:
    timer.tick(60)
    screen.fill((115, 73, 31))
    create_board()
    load_images()
    draw_pieces()



    for event in py.event.get():
        if event.type == py.QUIT:
            running = False


    py.display.flip()



py.quit()