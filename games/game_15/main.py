#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__authors__ = ('brawaga',)

from game_15 import G15Board, WrongPlayerMoveError

def is_correct_input(inp):
	if len(inp) != 3:
		return False
	if inp[0] not in '1234':
		return False
	if inp[1] not in '1234':
		return False
	if inp[2].lower() not in 'udlr':
		return False

def main():
	SIZE = 3
	# Цикл обработки событий
	inp = ''
	board = G15Board()
	is_quit = lambda: inp.lower() in {'q', 'в'}
	while True:
		inp = ' '
		while not is_quit() and not is_correct_input(inp):
			inp = input("Введите номер ячейки двумя цифрами и направление обмена {lrud} без разделителей: ").lower()
		if is_quit():
			return
		idx1 = (int(inp[0]) - 1, int(inp[1]) - 1)
		idx2 = {
			'l': (idx1[0] - 1, idx1[1]),
			'r': (idx1[0] + 1, idx1[1]),
			'u': (idx1[0], idx1[1] - 1),
			'd': (idx1[0], idx1[1] + 1),
		}[inp[2]]
		try:
			board.swap(idx1, idx2)
		except WrongPlayerMoveError:
			print('Неверный ход.')
		else:
			print('Доска:')
			for i in range(SIZE):
				for j in range(SIZE):
					print('[%2s]'.format(board[(i, j)] or ' '), end='')
				print()
			win = board.is_winned()
			if win:
				print('Поздравляю!')

if __name__ == "__main__":
	#print_license_info()
	main()