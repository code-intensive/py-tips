from abc import ABCMeta, abstractmethod


class IDisplayBoard(metaclass=ABCMeta):
    @abstractmethod
    def display_scoreboard(self) -> None:
        ...

    @staticmethod
    @abstractmethod
    def line_sep(number_of_lines: int) -> str:
        ...


class DisplayBoard(IDisplayBoard):
    def __init__(self, game) -> None:
        self.game = game

    def display_scoreboard(self) -> None:
        
        score_board = (
            F'{ DisplayBoard.line_sep(20) }'
            F'{ self.game._players[0]}: { self.game._scores[0] },\n'
            F'{ self.game._players[1]}: { self.game._scores[1] }\n'
            F'{ DisplayBoard.line_sep(20) }'
        )
        print(score_board)

    @staticmethod
    def line_sep(number_of_lines: int) -> str:
        return '-' * number_of_lines + '\n'
