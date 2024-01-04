import pygame as py
import time
import tkinter
from tkinter import messagebox



class Log:
    def __init__(self, piece_name, piece_color, start, destination, lost_piece):
        self.piece_name = piece_name
        self.piece_color = piece_color
        self.start = start
        self.destination = destination
        self.lost_piece = lost_piece



class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
    def clearStack(self):
        self.stack.clear()


log_list = Stack()
redo_list = Stack()


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


white_king_location = ()
black_king_location = ()


color1 = 'red'  # First color
color2 = 'blue'  # Second color
current_color = color1
flash_interval = 500  # Flash interval in milliseconds
last_flash_time = 0



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
    white_castle = py.transform.scale(white_castle, (55, 55))
    white_horse = py.image.load("C:\\Users\\Acer\\Desktop\\Python\\Chess\\images\\white horse.png")
    white_horse = py.transform.scale(white_horse, (55, 55))
    white_elephant = py.image.load("C:\\Users\\Acer\\Desktop\\Python\\Chess\\images\\white elephant.png")
    white_elephant = py.transform.scale(white_elephant, (55, 55))
    white_queen = py.image.load("C:\\Users\\Acer\\Desktop\\Python\\Chess\\images\\white queen.png")
    white_queen = py.transform.scale(white_queen, (55, 55))
    white_king = py.image.load("C:\\Users\\Acer\\Desktop\\Python\\Chess\\images\\white king.png")
    white_king = py.transform.scale(white_king, (55, 55))
    white_soldier = py.image.load("C:\\Users\\Acer\\Desktop\\Python\\Chess\\images\\white soldier.png")
    white_soldier = py.transform.scale(white_soldier, (50, 50))

    global black_castle, black_horse, black_elephant, black_queen, black_king, black_soldier
    black_castle = py.image.load("C:\\Users\\Acer\\Desktop\\Python\\Chess\\images\\black castle.png")
    black_castle = py.transform.scale(black_castle, (55, 55))
    black_horse = py.image.load("C:\\Users\\Acer\\Desktop\\Python\\Chess\\images\\black horse.png")
    black_horse = py.transform.scale(black_horse, (55, 55))
    black_elephant = py.image.load("C:\\Users\\Acer\\Desktop\\Python\\Chess\\images\\black elephant.png")
    black_elephant = py.transform.scale(black_elephant, (55, 55))
    black_queen = py.image.load("C:\\Users\\Acer\\Desktop\\Python\\Chess\\images\\black queen.png")
    black_queen = py.transform.scale(black_queen, (55, 55))
    black_king = py.image.load("C:\\Users\\Acer\\Desktop\\Python\\Chess\\images\\black king.png")
    black_king = py.transform.scale(black_king, (55, 55))
    black_soldier = py.image.load("C:\\Users\\Acer\\Desktop\\Python\\Chess\\images\\black soldier.png")
    black_soldier = py.transform.scale(black_soldier, (50, 50))

    global surrender
    surrender = py.image.load("C:\\Users\\AceR\\Desktop\\python\\Chess\\images\\surrender.png")
    surrender = py.transform.scale(surrender, (80, 80))
    screen.blit(surrender, (990, 70))

    global redo, undo
    redo = py.image.load("C:\\Users\\AceR\\Desktop\\python\\Chess\\images\\redo.png")
    redo = py.transform.scale(redo, (60, 60))
    screen.blit(redo, (1000, 270))

    undo = py.image.load("C:\\Users\\AceR\\Desktop\\python\\Chess\\images\\undo.png")
    undo = py.transform.scale(undo, (70, 70))
    screen.blit(undo, (995, 470))
    



def draw_pieces():
    for i in range(len(white_pieces)):
        if white_pieces[i] == 'soldier':
            screen.blit(white_soldier, (205 + white_locations[i][0]*70, 75 + white_locations[i][1]*70))

        elif white_pieces[i] == 'castle':
            screen.blit(white_castle, (205 + white_locations[i][0]*70, 75 + white_locations[i][1]*70))
        
        elif white_pieces[i] == 'horse':
            screen.blit(white_horse, (205 + white_locations[i][0]*70, 75 + white_locations[i][1]*70))

        elif white_pieces[i] == 'elephant':
            screen.blit(white_elephant, (205 + white_locations[i][0]*70, 75 + white_locations[i][1]*70))
        
        elif white_pieces[i] == 'queen':
            screen.blit(white_queen, (205 + white_locations[i][0]*70, 75 + white_locations[i][1]*70))
        
        elif white_pieces[i] == 'king':
            screen.blit(white_king, (205 + white_locations[i][0]*70, 75 + white_locations[i][1]*70))
        
        if turn == "white":
            if selected_piece[0] != -1:
                x = white_locations[selected_piece[0]][0]
                y = white_locations[selected_piece[0]][1]
                py.draw.rect(screen, 'green', (200+(x*70), 70+(y*70), 70, 70), 3)
        
    
    for i in range(len(black_pieces)):
        if black_pieces[i] == 'soldier':
            screen.blit(black_soldier, (205 + black_locations[i][0]*70, 75 + black_locations[i][1]*70))

        elif black_pieces[i] == 'castle':
            screen.blit(black_castle, (205 + black_locations[i][0]*70, 75 + black_locations[i][1]*70))
        
        elif black_pieces[i] == 'horse':
            screen.blit(black_horse, (205 + black_locations[i][0]*70, 75 + black_locations[i][1]*70))

        elif black_pieces[i] == 'elephant':
            screen.blit(black_elephant, (205 + black_locations[i][0]*70, 75 + black_locations[i][1]*70))
        
        elif black_pieces[i] == 'queen':
            screen.blit(black_queen, (205 + black_locations[i][0]*70, 75 + black_locations[i][1]*70))
        
        elif black_pieces[i] == 'king':
            screen.blit(black_king, (205 + black_locations[i][0]*70, 75 + black_locations[i][1]*70))

        if turn == "black":
            if selected_piece[0] != -1:
                x = black_locations[selected_piece[0]][0]
                y = black_locations[selected_piece[0]][1]
                py.draw.rect(screen, 'blue', (200+(x*70), 70+(y*70), 70, 70), 3)




