import pygame as py
import time
import tkinter
from tkinter import messagebox

py.init()
screen = py.display.set_mode((1100, 700))
timer = py.time.Clock()

font = py.font.Font(None, 30)
allowed_moves = []
lost_pieces_white = []
lost_pieces_black = []
white_total_moves = []
black_total_moves = []
checking_piece = []


black_pieces = ['castle', 'horse', 'elephant' ,'queen', 'king', 'elephant', 'horse', 'castle',
                'soldier', 'soldier', 'soldier', 'soldier', 'soldier', 'soldier', 'soldier', 'soldier']
black_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
white_pieces = ['castle', 'horse', 'elephant' ,'queen', 'king', 'elephant', 'horse', 'castle',
                'soldier', 'soldier', 'soldier', 'soldier', 'soldier', 'soldier', 'soldier', 'soldier']
white_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]



def create_board():
    # black lines around the board
    py.draw.rect(screen, 'black', (198, 67, 564, 566), 3)
    py.draw.line(screen, 'black', (198, 0), (198, 700), 2)
    py.draw.line(screen, 'black', (760, 0), (760, 700), 2)

    # left and right rects
    py.draw.rect(screen, (99, 97, 90), (2, 2, 194, 698))
    py.draw.rect(screen, 'white', (764, 0, 194, 698))

    #corner texts
    screen.blit(font.render("White Lost Pieces", True, 'black'), (10, 20))
    screen.blit(font.render("Black Lost Pieces", True, 'black'), (770, 20))
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
                py.draw.rect(screen, 'green', (200+(x*70), 70+(y*70), 70, 70), 3)
        
    
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
                x = black_locations[selected_piece[0]][0]
                y = black_locations[selected_piece[0]][1]
                py.draw.rect(screen, 'blue', (200+(x*70), 70+(y*70), 70, 70), 3)




def check_moves(selected):
    if selected[1] == 'soldier':
        check_soldier_moves(selected)
    elif selected[1] == 'horse':
        check_horse_moves(selected)
    elif selected[1] == 'elephant':
        check_elephant_moves(selected)
    elif selected[1] == 'castle':
        check_castle_moves(selected)
    elif selected[1] == 'queen':
        check_queen_moves(selected)
    elif selected[1] == 'king':
        check_king_moves(selected)
    
    # king can not be ommited
    for i in allowed_moves:
        if i==white_king_location or i==black_king_location:
            index = allowed_moves.index(i)
            allowed_moves.pop(index)
    


    
def check_soldier_moves(selected):
    if turn == 'white':
        enemies = black_locations
        friends = white_locations
        location = white_locations[selected[0]]

        if location[1] == 6:
            if (location[0], location[1]-1) not in enemies and (location[0], location[1]-1) not in friends \
                and (location[0], location[1]-1) not in allowed_moves:
                allowed_moves.append((location[0], location[1]-1))
            if (location[0], location[1]-2) not in enemies and (location[0], location[1]-2) not in friends \
                and (location[0], location[1]-2) not in allowed_moves:
                allowed_moves.append((location[0], location[1]-2))
            if (location[0]+1, location[1]-1) in enemies and (location[0]+1, location[1]-1) not in allowed_moves:
                allowed_moves.append((location[0]+1, location[1]-1))
            if (location[0]-1, location[1]-1) in enemies and (location[0]-1, location[1]-1) not in allowed_moves:
                allowed_moves.append((location[0]-1, location[1]-1))
                
        else:
            if (location[1] - 1 >= 0):
                if (location[0], location[1]-1) not in enemies and (location[0], location[1]-1) not in friends \
                    and (location[0], location[1]-1) not in allowed_moves:
                    allowed_moves.append((location[0], location[1]-1))
                if (location[0]+1, location[1]-1) in enemies and (location[0]+1, location[1]-1) not in allowed_moves:
                    allowed_moves.append((location[0]+1, location[1]-1))
                if (location[0]-1, location[1]-1) in enemies and (location[0]-1, location[1]-1) not in allowed_moves:
                    allowed_moves.append((location[0]-1, location[1]-1))
    
    elif turn == 'black':
        enemies = white_locations
        friends = black_locations
        location = black_locations[selected[0]]

        if location[1] == 1:
            if (location[0], location[1]+1) not in enemies and (location[0], location[1]+1) not in friends \
                and (location[0], location[1]+1) not in allowed_moves:
                allowed_moves.append((location[0], location[1]+1))
            if (location[0], location[1]+2) not in enemies and (location[0], location[1]+2) not in friends \
                and (location[0], location[1]+2) not in allowed_moves:
                allowed_moves.append((location[0], location[1]+2))
            if (location[0]-1, location[1]+1) in enemies and (location[0]-1, location[1]+1) not in allowed_moves:
                allowed_moves.append((location[0]-1, location[1]+1))
            if (location[0]+1, location[1]+1) in enemies and (location[0]+1, location[1]+1) not in allowed_moves:
                allowed_moves.append((location[0]+1, location[1]+1))
                
        else:
            if (location[1] + 1 <= 7):
                if (location[0], location[1]+1) not in enemies and (location[0], location[1]+1) not in friends \
                    and (location[0], location[1]+1) not in allowed_moves:
                    allowed_moves.append((location[0], location[1]+1))
                if (location[0]-1, location[1]+1) in enemies and (location[0]-1, location[1]+1) not in allowed_moves:
                    allowed_moves.append((location[0]-1, location[1]+1))
                if (location[0]+1, location[1]+1) in enemies and (location[0]+1, location[1]+1) not in allowed_moves:
                    allowed_moves.append((location[0]+1, location[1]+1))




