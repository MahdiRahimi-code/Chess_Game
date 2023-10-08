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


    

black_pieces = ['castle', 'horse', 'elephant' ,'queen', 'king', 'elephant', 'horse', 'castle',
                'soldier', 'soldier', 'soldier', 'soldier', 'soldier', 'soldier', 'soldier', 'soldier']
black_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
white_pieces = ['castle', 'horse', 'elephant' ,'queen', 'king', 'elephant', 'horse', 'castle',
                'soldier', 'soldier', 'soldier', 'soldier', 'soldier', 'soldier', 'soldier', 'soldier']
white_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]



def draw_pieces():
    for i in range(len(white_pieces)):
        if white_pieces[i] == 'soldier':
            screen.blit(white_soldier, (200 + white_locations[i][0]*70, 70 + white_locations[i][1]*70))

        elif white_pieces[i] == 'castle':
            screen.blit(white_castle, (200 + white_locations[i][0]*70, 70 + white_locations[i][1]*70))
        
        elif white_pieces[i] == 'horse':
            screen.blit(white_horse, (200 + white_locations[i][0]*70, 70 + white_locations[i][1]*70))

        elif white_pieces[i] == 'elephant':
            screen.blit(white_elephant, (200 + white_locations[i][0]*70, 70 + white_locations[i][1]*70))
        
        elif white_pieces[i] == 'queen':
            screen.blit(white_queen, (200 + white_locations[i][0]*70, 70 + white_locations[i][1]*70))
        
        elif white_pieces[i] == 'king':
            screen.blit(white_king, (200 + white_locations[i][0]*70, 70 + white_locations[i][1]*70))
        
        if turn == "white":
            if selected_piece[0] != -1:
                x = white_locations[selected_piece[0]][0]
                y = white_locations[selected_piece[0]][1]
                py.draw.rect(screen, 'red', (200+(x*70), 70+(y*70), 70, 70), 3)
        
    
    for i in range(len(black_pieces)):
        if black_pieces[i] == 'soldier':
            screen.blit(black_soldier, (200 + black_locations[i][0]*70, 70 + black_locations[i][1]*70))

        elif black_pieces[i] == 'castle':
            screen.blit(black_castle, (200 + black_locations[i][0]*70, 70 + black_locations[i][1]*70))
        
        elif black_pieces[i] == 'horse':
            screen.blit(black_horse, (200 + black_locations[i][0]*70, 70 + black_locations[i][1]*70))

        elif black_pieces[i] == 'elephant':
            screen.blit(black_elephant, (200 + black_locations[i][0]*70, 70 + black_locations[i][1]*70))
        
        elif black_pieces[i] == 'queen':
            screen.blit(black_queen, (200 + black_locations[i][0]*70, 70 + black_locations[i][1]*70))
        
        elif black_pieces[i] == 'king':
            screen.blit(black_king, (200 + black_locations[i][0]*70, 70 + black_locations[i][1]*70))

        if turn == "black":
            if selected_piece[0] != -1:
                x = white_locations[selected_piece[0]][0]
                y = white_locations[selected_piece[0]][1]
                py.draw.rect(screen, 'blue', (200+(x*70), 70+(y*70), 70, 70), 3)        


allowed_moves = []


lost_pices_white = []
lost_pices_black = []

def check_moves(selected_piece):
    if selected_piece[1] == 'soldier':
        check_soldier_moves(selected_piece)

    
        
def check_soldier_moves(selected_piece):
    if turn == 'white':
        enemies = black_locations
        friends = white_locations
        location = white_locations[selected_piece[0]]

        if location[1] == 6:
            if (location[0], location[1]-1) not in enemies and (location[0], location[1]-1) not in friends:
                allowed_moves.append((location[0], location[1]-1))
            if (location[0], location[1]-2) not in enemies and (location[0], location[1]-2) not in friends:
                allowed_moves.append((location[0], location[1]-2))
            if (location[0]+1, location[1]-1) in enemies:
                allowed_moves.append((location[0]+1, location[1]-1))
            if (location[0]-1, location[1]-1) in enemies:
                allowed_moves.append((location[0]-1, location[1]-1))
                
        else:
            if (location[0], location[1]-1) not in enemies and (location[0], location[1]-1) not in friends:
                allowed_moves.append((location[0], location[1]-1))
            if (location[0]+1, location[1]-1) in enemies:
                allowed_moves.append((location[0]+1, location[1]-1))
            if (location[0]-1, location[1]-1) in enemies:
                allowed_moves.append((location[0]-1, location[1]-1))


    




def draw_allowed_moves():
    if turn == 'white':
        for i in range(len(allowed_moves)):
            if allowed_moves[i] in black_locations:
                py.draw.rect(screen, 'red', (205+ 70*allowed_moves[i][0], 75+ 70*allowed_moves[i][1], 60, 60), 2)
            else:
                py.draw.rect(screen, (22, 250, 250), (205+ 70*allowed_moves[i][0], 75+ 70*allowed_moves[i][1], 60, 60), 2)
    else:
        for i in range(len(allowed_moves)):
            if allowed_moves[i] in white_locations:
                py.draw.rect(screen, 'red', (205+ 70*allowed_moves[i][0], 75+ 70*allowed_moves[i][1], 60, 60), 2)
            else:
                py.draw.rect(screen, (22, 250, 250), (205+ 70*allowed_moves[i][0], 75+ 70*allowed_moves[i][1], 60, 60), 2)
        


# white or black
turn = 'white'
selected_piece = [-1, '']

# variable for disselecting piece
alter = [-1 , -1]
running = True

while running:
    timer.tick(60)
    screen.fill((115, 73, 31))
    create_board()
    load_images()
    draw_pieces()

    if selected_piece[0] != -1:
        check_moves(selected_piece)
        draw_allowed_moves()



    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
            select_x = (event.pos[0] - 200) // 70
            select_y = (event.pos[1] - 70) // 70
            selected_coords = (select_x, select_y)

            if (turn == "white"):
                if (selected_coords in white_locations):
                    allowed_moves = []
                    index = white_locations.index(selected_coords)
                    selected_piece = [index, white_pieces[index]]
                    if alter == selected_piece:
                        alter = [-1, -1]
                        selected_piece = [-1, '']

                    alter = selected_piece

                if selected_coords in allowed_moves:
                    if selected_coords in black_locations:
                        allowed_moves = []
                        white_locations[index] = selected_coords
                        selected_piece = [-1, '']
                        index = black_locations.index(selected_coords)
                        lost_pices_black.append(black_pieces[index])
                        black_locations.pop(index)
                        black_pieces.pop(index)
                    else:
                        allowed_moves = []
                        white_locations[index] = selected_coords
                        selected_piece = [-1, '']
                        #turn = 'black'
                
                

                

                         


                   

                    


                    
                    

            

                    
            


    py.display.flip()



py.quit()