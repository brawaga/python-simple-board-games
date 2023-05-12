#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__authors__ = ('brawaga',)

from typing import Tuple

from commons.board import WrongCellChosenError
from games.tictactoe.tictactoe import TTTBoard


class TTTPlay:
	def __init__(self, board: TTTBoard):
		self.board = board
		self.quit = False

	def draw_board(self):
		print('Доска:')
		s = self.board.get_sizes()
		for i in range(s[0]):
			for j in range(s[1]):
				print(self.board[(i, j)], end='')
			print()

	def draw_state(self) -> None | Tuple[str, Tuple[int, ...], Tuple[int, ...]]:
		if self.quit:
			return self.board.get_empty_cell_value(), (0, 0), (0, 0)
		win_info = self.board.get_winner()
		e = self.board.get_empty_cell_value()
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
					print('Строка', win_info[1][1] + 1)
				else:
					print('Столбец', win_info[1][0] + 1)
			return win_info
		else:
			print('Ходит:', self.board.current_player)
			return None

	def get_default_input_message(self) -> str:
		return "Введите номер ячейки (1-9) или q/в для выхода: "

	def handle_input(self, inp) -> None | str:
		if inp.lower() in {'q', 'в'}:
			self.quit = True
			return "Выход из игры."
		if inp not in '123456789':
			return self.get_default_input_message()
		inp = int(inp) - 1
		s = self.board.get_sizes()
		try:
			self.board[divmod(inp, s[0])] = self.board.current_player
		except WrongCellChosenError:
			return 'Ячейка уже занята, выберите другую.'
		return None