def check_moves(selected):
    global allowed_moves
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
        
        # en_passant
        if( (location[0]-1, location[1]) in enemies ):
            if black_pieces[black_locations.index((location[0]-1, location[1]))]=="soldier":
                for i in log_list.stack:
                    if( (i.piece_name == "soldier") and (i.destination[1] - i.start[1]) == 2):
                        element1 = log_list.pop()
                        element2 = log_list.pop()
                        if element2.piece_name == "soldier" and element2.destination == location:
                            allowed_moves.append((location[0]-1, location[1]-1))
                        log_list.push(element2)
                        log_list.push(element1)
        if( (location[0]+1, location[1]) in enemies ):
            if black_pieces[black_locations.index((location[0]+1, location[1]))]=="soldier":
                for i in log_list.stack:
                    if( (i.piece_name == "soldier") and (i.destination[1] - i.start[1]) == 2):
                        element1 = log_list.pop()
                        element2 = log_list.pop()
                        if element2.piece_name == "soldier" and element2.destination == location:
                            allowed_moves.append((location[0]+1, location[1]-1))
                        log_list.push(element2)
                        log_list.push(element1)
    
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

        # en_passant
        if( (location[0]-1, location[1]) in enemies):
            if white_pieces[white_locations.index((location[0]-1, location[1]))]=="soldier":
                for i in log_list.stack:
                    if( (i.piece_name == "soldier") and (i.destination[1] - i.start[1]) == 2):
                        element1 = log_list.pop()
                        element2 = log_list.pop()
                        if element2.piece_name == "soldier" and element2.destination == location:
                            allowed_moves.append((location[0]-1, location[1]+1))
                        log_list.push(element2)
                        log_list.push(element1)
        if( (location[0]+1, location[1]) in enemies ):
            if white_pieces[white_locations.index((location[0]+1, location[1]))]=="soldier":
                for i in log_list.stack:
                    if( (i.piece_name == "soldier") and (i.destination[1] - i.start[1]) == 2):
                        element1 = log_list.pop()
                        element2 = log_list.pop()
                        if element2.piece_name == "soldier" and element2.destination == location:
                            allowed_moves.append((location[0]+1, location[1]+1))
                        log_list.push(element2)
                        log_list.push(element1)




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
        while (x1, y) not in white_locations and x1>=0 and (x1, y) not in allowed_moves:
            if (x1, y) in black_locations:
                allowed_moves.append((x1, y))
                break
            allowed_moves.append((x1, y))
            x1 -= 1
        
        x2 = x + 1
        while (x2, y) not in white_locations and x2<=7 and (x2, y) not in allowed_moves:
            if (x2, y) in black_locations:
                allowed_moves.append((x2, y))
                break
            allowed_moves.append((x2, y))
            x2 += 1
        
        y1 = y - 1
        while (x, y1) not in white_locations and y1>=0 and (x, y1) not in allowed_moves:
            if (x, y1) in black_locations:
                allowed_moves.append((x, y1))
                break
            allowed_moves.append((x, y1))
            y1 -= 1
        
        y2 = y + 1
        while (x, y2) not in white_locations and y2<=7 and (x, y2) not in allowed_moves:
            if (x, y2) in black_locations:
                allowed_moves.append((x, y2))
                break
            allowed_moves.append((x, y2))
            y2 += 1
    
    if turn == "black":
        x = black_locations[selected[0]][0]
        y = black_locations[selected[0]][1]

        x1 = x - 1
        while (x1, y) not in black_locations and x1>=0 and (x1, y) not in allowed_moves:
            if (x1, y) in white_locations:
                allowed_moves.append((x1, y))
                break
            allowed_moves.append((x1, y))
            x1 -= 1
        
        x2 = x + 1
        while (x2, y) not in black_locations and x2<=7 and (x2, y) not in allowed_moves:
            if (x2, y) in white_locations:
                allowed_moves.append((x2, y))
                break
            allowed_moves.append((x2, y))
            x2 += 1
        
        y1 = y - 1
        while (x, y1) not in black_locations and y1>=0 and (x, y1) not in allowed_moves:
            if (x, y1) in white_locations:
                allowed_moves.append((x, y1))
                break
            allowed_moves.append((x, y1))
            y1 -= 1
        
        y2 = y + 1
        while (x, y2) not in black_locations and y2<=7 and (x, y2) not in allowed_moves:
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
        colors = [(255, 42, 0), (255, 102, 0), (255, 153, 0), (255, 217, 0), (229, 255, 0), (191, 255, 0), \
            (153, 255, 0), (81, 255, 0), (0, 255, 21), (0, 255, 106), (0, 255, 179), (0, 255, 234), (0, 191, 255), \
            (0, 98, 255), (8, 0, 255), (76, 0, 255), (111, 0, 255), (166, 0, 255), (230, 0, 255), (255, 0, 144), \
            (217, 121, 217), (121, 124, 217), (121, 217, 132), (133, 4, 25), (15, 19, 99), (15, 99, 77), \
            (238, 129, 240)
            ]
        j=0
        for i in range(len(allowed_moves)):
            if j==len(colors)-1:
                j=0
            if allowed_moves[i] in black_locations:
                py.draw.rect(screen, 'red', (205+ 70*allowed_moves[i][0], 75+ 70*allowed_moves[i][1], 60, 60), 2)
            else:
                py.draw.rect(screen, colors[j], (205+ 70*allowed_moves[i][0], 75+ 70*allowed_moves[i][1], 60, 60), 2)
                j+=1
                
        
    if turn == 'black':
        colors = [(255, 42, 0), (255, 102, 0), (255, 153, 0), (255, 217, 0), (229, 255, 0), (191, 255, 0), \
            (153, 255, 0), (81, 255, 0), (0, 255, 21), (0, 255, 106), (0, 255, 179), (0, 255, 234), (0, 191, 255), \
            (0, 98, 255), (8, 0, 255), (76, 0, 255), (111, 0, 255), (166, 0, 255), (230, 0, 255), (255, 0, 144), \
            (217, 121, 217), (121, 124, 217), (121, 217, 132), (133, 4, 25), (15, 19, 99), (15, 99, 77), \
            (238, 129, 240)
            ]
        j=0
        for i in range(len(allowed_moves)):
            if j==len(colors)-1:
                j=0
            if allowed_moves[i] in white_locations:
                py.draw.rect(screen, 'red', (205+ 70*allowed_moves[i][0], 75+ 70*allowed_moves[i][1], 60, 60), 2)
            else:
                py.draw.rect(screen, colors[j], (205+ 70*allowed_moves[i][0], 75+ 70*allowed_moves[i][1], 60, 60), 2)
                j+=1
    