def check_king_moves(selected):
    if turn == "white":
        x = white_locations[selected[0]][0]
        y = white_locations[selected[0]][1]
        moves = [(1, -1), (1, 0), (1, 1), (0, -1),
        (0, 1), (-1, -1), (-1, 0), (-1, 1)]

        for i in range(len(moves)):
            if (x+moves[i][0], y+moves[i][1]) not in white_locations:
                if (x+moves[i][0])>=0 and (x+moves[i][0])<=7 and (y+moves[i][1])<=7 \
                    and (y+moves[i][1])>=0:
                    if (x+moves[i][0], y+moves[i][1]) not in allowed_moves:
                        allowed_moves.append((x+moves[i][0], y+moves[i][1]))
    if turn == "black":
        x = black_locations[selected[0]][0]
        y = black_locations[selected[0]][1]
        moves = [(1, -1), (1, 0), (1, 1), (0, -1),
        (0, 1), (-1, -1), (-1, 0), (-1, 1)]

        for i in range(len(moves)):
            if (x+moves[i][0], y+moves[i][1]) not in black_locations:
                if (x+moves[i][0])>=0 and (x+moves[i][0])<=7 and (y+moves[i][1])<=7 \
                    and (y+moves[i][1])>=0:
                    if (x+moves[i][0], y+moves[i][1]) not in allowed_moves:
                        allowed_moves.append((x+moves[i][0], y+moves[i][1]))




def check_horse_moves(selected):
    if turn == "white":
        moves = [(2, -1), (-2, -1), (1, -2), (-1, -2),
                (2, 1), (-2, 1), (1, 2), (-1, 2)]
        
        location = white_locations[selected[0]]

        for i in range(len(moves)):
            x = location[0] + moves[i][0]
            y = location[1] + moves[i][1]
            if (x,y) not in white_locations and (x>=0 and y<=7 and x<=7 and y>=0) and (x, y) not in allowed_moves:
                allowed_moves.append((x, y))

    if turn == "black":
        moves = [(2, -1), (-2, -1), (1, -2), (-1, -2),
                (2, 1), (-2, 1), (1, 2), (-1, 2)]
        
        location = black_locations[selected[0]]

        for i in range(len(moves)):
            x = location[0] + moves[i][0]
            y = location[1] + moves[i][1]
            if (x,y) not in black_locations and (x>=0 and y<=7 and x<=7 and y>=0) and (x, y) not in allowed_moves:
                allowed_moves.append((x, y))




def check_elephant_moves(selected):
    if turn == "white":
        enemies = black_locations
        friends = white_locations
        
        x = white_locations[selected[0]][0]
        y = white_locations[selected[0]][1]

        x1, y1 = x+1, y-1
        while (x1, y1) not in friends and x1<=7 and y1>=0 and (x1, y1) not in allowed_moves:
            if (x1, y1) in enemies:
                allowed_moves.append((x1, y1))
                break
            allowed_moves.append((x1, y1))
            x1 = x1 + 1
            y1 = y1 - 1
        
        x2, y2 = x-1, y-1
        while (x2, y2) not in friends and x2>=0 and y2>=0 and (x2, y2) not in allowed_moves:
            if (x2, y2) in enemies:
                allowed_moves.append((x2, y2))
                break
            allowed_moves.append((x2, y2))
            x2 = x2 - 1
            y2 = y2 - 1
        
        x3, y3 = x-1, y+1
        while (x3, y3) not in friends and x3>=0 and y3<=7 and (x3, y3) not in allowed_moves:
            if (x3, y3) in enemies:
                allowed_moves.append((x3, y3))
                break
            allowed_moves.append((x3, y3))
            x3 = x3 - 1
            y3 = y3 + 1
        
        x4, y4 = x+1, y+1
        while (x4, y4) not in friends and x4<=7 and y4<=7 and (x4, y4) not in allowed_moves:
            if (x4, y4) in enemies:
                allowed_moves.append((x4, y4))
                break
            allowed_moves.append((x4, y4))
            x4 = x4 + 1
            y4 = y4 + 1
    
    if turn == "black":
        enemies = white_locations
        friends = black_locations
        
        x = black_locations[selected[0]][0]
        y = black_locations[selected[0]][1]

        x1, y1 = x+1, y-1
        while (x1, y1) not in friends and x1<=7 and y1>=0 and (x1, y1) not in allowed_moves:
            if (x1, y1) in enemies:
                allowed_moves.append((x1, y1))
                break
            allowed_moves.append((x1, y1))
            x1 = x1 + 1
            y1 = y1 - 1
        
        x2, y2 = x-1, y-1
        while (x2, y2) not in friends and x2>=0 and y2>=0 and (x2, y2) not in allowed_moves:
            if (x2, y2) in enemies:
                allowed_moves.append((x2, y2))
                break
            allowed_moves.append((x2, y2))
            x2 = x2 - 1
            y2 = y2 - 1
        
        x3, y3 = x-1, y+1
        while (x3, y3) not in friends and x3>=0 and y3<=7 and (x3, y3) not in allowed_moves:
            if (x3, y3) in enemies:
                allowed_moves.append((x3, y3))
                break
            allowed_moves.append((x3, y3))
            x3 = x3 - 1
            y3 = y3 + 1
        
        x4, y4 = x+1, y+1
        while (x4, y4) not in friends and x4<=7 and y4<=7 and (x4, y4) not in allowed_moves:
            if (x4, y4) in enemies:
                allowed_moves.append((x4, y4))
                break
            allowed_moves.append((x4, y4))
            x4 = x4 + 1
            y4 = y4 + 1




