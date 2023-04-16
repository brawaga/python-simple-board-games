#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from commons.license import print_license_info
from tictactoe import TTTBoard, WrongCellChosenError

def main():
	SIZE = 3
	# Цикл обработки событий
	inp = ''
	board = TTTBoard(SIZE)
	win_info = board.get_winner()
	is_quit = lambda: inp.lower() in {'q', 'в'}
	while True:
		print('Ходит:', board.current_player)
		inp = ' '
		while not is_quit() and inp not in '123456789':
			inp = input("Введите номер ячейки или q/в для выхода: ")
		if is_quit():
			return
		inp = int(inp) - 1
		try:
			board[divmod(inp, SIZE)] = board.current_player
		except WrongCellChosenError:
			print('Ячейка уже занята, выберите другую.')
		else:
			print('Доска:')
			for i in range(SIZE):
				for j in range(SIZE):
					print(board[(i, j)], end='')
				print()
			win_info = board.get_winner()
			e = board.get_empty_cell_value()
			if win_info:
				if win_info[0] == e:
					print('Ничья.')
				else:
					print('Выиграли', win_info[0])
					if win_info[2][0] and win_info[2][1]:
						if win_info[2][0] == win_info[2][1]:
							print('Главная диагональ.')
						else:
							print('Побочная диагональ')
					elif win_info[2][0]:
						print('Строка', win_info[1][1]+1)
					else:
						print('Столбец', win_info[1][0]+1)
				return win_info[0]

if __name__ == "__main__":
	print_license_info()
	main()