def draw_lost_pieces():
    for i in range(len(lost_pieces_white)):
        if lost_pieces_white[i][0] == 'soldier':
            if i>9:
                screen.blit(white_soldier, (100, 75 + 60*(i-10)))
            else:
                screen.blit(white_soldier, (5, 75 + 60*i))

        elif lost_pieces_white[i][0] == 'castle':
            if i>9:
                screen.blit(white_castle, (100, 75 + 60*(i-10)))
            else:
                screen.blit(white_castle, (5, 75 + 60*i))
        
        elif lost_pieces_white[i][0] == 'horse':
            if i>9:
                screen.blit(white_horse, (100, 75 + 60*(i-10)))
            else:
                screen.blit(white_horse, (5, 75 + 60*i))

        elif lost_pieces_white[i][0] == 'elephant':
            if i>9:
                screen.blit(white_elephant, (100, 75 + 60*(i-10)))
            else:
                screen.blit(white_elephant, (5, 75 + 60*i))
        
        elif lost_pieces_white[i][0] == 'queen':
            if i>9:
                screen.blit(white_queen, (100, 75 + 60*(i-10)))
            else:
                screen.blit(white_queen, (5, 75 + 60*i))
    
    for i in range(len(lost_pieces_black)):
        if lost_pieces_black[i][0] == 'soldier':
            if i>9:
                screen.blit(black_soldier, (860, 75 + 60*(i-10)))
            else:
                screen.blit(black_soldier, (785, 75 + 60*i))

        elif lost_pieces_black[i][0] == 'castle':
            if i>9:
                screen.blit(black_castle, (860, 75 + 60*(i-10)))
            else:
                screen.blit(black_castle, (785, 75 + 60*i))
        
        elif lost_pieces_black[i][0] == 'horse':
            if i>9:
                screen.blit(black_horse, (860, 75 + 60*(i-10)))
            else:
                screen.blit(black_horse, (785, 75 + 60*i))

        elif lost_pieces_black[i][0] == 'elephant':
            if i>9:
                screen.blit(black_elephant, (860, 75 + 60*(i-10)))
            else:
                screen.blit(black_elephant, (785, 75 + 60*i))
        
        elif lost_pieces_black[i][0] == 'queen':
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



def undoaction():
    global turn, timerx, white_king_moves, black_king_moves, left_white_castle_moves, right_white_castle_moves,\
    left_black_castle_moves, right_black_castle_moves
    timerx = 0

    movement = log_list.pop()
    redo_list.push(movement)

    if movement.piece_color == "white":
        #action for check castling function
        if (movement.piece_name=="king" and movement.start==(4,7) and movement.destination==(2,7)):
            white_king_location=(4,7)
            white_locations[white_locations.index((2,7))]=(4,7)
            white_locations[white_locations.index((3,7))]=(0,7)
            turn = movement.piece_color
        elif (movement.piece_name=="king" and movement.start==(4,7) and movement.destination==(6,7)):
            white_king_location=(4,7)
            white_locations[white_locations.index((6,7))]=(4,7)
            white_locations[white_locations.index((5,7))]=(7,7)
            turn = movement.piece_color
        else:
            index = white_locations.index(movement.destination)
            white_locations[index] = movement.start
            if len(movement.lost_piece)!=0:
                black_pieces.append(movement.lost_piece[0])
                black_locations.append(movement.lost_piece[1])
                lost_pieces_black.remove(movement.lost_piece)
            turn = movement.piece_color
        
        if (movement.piece_name=="king" and movement.start==(4,7)):
            white_king_moves-=1
        
        if movement.piece_name=="castle" and movement.start==(0,7):
            left_white_castle_moves -= 1
        elif movement.piece_name=="castle" and movement.start==(7,7):
            right_white_castle_moves -= 1


    else:
        #action for check castling function
        if (movement.piece_name=="king" and movement.start==(4,0) and movement.destination==(2,0)):
            black_king_location=(4,0)
            black_locations[black_locations.index((2,0))]=(4,0)
            black_locations[black_locations.index((3,0))]=(0,0)
            turn = movement.piece_color
        elif (movement.piece_name=="king" and movement.start==(4,0) and movement.destination==(6,0)):
            black_king_location=(4,0)
            black_locations[black_locations.index((6,0))]=(4,0)
            black_locations[black_locations.index((5,0))]=(7,0)
            turn = movement.piece_color
        else:
            index = black_locations.index(movement.destination)
            black_locations[index] = movement.start
            if len(movement.lost_piece)!=0:
                white_pieces.append(movement.lost_piece[0])
                white_locations.append(movement.lost_piece[1])
                lost_pieces_white.remove(movement.lost_piece)
            turn = movement.piece_color
        
        if (movement.piece_name=="king" and movement.start==(4,0)):
            black_king_moves-=1

        if movement.piece_name=="castle" and movement.start==(0,0):
            left_black_castle_moves -= 1
        elif movement.piece_name=="castle" and movement.start==(7,0):
            right_black_castle_moves -= 1

        

