#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce
from typing import Generic, Iterable, Tuple, TypeVar


T = TypeVar('T')
class Board(Generic[T]):
	def __init__(self):
		val = self.get_empty_cell_value()
		sizes = self.get_sizes()
		self.cells = [val] * self.calc_idx((sizes[0],) + (0,)*(len(sizes)-1))

	def get_sizes(self) -> Tuple[int]:
		raise NotImplementedError(
			"Define the board geometry via get_sizes function."
		)

	@classmethod
	def get_empty_cell_value(cls) -> T:
		raise NotImplementedError(
			"Define the get_empty_cell_value method for non-abstract board."
		)

	def calc_idx(self, idx: Tuple[int]) -> int:
		sizes = self.get_sizes()
		# TODO cache one or more last indices
		return reduce(lambda acc, szidx: acc*szidx[0] + szidx[1], zip(sizes, idx), 0)

	def __getitem__(self, idx: Iterable[int]) -> T:
		return self.cells[self.calc_idx(tuple(idx))]

	def __setitem__(self, idx: Iterable[int], val: T):
		idx = tuple(idx)
		if self.check_rules(idx, val):
			self.cells[self.calc_idx(idx)] = val

	def check_rules(self, idx: Tuple[int], val: T):
		raise NotImplementedError(
			"Define validation via check_rules function to make the board writable."
		)


class WrongPlayerMoveError(ValueError):
	pass


class WrongCellChosenError(ValueError):
	pass
