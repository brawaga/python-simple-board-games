#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__authors__ = ('brawaga',)

from commons.license import print_license_info
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
	return True


def print_board(board):
	print('Доска:')
	for i in range(board.get_sizes()[0]):
		for j in range(board.get_sizes()[1]):
			print('[%2s]' % (board[(i, j)] or ' ',), end='')
		print()


def main():
	# Цикл обработки событий
	inp = ''
	board = G15Board()
	print_board(board)
	is_quit = lambda: inp.lower() in {'q', 'в'}
	while True:
		inp = ' '
		while not is_quit() and not is_correct_input(inp):
			inp = input(
				"Введите номер ячейки двумя цифрами и направление "
				"обмена {lrud} без разделителей: "
			).lower()
		if is_quit():
			return
		idx1 = (int(inp[0]) - 1, int(inp[1]) - 1)
		idx2 = {
			'u': (idx1[0] - 1, idx1[1]),
			'd': (idx1[0] + 1, idx1[1]),
			'l': (idx1[0], idx1[1] - 1),
			'r': (idx1[0], idx1[1] + 1),
		}[inp[2]]
		try:
			board.swap(idx1, idx2)
		except WrongPlayerMoveError:
			print('Неверный ход.')
		else:
			print_board(board)
			win = board.is_winned()
			if win:
				print('Поздравляю!')
				return


if __name__ == "__main__":
	print_license_info()
	main()