def check_castle_moves(selected):
    if turn == "white":
        x = white_locations[selected[0]][0]
        y = white_locations[selected[0]][1]

        x1 = x - 1
        while (x1, y) not in white_locations and x1>=0:
            if (x1, y) in black_locations:
                allowed_moves.append((x1, y))
                break
            allowed_moves.append((x1, y))
            x1 -= 1
        
        x2 = x + 1
        while (x2, y) not in white_locations and x2<=7:
            if (x2, y) in black_locations:
                allowed_moves.append((x2, y))
                break
            allowed_moves.append((x2, y))
            x2 += 1
        
        y1 = y - 1
        while (x, y1) not in white_locations and y1>=0:
            if (x, y1) in black_locations:
                allowed_moves.append((x, y1))
                break
            allowed_moves.append((x, y1))
            y1 -= 1
        
        y2 = y + 1
        while (x, y2) not in white_locations and y2<=7:
            if (x, y2) in black_locations:
                allowed_moves.append((x, y2))
                break
            allowed_moves.append((x, y2))
            y2 += 1
    
    if turn == "black":
        x = black_locations[selected[0]][0]
        y = black_locations[selected[0]][1]

        x1 = x - 1
        while (x1, y) not in black_locations and x1>=0:
            if (x1, y) in white_locations:
                allowed_moves.append((x1, y))
                break
            allowed_moves.append((x1, y))
            x1 -= 1
        
        x2 = x + 1
        while (x2, y) not in black_locations and x2<=7:
            if (x2, y) in white_locations:
                allowed_moves.append((x2, y))
                break
            allowed_moves.append((x2, y))
            x2 += 1
        
        y1 = y - 1
        while (x, y1) not in black_locations and y1>=0:
            if (x, y1) in white_locations:
                allowed_moves.append((x, y1))
                break
            allowed_moves.append((x, y1))
            y1 -= 1
        
        y2 = y + 1
        while (x, y2) not in black_locations and y2<=7:
            if (x, y2) in white_locations:
                allowed_moves.append((x, y2))
                break
            allowed_moves.append((x, y2))
            y2 += 1




def check_queen_moves(selected):
    check_castle_moves(selected)
    check_elephant_moves(selected)




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
        
    if turn == 'black':
        for i in range(len(allowed_moves)):
            if allowed_moves[i] in white_locations:
                py.draw.rect(screen, 'red', (205+ 70*allowed_moves[i][0], 75+ 70*allowed_moves[i][1], 60, 60), 2)
            else:
                py.draw.rect(screen, (22, 250, 250), (205+ 70*allowed_moves[i][0], 75+ 70*allowed_moves[i][1], 60, 60), 2)
    else:
        for i in range(len(allowed_moves)):
            if allowed_moves[i] in black_locations:
                py.draw.rect(screen, 'red', (205+ 70*allowed_moves[i][0], 75+ 70*allowed_moves[i][1], 60, 60), 2)
            else:
                py.draw.rect(screen, (22, 250, 250), (205+ 70*allowed_moves[i][0], 75+ 70*allowed_moves[i][1], 60, 60), 2)




def draw_lost_pieces():
    for i in range(len(lost_pieces_white)):
        if lost_pieces_white[i] == 'soldier':
            if i>9:
                screen.blit(white_soldier, (100, 75 + 60*(i-10)))
            else:
                screen.blit(white_soldier, (5, 75 + 60*i))

        elif lost_pieces_white[i] == 'castle':
            if i>9:
                screen.blit(white_castle, (100, 75 + 60*(i-10)))
            else:
                screen.blit(white_castle, (5, 75 + 60*i))
        
        elif lost_pieces_white[i] == 'horse':
            if i>9:
                screen.blit(white_horse, (100, 75 + 60*(i-10)))
            else:
                screen.blit(white_horse, (5, 75 + 60*i))

        elif lost_pieces_white[i] == 'elephant':
            if i>9:
                screen.blit(white_elephant, (100, 75 + 60*(i-10)))
            else:
                screen.blit(white_elephant, (5, 75 + 60*i))
        
        elif lost_pieces_white[i] == 'queen':
            if i>9:
                screen.blit(white_queen, (100, 75 + 60*(i-10)))
            else:
                screen.blit(white_queen, (5, 75 + 60*i))
    
    for i in range(len(lost_pieces_black)):
        if lost_pieces_black[i] == 'soldier':
            if i>9:
                screen.blit(black_soldier, (860, 75 + 60*(i-10)))
            else:
                screen.blit(black_soldier, (785, 75 + 60*i))

        elif lost_pieces_black[i] == 'castle':
            if i>9:
                screen.blit(black_castle, (860, 75 + 60*(i-10)))
            else:
                screen.blit(black_castle, (785, 75 + 60*i))
        
        elif lost_pieces_black[i] == 'horse':
            if i>9:
                screen.blit(black_horse, (860, 75 + 60*(i-10)))
            else:
                screen.blit(black_horse, (785, 75 + 60*i))

        elif lost_pieces_black[i] == 'elephant':
            if i>9:
                screen.blit(black_elephant, (860, 75 + 60*(i-10)))
            else:
                screen.blit(black_elephant, (785, 75 + 60*i))
        
        elif lost_pieces_black[i] == 'queen':
            if i>9:
                screen.blit(black_queen, (860, 75 + 60*(i-10)))
            else:
                screen.blit(black_queen, (785, 75 + 60*i))




