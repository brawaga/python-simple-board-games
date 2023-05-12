#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__authors__ = ('brawaga',)

from curses import A_BOLD, A_DIM
from typing import Tuple

from commons.board import WrongCellChosenError
from games.tictactoe.play_console import TTTConsolePlay
from games.tictactoe.tictactoe import TTTBoard


class TTTCursesPlay(TTTConsolePlay):
	def __init__(self, scr, board: TTTBoard):
		super().__init__(board)
		self.scr = scr
		self.winner = None

	def draw_board(self):
		for i in range(0, 5):
			self.scr.addstr(
				i, 0,
				'---+---+---' if 1 == i % 2 else
				'   |   |   ',
				A_DIM
			)
		s = self.board.get_sizes()
		winner = set()
		if self.winner:
			for i in range(3):
				winner.add((
					self.winner[0][0]+self.winner[1][0]*i,
					self.winner[0][1]+self.winner[1][1]*i
				))
		for i in range(s[0]):
			for j in range(s[1]):
				args = (self.board[(i, j)], A_BOLD if (i, j) in winner or not winner else A_DIM)
				if args[0] == self.board.get_empty_cell_value():
					args = (str(i*3+j+1), A_DIM)
				self.scr.addstr(i*2, j*4+1, *args)

	def show_message(self, msg, msg2=''):
		self.scr.addstr(6, 0, '%-80s' % msg)
		self.scr.addstr(7, 0, '%-80s' % msg2)

	def draw_state(self) -> None | Tuple[str, Tuple[int, ...], Tuple[int, ...]]:
		if self.quit:
			self.show_message('Выход.')
			return self.board.get_empty_cell_value(), (0, 0), (0, 0)
		win_info = self.board.get_winner()
		e = self.board.get_empty_cell_value()
		if win_info:
			self.winner = win_info[1:]
			if win_info[0] == e:
				self.show_message('Ничья.')
			else:
				self.show_message('Выиграли '+win_info[0])
				self.draw_board()
			return win_info
		else:
			self.show_message('Ходит: '+self.board.current_player, self.get_default_input_message())
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
