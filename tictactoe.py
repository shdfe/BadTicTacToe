from tkinter import *
from tkinter.ttk import *
import random

class TTT:
    def __init__(self,initiate=None):
        self.initiate = initiate
        self.board = [
            ['','',''],
            ['','',''],
            ['','','']
            ]
        print(__name__)
        
        self.p1, self.p2 = 'X', 'O'
        self.p1turn = True
        self.p2turn = False
        self.draw_board()
        self.r = 9
        self.ld = Button(text='',command = lambda: self.changed_based_on_id(self.ld))
        self.ld.place(x=30,y=30)
        self.tc = Button(text='',command = lambda: self.changed_based_on_id(self.tc))
        self.tc.place(x=165,y=30)
        self.rd = Button(text='',command = lambda: self.changed_based_on_id(self.rd))
        self.rd.place(x=300,y=30)
        self.cl = Button(text='',command = lambda: self.changed_based_on_id(self.cl))
        self.cl.place(x=30,y=110)
        self.c = Button(text='',command = lambda: self.changed_based_on_id(self.c))
        self.c.place(x=165,y=110)
        self.cr = Button(text='',command = lambda: self.changed_based_on_id(self.cr))
        self.cr.place(x=300,y=110)
        self.bld = Button(text='',command = lambda: self.changed_based_on_id(self.bld))
        self.bld.place(x=30,y=200)
        self.bc = Button(text='',command = lambda: self.changed_based_on_id(self.bc))
        self.bc.place(x=165,y=200)
        self.brd = Button(text='',command = lambda: self.changed_based_on_id(self.brd))
        self.brd.place(x=300,y=200)
        print(self.computer())
    def get_pre(self):
        available = []
        for li in self.board:
            for e in li:
                if e == '':
                    available.append(e)

                    
        return len(available)
                    
    def changed_based_on_id(self,btn):
        if btn.__str__() == '.!button' and btn['text'] == '':
            btn.config(text = 'X') if self.p1turn else btn.config(text = 'O')
            self.board[0][0] = 'X' if self.p1turn else 'O'
            self.turn()
            self.check()
        elif btn.__str__() == '.!button2' and btn['text'] == '': 
            btn.config(text = 'X') if self.p1turn else btn.config(text = 'O')
            self.board[0][1] = 'X' if self.p1turn else 'O'
            self.turn()
            self.check()
        elif btn.__str__() == '.!button3' and btn['text'] == '': 
            btn.config(text = 'X') if self.p1turn else btn.config(text = 'O')
            self.board[0][2] = 'X' if self.p1turn else 'O'
            self.turn()
            self.check()
        elif btn.__str__() == '.!button4' and btn['text'] == '':
            btn.config(text = 'X') if self.p1turn else btn.config(text = 'O')
            self.board[1][0] = 'X' if self.p1turn else 'O'
            self.turn()
            self.check()
        elif btn.__str__() == '.!button5' and btn['text'] == '':
            btn.config(text = 'X') if self.p1turn else btn.config(text = 'O')
            self.board[1][1] = 'X' if self.p1turn else 'O'
            self.turn()
            self.check()
        elif btn.__str__() == '.!button6' and btn['text'] == '':
            btn.config(text = 'X') if self.p1turn else btn.config(text = 'O')
            self.board[1][2] = 'X' if self.p1turn else 'O'
            self.turn()
            self.check()
        elif btn.__str__() == '.!button7' and btn['text'] == '':
            btn.config(text = 'X') if self.p1turn else btn.config(text = 'O')
            self.board[2][0] = 'X' if self.p1turn else 'O'
            self.turn()
            self.check()
        elif btn.__str__() == '.!button8' and btn['text'] == '':
            btn.config(text = 'X') if self.p1turn else btn.config(text = 'O')
            self.board[2][1] = 'X' if self.p1turn else 'O'
            self.turn()
            self.check()
        elif btn.__str__() == '.!button9' and btn['text'] == '':
            btn.config(text = 'X') if self.p1turn else btn.config(text = 'O')
            self.board[2][2] = 'X' if self.p1turn else 'O'
            self.turn()
            self.check()

        else:
            pass
        
            

    def turn(self):
        if self.p1turn == True and abs(self.get_pre()-self.r) % 2 == 1:
            self.p1turn = False
            self.p2turn = True
            
            
        else:
            self.p2turn = False
            self.p1turn= True
    def computer(self):
        best_moves = [5,7,3,9,1,4,6,2,8]
        odd = []
        even = []
        for move in best_moves:
            if move % 2 == 1:
                odd.append(move)
            else:
                even.append(move)
        
        print(odd, even)
    def equals3(self,a,b,c):
        return a == b and b == c and a != ''
    def forget_buttons(self):
        self.ld.destroy()
        self.tc.destroy()
        self.rd.destroy()
        self.cl.destroy()
        self.c.destroy()
        self.cr.destroy()
        self.bld.destroy()
        self.bc.destroy()
        self.brd.destroy()
    def check(self):
        #horizontal
        for i in range(3):
            if self.equals3(self.board[i][0], self.board[i][1], self.board[i][2]):
                v = StringVar()
                v = v.set(f'{self.board[i][0]} wins!')
                
                self.canvas.delete('all')
                Label(self.canvas, text = f'{self.board[i][0]} wins!', font=('Arial',50)).pack()
                self.forget_buttons()
                
        #vertical
        for i in range(3):
            if self.equals3(self.board[0][i], self.board[1][i], self.board[2][i]):
                v = StringVar()
                v = v.set(f'{self.board[0][i]} wins!')
                self.canvas.delete('all')
                Label(self.canvas, text = f'{self.board[0][i]} wins!', font=('Arial',50)).pack()
                self.forget_buttons()
        #diagonal
        if self.equals3(self.board[0][0],self.board[1][1],self.board[2][2]) or self.equals3(self.board[0][2],self.board[1][1],self.board[2][0]):
            v = StringVar()
            v = v.set(f'{self.board[1][1]} wins!')
            self.canvas.delete('all')
            Label(self.canvas, text = f'{self.board[1][1]} wins!', font=('Arial',50)).pack()
            self.forget_buttons()

        if self.get_pre() == 0:
            v = StringVar()
            v = v.set('Tie') 
            self.canvas.delete('all')
            Label(self.canvas, text = 'Tie!', font=('Arial',50)).pack()
            self.forget_buttons()


    def draw_board(self):
        self.canvas = Canvas(self.initiate)
        for i in range(len(self.board[0])):
            for j in range(2):
                self.canvas.create_line(i*30-200,j*80+80,i*70+2000,j*80+80)
                self.canvas.pack()
                self.canvas.create_line(i*135,j*70+0,i*135,j*70+400)
                self.canvas.pack()
                
        
    



    

    
#GameLoop

ue = Tk()

t = TTT(ue)