def check_white_total():
    for i in range(len(white_pieces)):
        selected = [i, white_pieces[i]]
        if selected[1] == 'soldier':
            enemies = black_locations
            friends = white_locations
            location = white_locations[selected[0]]

            if location[1] == 6:
                if (location[0], location[1]-1) not in enemies and (location[0], location[1]-1) not in friends\
                and (location[0], location[1]-1) not in white_total_moves:
                    white_total_moves.append((location[0], location[1]-1))
                if (location[0], location[1]-2) not in enemies and (location[0], location[1]-2) not in friends\
                and (location[0], location[1]-2) not in white_total_moves:
                    white_total_moves.append((location[0], location[1]-2))
                if (location[0]+1, location[1]-1) in enemies and (location[0]+1, location[1]-1) not in white_total_moves:
                    white_total_moves.append((location[0]+1, location[1]-1))
                if (location[0]-1, location[1]-1) in enemies and (location[0]-1, location[1]-1) not in white_total_moves:
                    white_total_moves.append((location[0]-1, location[1]-1))
                    
            else:
                if (location[1] - 1 >= 0):
                    if (location[0], location[1]-1) not in enemies and (location[0], location[1]-1) not in friends\
                    and (location[0], location[1]-1) not in white_total_moves:
                        white_total_moves.append((location[0], location[1]-1))
                    if (location[0]+1, location[1]-1) in enemies and (location[0]+1, location[1]-1) not in white_total_moves:
                        white_total_moves.append((location[0]+1, location[1]-1))
                    if (location[0]-1, location[1]-1) in enemies and (location[0]-1, location[1]-1) not in white_total_moves:
                        white_total_moves.append((location[0]-1, location[1]-1))
        elif selected[1] == 'castle':
            x = white_locations[selected[0]][0]
            y = white_locations[selected[0]][1]

            x1 = x - 1
            found = False
            while (x1, y) not in white_locations and x1>=0 and not found:
                if (x1, y) in black_locations:
                    found = True
                if (x1, y) not in white_total_moves:
                    white_total_moves.append((x1, y))
                x1 -= 1
            
            x2 = x + 1
            found = False
            while (x2, y) not in white_locations and x2<=7 and not found:
                if (x2, y) in black_locations:
                    found = True
                if (x2, y) not in white_total_moves:
                    white_total_moves.append((x2, y))
                x2 += 1
            
            y1 = y - 1
            found = False
            while (x, y1) not in white_locations and y1>=0 and not found:                
                if (x, y1) in black_locations:
                    found = True
                if (x, y1) not in white_total_moves:
                    white_total_moves.append((x, y1))
                y1 -= 1
            
            y2 = y + 1
            found = False
            while (x, y2) not in white_locations and y2<=7 and not found:                
                if (x, y2) in black_locations:
                    found = True
                if (x, y2) not in white_total_moves:
                    white_total_moves.append((x, y2))
                y2 += 1
        elif selected[1] == 'horse':
            moves = [(2, -1), (-2, -1), (1, -2), (-1, -2),
                (2, 1), (-2, 1), (1, 2), (-1, 2)]
        
            location = white_locations[selected[0]]

            for i in range(len(moves)):
                x = location[0] + moves[i][0]
                y = location[1] + moves[i][1]
                if (x,y) not in white_locations and (x>=0 and y<=7 and x<=7 and y>=0) and (x,y) not in white_total_moves:
                    white_total_moves.append((x, y))
        elif selected[1] == 'elephant':
            enemies = black_locations
            friends = white_locations
            
            x = white_locations[selected[0]][0]
            y = white_locations[selected[0]][1]

            x1, y1 = x+1, y-1
            found = False
            while (x1, y1) not in friends and x1<=7 and y1>=0 and not found:                
                if (x1, y1) in enemies:
                    found = True
                if (x1, y1) not in white_total_moves:    
                    white_total_moves.append((x1, y1))
                x1 = x1 + 1
                y1 = y1 - 1
            
            x2, y2 = x-1, y-1
            found = False
            while (x2, y2) not in friends and x2>=0 and y2>=0 and not found:
                if (x2, y2) in enemies:
                    found = True
                if (x2, y2) not in white_total_moves:    
                    white_total_moves.append((x2, y2))
                x2 = x2 - 1
                y2 = y2 - 1
            
            x3, y3 = x-1, y+1
            found = False
            while (x3, y3) not in friends and x3>=0 and y3<=7 and not found:                            
                if (x3, y3) in enemies:
                    found = True
                if (x3, y3) not in white_total_moves:    
                    white_total_moves.append((x3, y3))
                x3 = x3 - 1
                y3 = y3 + 1
            
            x4, y4 = x+1, y+1
            found = False
            while (x4, y4) not in friends and x4<=7 and y4<=7 and not found:                
                if (x4, y4) in enemies:
                    found = True
                if (x4, y4) not in white_total_moves:    
                    white_total_moves.append((x4, y4))
                x4 = x4 + 1
                y4 = y4 + 1
        elif selected[1] == 'queen':
            x = white_locations[selected[0]][0]
            y = white_locations[selected[0]][1]

            x1 = x - 1
            found = False
            while (x1, y) not in white_locations and x1>=0 and not found:
                if (x1, y) in black_locations:
                    found = True
                if (x1, y) not in white_total_moves:
                    white_total_moves.append((x1, y))
                x1 -= 1
            
            x2 = x + 1
            found = False
            while (x2, y) not in white_locations and x2<=7 and not found:
                if (x2, y) in black_locations:
                    found = True
                if (x2, y) not in white_total_moves:
                    white_total_moves.append((x2, y))
                x2 += 1
            
            y1 = y - 1
            found = False
            while (x, y1) not in white_locations and y1>=0 and not found:                
                if (x, y1) in black_locations:
                    found = True
                if (x, y1) not in white_total_moves:
                    white_total_moves.append((x, y1))
                y1 -= 1
            
            y2 = y + 1
            found = False
            while (x, y2) not in white_locations and y2<=7 and not found:                
                if (x, y2) in black_locations:
                    found = True
                if (x, y2) not in white_total_moves:
                    white_total_moves.append((x, y2))
                y2 += 1                    

            enemies = black_locations
            friends = white_locations
            
            x = white_locations[selected[0]][0]
            y = white_locations[selected[0]][1]

            x1, y1 = x+1, y-1
            found = False
            while (x1, y1) not in friends and x1<=7 and y1>=0 and not found:                
                if (x1, y1) in enemies:
                    found = True
                if (x1, y1) not in white_total_moves:    
                    white_total_moves.append((x1, y1))
                x1 = x1 + 1
                y1 = y1 - 1
            
            x2, y2 = x-1, y-1
            found = False
            while (x2, y2) not in friends and x2>=0 and y2>=0 and not found:
                if (x2, y2) in enemies:
                    found = True
                if (x2, y2) not in white_total_moves:    
                    white_total_moves.append((x2, y2))
                x2 = x2 - 1
                y2 = y2 - 1
            
            x3, y3 = x-1, y+1
            found = False
            while (x3, y3) not in friends and x3>=0 and y3<=7 and not found:                            
                if (x3, y3) in enemies:
                    found = True
                if (x3, y3) not in white_total_moves:    
                    white_total_moves.append((x3, y3))
                x3 = x3 - 1
                y3 = y3 + 1
            
            x4, y4 = x+1, y+1
            found = False
            while (x4, y4) not in friends and x4<=7 and y4<=7 and not found:                
                if (x4, y4) in enemies:
                    found = True
                if (x4, y4) not in white_total_moves:    
                    white_total_moves.append((x4, y4))
                x4 = x4 + 1
                y4 = y4 + 1
        elif selected[1] == 'king':
            x = white_locations[selected[0]][0]
            y = white_locations[selected[0]][1]
            moves = [(1, -1), (1, 0), (1, 1), (0, -1),
            (0, 1), (-1, -1), (-1, 0), (-1, 1)]

            for i in range(len(moves)):
                if (x+moves[i][0], y+moves[i][1]) not in white_locations:
                    if (x+moves[i][0])>=0 and (x+moves[i][0])<=7 and (y+moves[i][1])<=7 \
                        and (y+moves[i][1])>=0:
                        if (x+moves[i][0], y+moves[i][1]) not in white_total_moves:
                            white_total_moves.append((x+moves[i][0], y+moves[i][1]))




