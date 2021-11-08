import tkinter
from tkinter import messagebox

from tictactoe_game_engine import TictactoeGameEngine

class TictactoeGUI:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()
        self.init_GUI()

    def init_GUI(self):
        self.CANVAS_SIZE = 300
        self.root = tkinter.Tk()    # 창
        self.root.title('틱택토')    # 제목
        self.root.geometry(f'{self.CANVAS_SIZE}x{self.CANVAS_SIZE}')    # 창 크기
        self.root.resizable(width=False, height=False)                  # 창 크기 변경 or 고정

        self.canvas = tkinter.Canvas(self.root, bg='white', width=self.CANVAS_SIZE, height=self.CANVAS_SIZE)    # 캔버스 설정
        self.canvas.pack()      # 캔버스 띄우기

        self.images = {}    #{ 'X' : PhotoImage객체 , 'O' : PhotoImage객체}
        self.images['X'] = tkinter.PhotoImage(file='X.gif')     # 이미지 가져오기
        self.images['O'] = tkinter.PhotoImage(file='O.gif')     # 이미지 가져오기

        self.canvas.bind('<Button-1>', self.click_handler)      # 시험* 괄호X



        self.root.mainloop()       # 창띄우기(마지막)

    def click_handler(self, event):
        # print(f'{event.x}, {event.y}')
        row, col = self.coordinate_to_position(event.x, event.y)
        # set row, col
        self.game_engine.set(row, col)
        # show board
        self.game_engine.show_board()
        # set winner
        winner = self.game_engine.set_winner()
        # 승자가 있거나, 무승부이면, 게임오버, 결과 표시
        if winner == 'O' or winner == 'X':
            messagebox.showinfo('Game Over', f'{winner}가 승리하였습니다🏆')
            self.root.quit()
        elif winner == 'd':
            messagebox.showinfo('Game Over', '무승부입니다')
            self.root.quit()

        # change_turn
        self.game_engine.change_turn()

    def draw_board(self):
        pass

    def coordinate_to_position(self, x, y):
        # if 0 <= x < 100:
        #     x = 1
        # elif 101 <= x < 200:
        #     x = 2
        # elif 201 <= x < 300:
        #     x = 3
        #
        # if 0 <= y < 100:
        #     y = 1
        # elif 101 <= y < 200:
        #     y = 2
        # elif 201 <= y < 300:
        #     y = 3

        # row
        row = y//(self.CANVAS_SIZE // self.game_engine.SIZE) + 1
        # col
        col = x//(self.CANVAS_SIZE // self.game_engine.SIZE) + 1

        return row, col



if __name__ == '__main__':
    ttt_GUI = TictactoeGUI()