def redoaction():
    global turn, timerx, white_king_moves, black_king_moves, left_white_castle_moves, right_white_castle_moves,\
    left_black_castle_moves, right_black_castle_moves
    timerx=0

    movement = redo_list.pop()
    log_list.push(movement)

    if movement.piece_color == "white":
        #action for check castling function
        if (movement.piece_name=="king" and movement.start==(4,7) and movement.destination==(2,7)):
            white_king_location=(2,7)
            white_locations[white_locations.index((4,7))]=(2,7)
            white_locations[white_locations.index((0,7))]=(3,7)
            turn = "black"
        elif (movement.piece_name=="king" and movement.start==(4,7) and movement.destination==(6,7)):
            white_king_location=(6,7)
            white_locations[white_locations.index((4,7))]=(6,7)
            white_locations[white_locations.index((7,7))]=(5,7)
            turn = "black"

        #en_passant
        elif (movement.piece_name=="soldier" and movement.start[0]+1==movement.destination[0] and 
        movement.start[1]-1==movement.destination[1]):  #ex: (3,4) -> (4,3)
            index = white_locations.index(movement.start)
            white_locations[index] = movement.destination
            lost_piece = [-1, -1]
            index2 = black_locations.index((movement.destination[0], movement.destination[1]+1))
            lost_piece[0] = black_pieces.pop(index2)
            lost_piece[1] = black_locations.pop(index2)
            lost_pieces_black.append(lost_piece)
        
        elif (movement.piece_name=="soldier" and movement.start[0]-1==movement.destination[0] and 
        movement.start[1]-1==movement.destination[1]):  #ex : (3,4) -> (2,3)
            index = white_locations.index(movement.start)
            white_locations[index] = movement.destination
            lost_piece = [-1, -1]
            index2 = black_locations.index((movement.destination[0], movement.destination[1]+1))
            lost_piece[0] = black_pieces.pop(index2)
            lost_piece[1] = black_locations.pop(index2)
            lost_pieces_black.append(lost_piece)
        
        else:
            index = white_locations.index(movement.start)
            white_locations[index] = movement.destination
            if len(movement.lost_piece)!=0:
                lost_piece = [-1, -1]
                index2 = black_locations.index(movement.destination)
                lost_piece[0] = black_pieces.pop(index2)
                lost_piece[1] = black_locations.pop(index2)
                lost_pieces_black.append(lost_piece)
            turn = "black"

        if (movement.piece_name=="king"):
            white_king_moves+=1
        
        if movement.piece_name=="castle" and movement.start==(0,7):
            left_white_castle_moves += 1
        elif movement.piece_name=="castle" and movement.start==(7,7):
            right_white_castle_moves += 1
        
        
        
    else:
        #action for check castling function
        if (movement.piece_name=="king" and movement.start==(4,0) and movement.destination==(2,0)):
            black_king_location=(2,0)
            black_locations[black_locations.index((4,0))]=(2,0)
            black_locations[black_locations.index((0,0))]=(3,0)
            turn = "white"
        elif (movement.piece_name=="king" and movement.start==(4,0) and movement.destination==(6,0)):
            black_king_location=(6,0)
            black_locations[black_locations.index((4,0))]=(6,0)
            black_locations[black_locations.index((7,0))]=(5,0)
            turn = "white"
        #en_passant
        elif (movement.piece_name=="soldier" and movement.start[0]+1==movement.destination[0] and 
        movement.start[1]+1==movement.destination[1]):   # ex : (3,4) -> (4,5)
            index = black_locations.index(movement.start)
            black_locations[index] = movement.destination
            lost_piece = [-1, -1]
            index2 = white_locations.index((movement.destination[0], movement.destination[1]-1))
            lost_piece[0] = white_pieces.pop(index2)
            lost_piece[1] = white_locations.pop(index2)
            lost_pieces_white.append(lost_piece)
        
        elif (movement.piece_name=="soldier" and movement.start[0]-1==movement.destination[0] and 
        movement.start[1]+1==movement.destination[1]):   # ex : (3,4) -> (2,5)
            index = black_locations.index(movement.start)
            black_locations[index] = movement.destination
            lost_piece = [-1, -1]
            index2 = white_locations.index((movement.destination[0], movement.destination[1]-1))
            lost_piece[0] = white_pieces.pop(index2)
            lost_piece[1] = white_locations.pop(index2)
            lost_pieces_white.append(lost_piece)

        else:
            index = black_locations.index(movement.start)
            black_locations[index] = movement.destination
            if len(movement.lost_piece)!=0:
                lost_piece = [-1, -1]
                index2 = white_locations.index(movement.destination)
                lost_piece[0] = white_pieces.pop(index2)
                lost_piece[1] = white_locations.pop(index2)
                lost_pieces_white.append(lost_piece)
            turn = "white"

        if (movement.piece_name=="king"):
            black_king_moves+=1   
        
        if movement.piece_name=="castle" and movement.start==(0,0):
            left_black_castle_moves += 1
        elif movement.piece_name=="castle" and movement.start==(7,0):
            right_black_castle_moves += 1



