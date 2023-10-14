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
	def get_empty_cell_value(cls) -> str:
		return ' '

	def switch_to_next_player(self):
		self.current_player = 'O' if self.current_player == 'X' else 'X'

	def check_rules(self, idx: Tuple[int, ...], val: str):
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
					return v, (0, j), (1, 0)
			v = self[(j, 0)]
			if v != e:
				for i in range(1, size):
					if self[(j, i)] != v:
						break
				else:
					return v, (j, 0), (0, 1)

		# Has room to put a figure — game is not over
		if e in self.cells:
			return None

		# No room and no win conditions met — so draw
		return e, (0, 0), (0, 0)