def check_black_total():
    for i in range(len(black_pieces)):
        selected = [i, black_pieces[i]]
        if selected[1] == 'soldier':
            enemies = white_locations
            friends = black_locations
            location = black_locations[selected[0]]

            if location[1] == 6:
                if (location[0], location[1]-1) not in enemies and (location[0], location[1]-1) not in friends\
                and (location[0], location[1]-1) not in black_total_moves:
                    black_total_moves.append((location[0], location[1]-1))
                if (location[0], location[1]-2) not in enemies and (location[0], location[1]-2) not in friends\
                and (location[0], location[1]-2) not in black_total_moves:
                    black_total_moves.append((location[0], location[1]-2))
                if (location[0]+1, location[1]-1) in enemies and (location[0]+1, location[1]-1) not in black_total_moves:
                    black_total_moves.append((location[0]+1, location[1]-1))
                if (location[0]-1, location[1]-1) in enemies and (location[0]-1, location[1]-1) not in black_total_moves:
                    black_total_moves.append((location[0]-1, location[1]-1))
                    
            else:
                if (location[1] - 1 >= 0):
                    if (location[0], location[1]-1) not in enemies and (location[0], location[1]-1) not in friends\
                    and (location[0], location[1]-1) not in black_total_moves:
                        black_total_moves.append((location[0], location[1]-1))
                    if (location[0]+1, location[1]-1) in enemies and (location[0]+1, location[1]-1) not in black_total_moves:
                        black_total_moves.append((location[0]+1, location[1]-1))
                    if (location[0]-1, location[1]-1) in enemies and (location[0]-1, location[1]-1) not in black_total_moves:
                        black_total_moves.append((location[0]-1, location[1]-1))
        elif selected[1] == 'castle':
            x = black_locations[selected[0]][0]
            y = black_locations[selected[0]][1]

            x1 = x - 1
            found = False
            while (x1, y) not in black_locations and x1>=0 and not found:
                if (x1, y) in white_locations:
                    found = True
                if (x1, y) not in black_total_moves:
                    black_total_moves.append((x1, y))
                x1 -= 1
            
            x2 = x + 1
            found = False
            while (x2, y) not in black_locations and x2<=7 and not found:
                if (x2, y) in white_locations:
                    found = True
                if (x2, y) not in black_total_moves:
                    black_total_moves.append((x2, y))
                x2 += 1
            
            y1 = y - 1
            found = False
            while (x, y1) not in black_locations and y1>=0 and not found:                
                if (x, y1) in white_locations:
                    found = True
                if (x, y1) not in black_total_moves:
                    black_total_moves.append((x, y1))
                y1 -= 1
            
            y2 = y + 1
            found = False
            while (x, y2) not in black_locations and y2<=7 and not found:                
                if (x, y2) in white_locations:
                    found = True
                if (x, y2) not in black_total_moves:
                    black_total_moves.append((x, y2))
                y2 += 1
        elif selected[1] == 'horse':
            moves = [(2, -1), (-2, -1), (1, -2), (-1, -2),
                (2, 1), (-2, 1), (1, 2), (-1, 2)]
        
            location = black_locations[selected[0]]

            for i in range(len(moves)):
                x = location[0] + moves[i][0]
                y = location[1] + moves[i][1]
                if (x,y) not in black_locations and (x>=0 and y<=7 and x<=7 and y>=0) and (x,y) not in black_total_moves:
                    black_total_moves.append((x, y))
        elif selected[1] == 'elephant':
            enemies = white_locations
            friends = black_locations
            
            x = black_locations[selected[0]][0]
            y = black_locations[selected[0]][1]

            x1, y1 = x+1, y-1
            found = False
            while (x1, y1) not in friends and x1<=7 and y1>=0 and not found:                
                if (x1, y1) in enemies:
                    found = True
                if (x1, y1) not in black_total_moves:    
                    black_total_moves.append((x1, y1))
                x1 = x1 + 1
                y1 = y1 - 1
            
            x2, y2 = x-1, y-1
            found = False
            while (x2, y2) not in friends and x2>=0 and y2>=0 and not found:
                if (x2, y2) in enemies:
                    found = True
                if (x2, y2) not in black_total_moves:    
                    black_total_moves.append((x2, y2))
                x2 = x2 - 1
                y2 = y2 - 1
            
            x3, y3 = x-1, y+1
            found = False
            while (x3, y3) not in friends and x3>=0 and y3<=7 and not found:                            
                if (x3, y3) in enemies:
                    found = True
                if (x3, y3) not in black_total_moves:    
                    black_total_moves.append((x3, y3))
                x3 = x3 - 1
                y3 = y3 + 1
            
            x4, y4 = x+1, y+1
            found = False
            while (x4, y4) not in friends and x4<=7 and y4<=7 and not found:                
                if (x4, y4) in enemies:
                    found = True
                if (x4, y4) not in black_total_moves:    
                    black_total_moves.append((x4, y4))
                x4 = x4 + 1
                y4 = y4 + 1
        elif selected[1] == 'queen':
            x = black_locations[selected[0]][0]
            y = black_locations[selected[0]][1]

            x1 = x - 1
            found = False
            while (x1, y) not in black_locations and x1>=0 and not found:
                if (x1, y) in white_locations:
                    found = True
                if (x1, y) not in black_total_moves:
                    black_total_moves.append((x1, y))
                x1 -= 1
            
            x2 = x + 1
            found = False
            while (x2, y) not in black_locations and x2<=7 and not found:
                if (x2, y) in white_locations:
                    found = True
                if (x2, y) not in black_total_moves:
                    black_total_moves.append((x2, y))
                x2 += 1
            
            y1 = y - 1
            found = False
            while (x, y1) not in black_locations and y1>=0 and not found:                
                if (x, y1) in white_locations:
                    found = True
                if (x, y1) not in black_total_moves:
                    black_total_moves.append((x, y1))
                y1 -= 1
            
            y2 = y + 1
            found = False
            while (x, y2) not in black_locations and y2<=7 and not found:                
                if (x, y2) in white_locations:
                    found = True
                if (x, y2) not in black_total_moves:
                    black_total_moves.append((x, y2))
                y2 += 1                    

            enemies = white_locations
            friends = black_locations
            
            x = black_locations[selected[0]][0]
            y = black_locations[selected[0]][1]

            x1, y1 = x+1, y-1
            found = False
            while (x1, y1) not in friends and x1<=7 and y1>=0 and not found:                
                if (x1, y1) in enemies:
                    found = True
                if (x1, y1) not in black_total_moves:    
                    black_total_moves.append((x1, y1))
                x1 = x1 + 1
                y1 = y1 - 1
            
            x2, y2 = x-1, y-1
            found = False
            while (x2, y2) not in friends and x2>=0 and y2>=0 and not found:
                if (x2, y2) in enemies:
                    found = True
                if (x2, y2) not in black_total_moves:    
                    black_total_moves.append((x2, y2))
                x2 = x2 - 1
                y2 = y2 - 1
            
            x3, y3 = x-1, y+1
            found = False
            while (x3, y3) not in friends and x3>=0 and y3<=7 and not found:                            
                if (x3, y3) in enemies:
                    found = True
                if (x3, y3) not in black_total_moves:    
                    black_total_moves.append((x3, y3))
                x3 = x3 - 1
                y3 = y3 + 1
            
            x4, y4 = x+1, y+1
            found = False
            while (x4, y4) not in friends and x4<=7 and y4<=7 and not found:                
                if (x4, y4) in enemies:
                    found = True
                if (x4, y4) not in black_total_moves:    
                    black_total_moves.append((x4, y4))
                x4 = x4 + 1
                y4 = y4 + 1
        elif selected[1] == 'king':
            x = black_locations[selected[0]][0]
            y = black_locations[selected[0]][1]
            moves = [(1, -1), (1, 0), (1, 1), (0, -1),
            (0, 1), (-1, -1), (-1, 0), (-1, 1)]

            for i in range(len(moves)):
                if (x+moves[i][0], y+moves[i][1]) not in black_locations:
                    if (x+moves[i][0])>=0 and (x+moves[i][0])<=7 and (y+moves[i][1])<=7 \
                        and (y+moves[i][1])>=0:
                        if (x+moves[i][0], y+moves[i][1]) not in black_total_moves:
                            black_total_moves.append((x+moves[i][0], y+moves[i][1]))