white_king_moves = 0
black_king_moves = 0
left_white_castle_moves = 0
right_white_castle_moves = 0
left_black_castle_moves = 0
right_black_castle_moves = 0


def check_castling():
    global white_king_location, black_king_location
    if (white_king_location==(4,7) and (1,7) not in white_locations and (2,7) not in white_locations and
    (3,7) not in white_locations and white_pieces[white_locations.index((0, 7))]=="castle" and (not white_check)
    and white_king_moves==0 and left_white_castle_moves==0):
        if ((2,7) not in allowed_moves):
            allowed_moves.append((2, 7))
            

    if (white_king_location==(4,7) and (5,7) not in white_locations and (6,7) not in white_locations and
    white_pieces[white_locations.index((7, 7))]=="castle" and (not white_check) and white_king_moves==0 and
    right_white_castle_moves==0):
        if (6,7) not in allowed_moves:
            allowed_moves.append((6, 7))
            
    
    if (black_king_location==(4,0) and (1,0) not in black_locations and (2,0) not in black_locations and
    (3,0) not in black_locations and black_pieces[black_locations.index((0, 0))]=="castle" and (not black_check)
    and black_king_moves==0 and left_black_castle_moves==0):
        if (2,0) not in allowed_moves: 
            allowed_moves.append((2, 0))
            
    
    if (black_king_location==(4,0) and (5,0) not in black_locations and (6,0) not in black_locations and
    black_pieces[black_locations.index((7, 0))]=="castle" and (not black_check) and black_king_moves==0 and
    right_black_castle_moves==0):
        if (6,0) not in allowed_moves:
            allowed_moves.append((6, 0))
            





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



clock = py.time.Clock()
start_time = time.time()
elapsed_time = 0


timerx = 0  # Initial timer value in seconds
MAX_TIMER = 31  # Maximum time allowed for a turn in seconds
f = open("C:\\Users\\AceR\\Desktop\\python\\Chess\\log.txt", "a")


