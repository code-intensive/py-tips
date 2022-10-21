from game import Game
from validator import Validator
from display_board import DisplayBoard


def main() -> None:
    game = Game(validator=Validator, display_board=DisplayBoard)
    game.play()
    print(F'{ game.winner } is the undefeated ultimate guess game champ!')

if __name__ == '__main__':
    main()
