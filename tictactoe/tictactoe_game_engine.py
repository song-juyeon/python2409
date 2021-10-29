class TictactoeGameEngine:
    def __init__(self):
        self.board = list('.' * 9)      #['.', '.', '.', '.', '.', '.', '.', '.', '.']
        self.turn = 'X'

    def show_board(self):
        print(self.board)

    def set(self, row, cel):
        pass
        #일반인의 입장에서 가로세로 입력
        # board에 값을 변경 시킴

    def set_winner(self):
        pass

    def change_turn(self):
        pass

if __name__ == '__main__':
    game_engine = TictactoeGameEngine()
    game_engine.show_board()    #...\n...\n...
    game_engine.set(2,2)
    game_engine.show_board()    #['.', '.', '.', '.', 'X', '.', '.', '.', '.']
    game_engine.set(2, 1)
    game_engine.set(2, 3)
    game_engine.show_board()    #['.', '.', '.', 'X', 'X', 'X', '.', '.', '.']
    game_engine.board = ['.', '.', '.', 'X', 'X', 'X', '.', '.', '.']
    game_engine.set_winner()    #'-' -> 'X'
    game_engine.change_turn()
    print(game_engine.turn)     #'O'
    game_engine.change_turn()
    print(game_engine.turn)     #'X'