from typing import Union
from random import randint

from validator import IValidator
from display_board import IDisplayBoard


class Game:
    WINNING_SCORE = 3

    def __init__(self, validator: IValidator, display_board: IDisplayBoard):
        self._scores = [0, 0]
        self._winner = None
        self.we_have_a_winner = False
        self._players = ['Rael', 'My Linh']
        self.validator = validator(self)
        self.display_board = display_board(self)
        self.__current_player = self._players[randint(0, len(self._players) - 1)]

    def add_player(self) -> None:
        player = input('Enter player name you wish to register: ')

        player = self.validator.validate_player(player)

        if not player:
            return

        self._players.append(player)
        self._scores.append(0)
        print(F'{ player } successfully registered to the ongoing game')

    def _check_guess(self, *, answer: int, guess: int) -> None:
        if answer == guess:
            current_score = self._scores[self._players.index(
                self.__current_player)]
            self._scores[self._players.index(
                self.__current_player)] = current_score + 1
            print('Yay! You got it right...')
        else:
            print(
                F'Sorry, { self.__current_player } you got it wrong this time...')
            print(F'The correct answer was { answer }')

    def _decide_winner(self) -> None:
        if self._scores[self._players.index(self.__current_player)] == self.WINNING_SCORE:
            print('The winner of the ultimate guess challenge is....')
            print(F'{ self.__current_player.upper() }!!!!!')
            self._winner = self.__current_player
            self.we_have_a_winner = True


    def handover_to_next_user(self) -> None:
        if self.__current_player == self._players[-1]:
            self.__current_player = self._players[0]
            return

        next_player_index = self._players.index(self.__current_player) + 1
        self.__current_player = self._players[next_player_index]

    def play(self) -> None:
        while not self.we_have_a_winner:
            answer = randint(1, 3)
            user_response = input(F'{ self.__current_player } enter your guess\n>>> ')

            if user_response == '+':
                self.add_player()
                continue
            elif user_response == '!':
                self.display_board.display_scoreboard()
                continue

            try:
                guess = int(user_response)
            except ValueError:
                print('Kindly input a valid integer next time')
                print(F'{ self.__current_player }, your turn is forfeited...')
            else:
                self._check_guess(answer=answer, guess=guess)
                self._decide_winner()
                self.display_board.display_scoreboard()
                self.handover_to_next_user()

    @property
    def winner(self) -> Union[str, None]:
        if self._winner is None:
            print('The winner has not been decided yet')
        return self._winner