while running and black_win == False  and  white_win == False:
    #text for check
    timer.tick(30)
    screen.fill((115, 73, 31))
    create_board()
    load_images()
    draw_pieces()
    draw_check()
    draw_lost_pieces()
    check_total_moves()
    check_king_check()


    # Update the timer
    timerx += clock.get_time() / 1000   # Convert milliseconds to seconds

    # Check if the timer has exceeded the maximum time for a turn
    if timerx > MAX_TIMER:
        # Switch turn and reset the timer
        if turn == "white":
            black_win = True
        else:
            white_win = True
    

    # Render the time as text
    time_text = font.render(f"Time: {int(MAX_TIMER - timerx)}", True, (255, 255, 255))  # Convert timer to countdown

    # Blit the time onto the screen
    screen.blit(time_text, (985, 10))  # Adjust the position as needed


    if turn == "white":
        py.draw.rect(screen, 'gold', (200, 640, 560, 70))
    elif turn == "black":
        py.draw.rect(screen, 'gold', (200, 0, 560, 60))
    

    #draws and limits allowed_moves
    if selected_piece[0] != -1:
        
        if white_check:
            allowed_moves2 = allowed_moves
            for i in allowed_moves2:
                if i in black_locations:
                    white_total_moves = []
                    black_total_moves = []
                    index = selected_piece[0]
                    previous_location = white_locations[index]
                    white_locations[index] = i
                    index2 = black_locations.index(i)
                    lost_piece_location = black_locations.pop(index2)
                    lost_piece_name = black_pieces.pop(index2)
                    
                    check_total_moves()
                    check_king_check()

                    if white_check:
                        allowed_moves2.remove(i)
                    black_locations.append(lost_piece_location)
                    black_pieces.append(lost_piece_name)
                    white_locations[index] = previous_location
                    
                else:
                    white_total_moves = []
                    black_total_moves = []
                    index = selected_piece[0]
                    previous_location = white_locations[index]
                    white_locations[index] = i

                    check_total_moves()
                    check_king_check()                   
                
                    if white_check:
                        allowed_moves2.remove(i)
                
                    white_locations[index] = previous_location
            
            allowed_moves = allowed_moves2
        
        elif black_check:
            allowed_moves2 = allowed_moves
            for i in allowed_moves2:
                if i in white_locations:
                    white_total_moves = []
                    black_total_moves = []
                    index = selected_piece[0]
                    previous_location = black_locations[index]
                    black_locations[index] = i
                    index2 = white_locations.index(i)
                    lost_piece_location = white_locations.pop(index2)
                    lost_piece_name = white_pieces.pop(index2)
                    
                    check_total_moves()
                    check_king_check()

                    if black_check:
                        allowed_moves2.remove(i)
                    white_locations.append(lost_piece_location)
                    white_pieces.append(lost_piece_name)
                    black_locations[index] = previous_location
                    
                else:
                    white_total_moves = []
                    black_total_moves = []
                    index = selected_piece[0]
                    previous_location = black_locations[index]
                    black_locations[index] = i

                    check_total_moves()
                    check_king_check()                   
                
                    if black_check:
                        allowed_moves2.remove(i)
                
                    black_locations[index] = previous_location
            
            allowed_moves = allowed_moves2
        ##############################################################################
        else:
            if turn == "white":
                allowed_moves2 = allowed_moves
                for i in allowed_moves2:
                    if i in black_locations:
                        white_total_moves = []
                        black_total_moves = []
                        index = selected_piece[0]
                        previous_location = white_locations[index]
                        white_locations[index] = i
                        index2 = black_locations.index(i)
                        lost_piece_location = black_locations.pop(index2)
                        lost_piece_name = black_pieces.pop(index2)
                        
                        check_total_moves()
                        check_king_check()

                        if white_check:
                            allowed_moves2.remove(i)
                        
                        black_locations.append(lost_piece_location)
                        black_pieces.append(lost_piece_name)
                        white_locations[index] = previous_location
                          
                    else:
                        white_total_moves = []
                        black_total_moves = []
                        index = selected_piece[0]
                        previous_location = white_locations[index]
                        white_locations[index] = i

                        check_total_moves()
                        check_king_check()                   
                    
                        if white_check:
                            allowed_moves2.remove(i)
                    
                        white_locations[index] = previous_location
                
                allowed_moves = allowed_moves2
        
            elif turn == "black":
                allowed_moves2 = allowed_moves
                for i in allowed_moves2:
                    if i in white_locations:
                        white_total_moves = []
                        black_total_moves = []
                        index = selected_piece[0]
                        previous_location = black_locations[index]
                        black_locations[index] = i
                        index2 = white_locations.index(i)
                        lost_piece_location = white_locations.pop(index2)
                        lost_piece_name = white_pieces.pop(index2)
                        
                        check_total_moves()
                        check_king_check()

                        if black_check:
                            allowed_moves2.remove(i)
                        white_locations.append(lost_piece_location)
                        white_pieces.append(lost_piece_name)
                        black_locations[index] = previous_location
                        
                    else:
                        white_total_moves = []
                        black_total_moves = []
                        index = selected_piece[0]
                        previous_location = black_locations[index]
                        black_locations[index] = i

                        check_total_moves()
                        check_king_check()                   
                    
                        if black_check:
                            allowed_moves2.remove(i)
                    
                        black_locations[index] = previous_location
                
                allowed_moves = allowed_moves2
        

        draw_allowed_moves()


    white_total_moves = []
    black_total_moves = []
    check_total_moves()
    check_king_check()


    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        
        if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
            select_x = (event.pos[0] - 200) // 70
            select_y = (event.pos[1] - 70) // 70
            selected_coords = (select_x, select_y)

            if selected_coords == (11, 6) or selected_coords == (12, 6):
                try:
                    undoaction()
                except AttributeError:
                    messagebox.showerror("Error", "No Moves made to Undo !")
                    
            if selected_coords == (11, 3) or selected_coords == (12, 3):
                try:
                    redoaction()
                except AttributeError:
                    messagebox.showerror("Error", "No Undos made to Redo !")

            if (turn == "white"):

                if selected_coords == (11,0) or selected_coords == (12,0):
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
                    
                    check_moves(selected_piece)

                    # action for castling function
                    if selected_piece[1]=="king":
                        check_castling()
                    
                    
                    alter = selected_piece

                

                if selected_coords in allowed_moves:
                    redo_list.clearStack()
                    timerx = 0


                    if selected_coords in black_locations:
                        white_total_moves = []
                        black_total_moves = []


                        index2 = black_locations.index(selected_coords)
                        lost_piece_location = black_locations.pop(index2)
                        lost_piece_name = black_pieces.pop(index2)
                        lost_piece = [lost_piece_name, lost_piece_location]
                        lost_pieces_black.append(lost_piece)


                        movement = Log(white_pieces[index], "white", white_locations[index], selected_coords, lost_piece)
                        log_list.push(movement)
                        f.write("\n"+movement.piece_color+"_"+movement.piece_name+"_("+str(movement.start[0])+","+
                        str(movement.start[1])+")_("+str(movement.destination[0])+","+str(movement.destination[1])+
                        ")_"+movement.lost_piece[0]+"_#_!")

                        white_locations[index] = selected_coords
                        if white_pieces[index] == 'king':
                            white_king_location = white_locations[index]
                        allowed_moves = []


                        selected_piece = [-1, '']
                        
                        
                        white_locations[index] = selected_coords
                        turn = 'black'
                    
                    else:
                        #action for check castling function
                        if selected_piece[1]=="castle":
                            left_white_castle_moves += 1
                        if selected_piece[1]=="castle":
                            right_white_castle_moves += 1
                        if selected_piece[1]=="king":
                            white_king_moves += 1
                        

                        castling = False
                        # action for castling function
                        if (white_locations[selected_piece[0]]==(4,7) and selected_piece[1]=="king" and
                        (selected_coords==(2,7) or selected_coords==(6,7))):
                            white_total_moves = []
                            black_total_moves = []
                            castling = True

                            if selected_coords == (2,7):
                                white_king_location=(2,7)
                                white_locations[white_locations.index((4,7))]=(2,7)
                                white_locations[white_locations.index((0,7))]=(3,7)
                                movement = Log("king", "white", (4,7), selected_coords, [])
                                log_list.push(movement)
                                f.write("\n"+movement.piece_color+"_"+movement.piece_name+"_("+str(movement.start[0])+","+
                                str(movement.start[1])+")_("+str(movement.destination[0])+","+str(movement.destination[1])+
                                ")_*_l_!")
                            elif selected_coords == (6,7):
                                white_king_location=(6,7)
                                white_locations[white_locations.index((4,7))]=(6,7)
                                white_locations[white_locations.index((7,7))]=(5,7)
                                movement = Log("king", "white", (4,7), selected_coords, [])
                                log_list.push(movement)
                                f.write("\n"+movement.piece_color+"_"+movement.piece_name+"_("+str(movement.start[0])+","+
                                str(movement.start[1])+")_("+str(movement.destination[0])+","+str(movement.destination[1])+
                                ")_*_r_!")
                            

                            allowed_moves = []
                            selected_piece = [-1, '']
                            turn = 'black'
                        

                        passant = False
                        #en_passant
                        location = white_locations[selected_piece[0]]
                        if (selected_piece[1]=="soldier" and selected_coords==(location[0]-1, location[1]-1) and
                        selected_coords not in black_locations):
                            passant = True

                            index2 = black_locations.index((location[0]-1, location[1]))
                            lost_piece_location = black_locations.pop(index2)
                            lost_piece_name = black_pieces.pop(index2)
                            lost_piece = [lost_piece_name, lost_piece_location]
                            lost_pieces_black.append(lost_piece)

                            movement = Log(white_pieces[index], "white", white_locations[index], selected_coords, lost_piece)
                            log_list.push(movement)
                            f.write("\n"+movement.piece_color+"_"+movement.piece_name+"_("+str(movement.start[0])+","+
                            str(movement.start[1])+")_("+str(movement.destination[0])+","+str(movement.destination[1])+
                            ")_soldier_#_("+str(movement.lost_piece[1][0])+","+str(movement.lost_piece[1][1])+")")


                            white_total_moves = []
                            black_total_moves = []
                            allowed_moves = []
                            selected_piece = [-1, '']
                            white_locations[index] = selected_coords
                            turn = 'black'
                        
                        elif (selected_piece[1]=="soldier" and selected_coords==(location[0]+1, location[1]-1) and
                        selected_coords not in black_locations):
                            passant = True

                            index2 = black_locations.index((location[0]+1, location[1]))
                            lost_piece_location = black_locations.pop(index2)
                            lost_piece_name = black_pieces.pop(index2)
                            lost_piece = [lost_piece_name, lost_piece_location]
                            lost_pieces_black.append(lost_piece)

                            movement = Log(white_pieces[index], "white", white_locations[index], selected_coords, lost_piece)
                            log_list.push(movement)
                            f.write("\n"+movement.piece_color+"_"+movement.piece_name+"_("+str(movement.start[0])+","+
                            str(movement.start[1])+")_("+str(movement.destination[0])+","+str(movement.destination[1])+
                            ")_soldier_#_("+str(movement.lost_piece[1][0])+","+str(movement.lost_piece[1][1])+")")


                            white_total_moves = []
                            black_total_moves = []
                            allowed_moves = []
                            selected_piece = [-1, '']
                            white_locations[index] = selected_coords
                            turn = 'black'


                        if (not castling and not passant):
                            white_total_moves = []
                            black_total_moves = []

                            movement = Log(white_pieces[index], "white", white_locations[index], selected_coords, [])
                            log_list.push(movement)
                            f.write("\n"+movement.piece_color+"_"+movement.piece_name+"_("+str(movement.start[0])+","+
                                str(movement.start[1])+")_("+str(movement.destination[0])+","+str(movement.destination[1])+
                                ")_*_#_!")


                            white_locations[index] = selected_coords
                            if white_pieces[index] == 'king':
                                white_king_location = white_locations[index]
                            allowed_moves = []
                            
                            
                            selected_piece = [-1, '']
                            turn = 'black'
                        

            
            if (turn == "black"):
                if selected_coords == (11,0) or selected_coords == (12,0):
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

                    check_moves(selected_piece)

                    if selected_piece[1] == "king":
                        check_castling()

                    alter = selected_piece

                if selected_coords in allowed_moves:
                    redo_list.clearStack()
                    timerx = 0


                    if selected_coords in white_locations:
                        black_total_moves = []
                        white_total_moves = []

                        index2 = white_locations.index(selected_coords)
                        lost_piece_location = white_locations.pop(index2)
                        lost_piece_name = white_pieces.pop(index2)
                        lost_piece = [lost_piece_name, lost_piece_location]                        
                        lost_pieces_white.append(lost_piece)

                        movement = Log(black_pieces[index], "black", black_locations[index], selected_coords, lost_piece)
                        log_list.push(movement)
                        f.write("\n"+movement.piece_color+"_"+movement.piece_name+"_("+str(movement.start[0])+","+
                        str(movement.start[1])+")_("+str(movement.destination[0])+","+str(movement.destination[1])+
                        ")_"+movement.lost_piece[0]+"_#_!")


                        black_locations[index] = selected_coords
                        if black_pieces[index] == 'king':
                            black_king_location = black_locations[index]
                        allowed_moves = []


                        selected_piece = [-1, '']

                        black_locations[index] = selected_coords
                        turn = 'white'


                    else:
                        #action for check castling function
                        if selected_piece[1]=="castle" and black_locations[selected_piece[0]]==(0,0):
                            left_black_castle_moves += 1
                        if selected_piece[1]=="castle" and black_locations[selected_piece[0]]==(7,0):
                            right_black_castle_moves += 1
                        if selected_piece[1]=="king" and black_locations[selected_piece[0]]==(4,0):
                            black_king_moves += 1 


                        castling = False
                        # action for castling function
                        if (black_locations[selected_piece[0]]==(4,0) and selected_piece[1]=="king" 
                        and (selected_coords==(2,0) or selected_coords==(6,0))):
                            castling = True
                            if selected_coords == (2,0):
                                black_king_location=(2,0)
                                black_locations[black_locations.index((4,0))]=(2,0)
                                black_locations[black_locations.index((0,0))]=(3,0)
                                movement = Log("king", "black", (4,0), selected_coords, [])
                                log_list.push(movement)
                                f.write("\n"+movement.piece_color+"_"+movement.piece_name+"_("+str(movement.start[0])+","+
                                str(movement.start[1])+")_("+str(movement.destination[0])+","+str(movement.destination[1])+
                                ")_*_l_!")
                            elif selected_coords == (6,0):
                                black_king_location=(6,0)
                                black_locations[black_locations.index((4,0))]=(6,0)
                                black_locations[black_locations.index((7,0))]=(5,0)
                                movement = Log("king", "black", (4,0), selected_coords, [])
                                log_list.push(movement)
                                f.write("\n"+movement.piece_color+"_"+movement.piece_name+"_("+str(movement.start[0])+","+
                                str(movement.start[1])+")_("+str(movement.destination[0])+","+str(movement.destination[1])+
                                ")_*_r_!")


                            allowed_moves = []
                            selected_piece = [-1, '']
                            turn = 'white'


                        passant = False
                        #en_passant
                        location = black_locations[selected_piece[0]]
                        if (selected_piece[1]=="soldier" and selected_coords==(location[0]-1, location[1]+1) and
                        selected_coords not in white_locations):
                            passant = True

                            index2 = white_locations.index((location[0]-1, location[1]))
                            lost_piece_location = white_locations.pop(index2)
                            lost_piece_name = white_pieces.pop(index2)
                            lost_piece = [lost_piece_name, lost_piece_location]
                            lost_pieces_white.append(lost_piece)

                            movement = Log(black_pieces[index], "black", black_locations[index], selected_coords, lost_piece)
                            log_list.push(movement)
                            f.write("\n"+movement.piece_color+"_"+movement.piece_name+"_("+str(movement.start[0])+","+
                            str(movement.start[1])+")_("+str(movement.destination[0])+","+str(movement.destination[1])+
                            ")_soldier_#_("+str(movement.lost_piece[1][0])+","+str(movement.lost_piece[1][1])+")")


                            white_total_moves = []
                            black_total_moves = []
                            allowed_moves = []
                            selected_piece = [-1, '']
                            black_locations[index] = selected_coords
                            turn = 'white'
                        
                        elif (selected_piece[1]=="soldier" and selected_coords==(location[0]+1, location[1]+1) and
                        selected_coords not in white_locations):
                            passant = True

                            index2 = white_locations.index((location[0]+1, location[1]))
                            lost_piece_location = white_locations.pop(index2)
                            lost_piece_name = white_pieces.pop(index2)
                            lost_piece = [lost_piece_name, lost_piece_location]
                            lost_pieces_white.append(lost_piece)

                            movement = Log(black_pieces[index], "black", black_locations[index], selected_coords, lost_piece)
                            log_list.push(movement)
                            f.write("\n"+movement.piece_color+"_"+movement.piece_name+"_("+str(movement.start[0])+","+
                            str(movement.start[1])+")_("+str(movement.destination[0])+","+str(movement.destination[1])+
                            ")_soldier_#_("+str(movement.lost_piece[1][0])+","+str(movement.lost_piece[1][1])+")")


                            white_total_moves = []
                            black_total_moves = []
                            allowed_moves = []
                            selected_piece = [-1, '']
                            black_locations[index] = selected_coords
                            turn = 'white'


                        if (not castling and not passant):
                            black_total_moves = []
                            white_total_moves = []

                            movement = Log(black_pieces[index], "black", black_locations[index], selected_coords, [])
                            log_list.push(movement)
                            f.write("\n"+movement.piece_color+"_"+movement.piece_name+"_("+str(movement.start[0])+","+
                                str(movement.start[1])+")_("+str(movement.destination[0])+","+str(movement.destination[1])+
                                ")_*_#_!")

                            black_locations[index] = selected_coords
                            if black_pieces[index] == 'king':
                                black_king_location = black_locations[index]
                            allowed_moves = []
                            selected_piece = [-1, '']
                            
                            
                            
                            selected_piece = [-1, '']
                            turn = 'white'
                        
                
    clock.tick(30)
    py.display.flip()

f.close()



if (white_win==True or black_win==True):
    running = True
    while running:
        timer.tick(60)
        screen.fill((115, 73, 31))
    

        if (white_win == True) :
            font_size = 100
            new_font = py.font.Font(None, font_size)
            text_surface2 = new_font.render("White won the game", True, "white")
            textrect2 = text_surface2.get_rect()
            textrect2.center = (480, 200)
            screen.blit(text_surface2, textrect2)
            s = py.image.load("C:\\Users\\AceR\\Desktop\\python\\Chess\\images\\success.png")
            win = py.transform.scale(s, (200, 200))
            screen.blit(win, (700, 250))
        
        if (black_win == True) :
            font_size = 100
            new_font = py.font.Font(None, font_size)
            text_surface2 = new_font.render("Black won the game", True, "black")
            textrect2 = text_surface2.get_rect()
            textrect2.center = (480, 200)
            screen.blit(text_surface2, textrect2)
            s = py.image.load("C:\\Users\\AceR\\Desktop\\python\\Chess\\images\\success.png")
            win = py.transform.scale(s, (200, 200))
            screen.blit(win, (700, 250))
            

        for event in py.event.get():
                if event.type == py.QUIT:
                    running = False

        py.display.flip()

py.quit()