def check_total_moves():
    check_white_total()
    check_black_total()



color1 = 'red'  # First color
color2 = 'blue'  # Second color
current_color = color1
flash_interval = 500  # Flash interval in milliseconds
last_flash_time = 0
def draw_check():
    global last_flash_time, flash_interval ,current_color , color1 , color2
    
    white_king_location = ()
    for i in range(len(white_locations)):
        if white_pieces[i] == "king":
            white_king_location = white_locations[i]
            break
    
    if white_check == True:
        current_time = py.time.get_ticks()
        if current_time - last_flash_time >= flash_interval:
                
            if current_color == color1:
                current_color = color2
            else:
                current_color = color1
                    
            last_flash_time = current_time

        py.draw.rect(screen, current_color, (200+ 70*white_king_location[0], 68+ 70*white_king_location[1], 70, 70), 4)
    



    for i in range(len(black_locations)):
        if black_pieces[i] == "king":
            black_king_location = black_locations[i]
            break

    if black_check == True:
        current_time = py.time.get_ticks()
        if current_time - last_flash_time >= flash_interval:
                
            if current_color == color1:
                current_color = color2
            else:
                current_color = color1
                    
            last_flash_time = current_time

        py.draw.rect(screen, current_color, (200+ 70*black_king_location[0], 68+ 70*black_king_location[1], 70, 70), 4)

        
