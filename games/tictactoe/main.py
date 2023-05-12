#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from commons.license import print_license_info
from tictactoe import TTTBoard
from games.tictactoe.play import TTTPlay


def main():
	board = TTTBoard(3)
	gameplay = TTTPlay(board)
	# Цикл обработки событий
	msg = None
	while True:
		msg = msg or gameplay.get_default_input_message()
		gameplay.draw_board()
		if gameplay.draw_state():
			break
		inp = input(msg)
		msg = gameplay.handle_input(inp)


if __name__ == "__main__":
	print_license_info()
	main()
