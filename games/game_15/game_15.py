#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import choice
from typing import Iterable, Tuple

from commons.board import Board, WrongPlayerMoveError


class G15Board(Board):
	FIXED_BOARD_SIZE = (4, 4)
	ORDERED_CELLS_STATE = list(range(1, 16))

	def __init__(self):
		super().__init__()
		self.cells = self.ORDERED_CELLS_STATE[:]
		self.shuffle()

	@classmethod
	def get_empty_cell_value(cls) -> int | None:
		return None

	def shuffle(self):
		swap_count = 100
		empty_idx = (3, 3)
		while swap_count > 0 or self.is_winned():
			swap_count -= 1
			next_available = [
				(empty_idx[0], empty_idx[1] + 1),
				(empty_idx[0], empty_idx[1] - 1),
				(empty_idx[0] + 1, empty_idx[1]),
				(empty_idx[0] - 1, empty_idx[1]),
			]
			next_available = list([
				n for n in next_available if n[0] in range(4) and n[1] in range(4)
			])
			next_idx = choice(next_available)
			self.swap(empty_idx, next_idx)
			empty_idx = next_idx

	def get_sizes(self) -> Tuple[int]:
		return self.FIXED_BOARD_SIZE

	def swap(self, idx1: Tuple[int], idx2: Tuple[int]):
		if self[idx1] is None and self[idx2] is None:
			return
		if self[idx1] is not None and self[idx2] is not None:
			raise WrongPlayerMoveError("Ход не разрешён")
		dif = [abs(i2-i1) for i1, i2 in zip(idx1, idx2)]
		if (dif[0] == 0 and dif[1] == 1) or (dif[1] == 0 and dif[0] == 1):
			t = self[idx1]
			super().__setitem__(idx1, self[idx2])
			super().__setitem__(idx2, t)
		else:
			raise WrongPlayerMoveError("Ход не разрешён")

	def check_rules(self, idx: Iterable[int], val: int| None):
		return True

	def __setitem__(self, idx: Iterable[int], val: int | None):
		raise RuntimeError("Не меняйте поле вручную, используйте swap")

	def is_winned(self):
		return self.cells == self.ORDERED_CELLS_STATE
G15Board.ORDERED_CELLS_STATE += [G15Board.get_empty_cell_value()]