import time
from turtle import Screen

from game_board import Game_board
from player import Player

clicks_on_screen = []
winer = ''
winning_cells = [
    [(-100, -100), (-100, 0), (-100, 100)],
    [(-100, 100), (0, 100), (100, 100)],
    [(-100, 100), (0, 0), (100, -100)],
    [(0, -100), (0, 0), (0, 100)],
    [(100, -100), (100, 0), (100, 100)],
    [(-100, -100), (0, 0), (100, 100)],
    [(-100, 0), (0, 0), (100, 0)],
    [(-100, -100), (0, -100), (100, -100)]
]

screen = Screen()
screen.bgcolor('#9575DE')
screen.title("The Tic Tac Toe game")
screen.tracer(0)

game_board = Game_board()
player = Player()

screen.listen()
screen.onkey(game_board.board_drawing(), key='enter')

game_is_on = True
while game_is_on:
    time.sleep(1)
    screen.update()
    screen.onclick(player.play)
    game_board.description_writing()
    for cell in winning_cells:
        if cell == player.x_signs:
            winer = 'X'
            game_board.winner_Announcing(winer)
            game_is_on = False
        elif cell == player.o_signs:
            winer = 'O'
            game_board.winner_Announcing(winer)
            game_is_on = False

screen.exitonclick()
