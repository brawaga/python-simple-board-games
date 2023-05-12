#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from curses import wrapper

from commons.license import print_license_info
from tictactoe import TTTBoard
from games.tictactoe.play_curses import TTTCursesPlay as TTTPlay


def main(scr):
	board = TTTBoard(3)
	gameplay = TTTPlay(scr, board)
	msg = None
	# Цикл обработки событий
	while True:
		msg = msg or gameplay.get_default_input_message()
		gameplay.draw_board()
		if gameplay.draw_state():
			break
		inp = scr.getkey()
		msg = gameplay.handle_input(inp)
	inp = scr.getkey()


if __name__ == "__main__":
	print_license_info()
	wrapper(main)
