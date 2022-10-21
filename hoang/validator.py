from abc import ABCMeta, abstractmethod


class IValidator(metaclass=ABCMeta):
    @abstractmethod
    def validate_player(self) -> None:
        ...


class Validator(IValidator):
    def __init__(self, game) -> None:
        self.game = game

    def validate_player(self, player: str) -> str:
        if player in self.game._players:
            print(F'A player named { player } exists, kindly use another name')
            self.game.display_board.display_users()
            return

        if player.isalnum():
            return player
        
        print('Invalid player name selected, kindly enter an alpha numeric name')
