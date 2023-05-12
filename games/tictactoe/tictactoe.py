#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Tuple

from commons.board import Board, WrongCellChosenError, WrongPlayerMoveError


class TTTBoard(Board):
	def __init__(self, s):
		self.size = s
		super().__init__()
		self.current_player = 'X'

	def get_sizes(self) -> Tuple[int]:
		return (self.size, self.size)

	@classmethod
	def get_empty_cell_value(cls):
		return ' '

	def switch_to_next_player(self):
		self.current_player = 'O' if self.current_player == 'X' else 'X'

	def check_rules(self, idx: Tuple[int, ...], val):
		if val != self.current_player:
			raise WrongPlayerMoveError('Wrong player move.')
		if self[(idx)] != self.get_empty_cell_value():
			raise WrongCellChosenError('Cell is already occupied.')
		return True

	def __setitem__(self, key, value):
		super().__setitem__(key, value)
		self.switch_to_next_player()

	def get_winner(self) -> None | Tuple[str, Tuple[int, ...], Tuple[int, ...]]:
		size = self.size
		e = self.get_empty_cell_value()

		# Main diagonal
		v = self[(0, 0)]
		if v != e:
			for i in range(1, size):
				if self[(i, i)] != v:
					break
			else:
				return v, (0, 0), (1, 1)

		# Secondary diagonal
		v = self[(0, size-1)]
		if v != e:
			for i in range(1, size):
				if self[(i, size-1-i)] != v:
					break
			else:
				return v, (0, size-1), (1, -1)

		# Horizontals/verticals
		for j in range(size):
			v = self[(0, j)]
			if v != e:
				for i in range(1, size):
					if self[(i, j)] != v:
						break
				else:
					return v, (0, j), (0, 1)
			v = self[(j, 0)]
			if v != e:
				for i in range(1, size):
					if self[(j, i)] != v:
						break
				else:
					return v, (j, 0), (1, 0)

		# Has room to put a figure — game is not over
		if e in self.cells:
			return None

		# No room and no win conditions met — so draw
		return e, (0, 0), (0, 0)


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