white_king_location = ()
black_king_location = ()


def check_king_check():
    global white_check, black_check
    global white_king_location, black_king_location

    white_index = -1
    for i in range(len(white_pieces)):
            if white_pieces[i] == "king":
                white_index=i
                break
    white_king_location = white_locations[white_index]        
    if (white_king_location) in black_total_moves:
        white_check = True
    else:
        white_check = False


    black_index = -1
    for i in range(len(black_pieces)):
        if black_pieces[i] == "king":
            black_index=i
            break
    black_king_location = black_locations[black_index]
    if (black_king_location) in white_total_moves:
        black_check = True
    else:
        black_check = False



white_win = False
black_win = False
check_counter = 8


new_font = py.font.Font(None, 60)


# white or black
turn = 'white'
selected_piece = [-1, '']

# variable for disselecting piece
alter = [-1 , -1]

running = True
white_check = False
black_check = False




while running and black_win == False  and  white_win == False:
    text_surface = new_font.render("you are check _ " + str(check_counter), True, "white", "black")
    textrect = text_surface.get_rect()
    textrect.center = (480, 40)
    timer.tick(60)
    screen.fill((115, 73, 31))
    create_board()
    load_images()
    draw_pieces()
    draw_check()
    draw_lost_pieces()
    check_total_moves()
    check_king_check()



    s = py.image.load("C:\\Users\\AceR\\Desktop\\python\\Chess\\images\\surrender.png")
    surrender = py.transform.scale(s, (80, 80))
    screen.blit(surrender, (980, 200))
    

    
    if (white_check == True) and check_counter == 0:  
        text_surface2 = new_font.render("black won the game", True, "white", "black")
        textrect2 = text_surface2.get_rect()
        textrect2.center = (480, 400)
        screen.blit(text_surface2, textrect2)
        for event in py.event.get():            
            if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
                black_win = True
    if (black_check == True) and check_counter == 0:
        text_surface2 = new_font.render("white won the game", True, "white", "black")
        textrect2 = text_surface2.get_rect()
        textrect2.center = (480, 400)
        screen.blit(text_surface2, textrect2)
        for event in py.event.get():            
            if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
                white_win = True


    if turn == "white":
        py.draw.rect(screen, 'gold', (200, 640, 560, 70))
    elif turn == "black":
        py.draw.rect(screen, 'gold', (200, 0, 560, 60))
    

    if selected_piece[0] != -1:
        check_moves(selected_piece)
        draw_allowed_moves()

    # blit the text to show you are check
    if (black_check == True and selected_piece == [-1, '']) or (white_check == True and selected_piece == [-1, '']):
        screen.blit(text_surface, textrect)

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        
        if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
            select_x = (event.pos[0] - 200) // 70
            select_y = (event.pos[1] - 70) // 70
            selected_coords = (select_x, select_y)

            if (turn == "white"):
                if selected_coords == (11,2):
                    result = messagebox.askyesno("Surrender", "Are you sure?\nYou will lose the game")
                    if result:
                        black_win = True
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
                        white_total_moves = []
                        black_total_moves = []
                        previous_location = white_locations[index]
                        white_locations[index] = selected_coords
                        if white_pieces[index] == 'king':
                            white_king_location = white_locations[index]
                        allowed_moves = []

                        index2 = black_locations.index(selected_coords)
                        lost = black_locations.pop(index2)
                        lost_piece = black_pieces.pop(index2)                        
                        lost_pieces_black.append(lost_piece)

                        selected_piece = [-1, '']
                        check_total_moves()
                        check_king_check()
                        if white_check==True:
                            black_locations.append(lost)
                            black_pieces.append(lost_piece)
                            lost_pieces_black.pop(black_pieces[index2])
                            white_locations[index] = previous_location
                            if white_pieces[index] == 'king':
                                white_king_location = previous_location
                            selected_piece = [-1, '']
                            check_counter -= 1
                        else:
                            white_locations[index] = selected_coords
                            turn = 'black'
                            check_counter = 8
                    else:                                                                            
                        white_total_moves = []
                        black_total_moves = []
                        previous_location = white_locations[index]
                        white_locations[index] = selected_coords
                        if white_pieces[index] == 'king':
                            white_king_location = white_locations[index]
                        allowed_moves = []
                        selected_piece = [-1, '']
                        check_total_moves()
                        check_king_check()
                        if white_check==True:
                            white_locations[index] = previous_location
                            if white_pieces[index] == 'king':
                                white_king_location = previous_location
                            selected_piece = [-1, '']
                            white_total_moves = []
                            black_total_moves = []
                            check_total_moves()
                            check_king_check()
                            check_counter -= 1
                        else:
                            selected_piece = [-1, '']
                            turn = 'black'
                            check_counter = 8

            
            if (turn == "black"):
                if selected_coords == (11,2):
                    result = messagebox.askyesno("Surrender", "Are you sure?\nYou will lose the game")
                    if result:
                        white_win = True
                if (selected_coords in black_locations):
                    allowed_moves = []
                    index = black_locations.index(selected_coords)
                    selected_piece = [index, black_pieces[index]]
                    if alter == selected_piece:
                        alter = [-1, -1]
                        selected_piece = [-1, '']

                    alter = selected_piece

                if selected_coords in allowed_moves:
                    
                    if selected_coords in white_locations:
                        black_total_moves = []
                        white_total_moves = []
                        previous_location = black_locations[index]
                        black_locations[index] = selected_coords
                        if black_pieces[index] == 'king':
                            black_king_location = black_locations[index]
                        allowed_moves = []

                        index2 = white_locations.index(selected_coords)
                        lost = white_locations.pop(index2)
                        lost_piece = white_pieces.pop(index2)                        
                        lost_pieces_white.append(lost_piece)

                        selected_piece = [-1, '']
                        check_total_moves()
                        check_king_check()
                        if black_check==True:
                            white_locations.append(lost)
                            white_pieces.append(lost_piece)
                            lost_pieces_white.pop(white_pieces[index2])
                            black_locations[index] = previous_location
                            if black_pieces[index] == 'king':
                                black_king_location = previous_location
                            selected_piece = [-1, '']
                            check_counter -= 1
                        else:
                            black_locations[index] = selected_coords
                            turn = 'white'
                            check_counter = 8
                    else:                                                                            
                        black_total_moves = []
                        white_total_moves = []
                        previous_location = black_locations[index]
                        black_locations[index] = selected_coords
                        if black_pieces[index] == 'king':
                            black_king_location = black_locations[index]
                        allowed_moves = []
                        selected_piece = [-1, '']
                        check_total_moves()
                        check_king_check()
                        if black_check==True:
                            black_locations[index] = previous_location
                            if black_pieces[index] == 'king':
                                black_king_location = previous_location
                            selected_piece = [-1, '']
                            black_total_moves = []
                            white_total_moves = []
                            check_total_moves()
                            check_king_check()
                            check_counter -= 1
                        else:
                            selected_piece = [-1, '']
                            turn = 'white'
                            check_counter = 8
    py.display.flip()



py.quit()