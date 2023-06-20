game_start=True
while game_start:
    def input_choice():
        global c
        c='wrong'
        global c2
        global P1_pos
        global P2_pos
        while c not in ['X','O']:
            c=input("Please choose X or O")
            if c not in ['X','O']:
                print("Incorrect Input!")
            else:
                print("Player 1 is",c)
                if c=='X':
                    c2='O'
                    print("Player 2 is",c2)
                else:
                    c2='X'
                    print("Player 2 is",c2)          
        

    input_choice()       

    def board_rep():
        global game
        game=False
        global board
        board=list(range(9))
        row_1=[board[i:i+3]for i in range(0,9,3)]

        def print_board():
            for row in row_1:
                print("\n",row)
        print_board()
        def check_win():
            global game
            if board[0]==board[1]==board[2]==c or board[3]==board[4]==board[5]==c or board[6]==board[7]==board[8]==c or board[0]==board[3]==board[6]==c or board[1]==board[4]==board[7]==c or board[2]==board[5]==board[8]==c or board[0]==board[4]==board[8]==c or board[2]==board[4]==board[6]==c:
                print('Congratulations Player 1 you have won the game')
                game=True
            elif board[0]==board[1]==board[2]==c2 or  board[3]==board[4]==board[5]==c2 or board[6]==board[7]==board[8]==c2 or board[0]==board[3]==board[6]==c2 or board[1]==board[4]==board[7]==c2 or board[2]==board[5]==board[8]==c2 or board[0]==board[4]==board[8]==c2 or board[2]==board[4]==board[6]==c2:
                print('Congratulations Player 2 you have won the game')
                game=True
            elif all(marker=='X'or marker=='O' for marker in board):   
                print("Game is tied")
                game=True
            else:
                game=False

        while game==False:
            global game_start
            P1_pos=int(input("Player 1 choose a position from 0 to 8"))
            board[P1_pos]=c
            for i in range(0,3):
                for j in range(0,3):
                    row_1[i][j]=board[i*3+j]

            print_board()
            check_win()

            if game==True:
                break

            P2_pos=int(input("Player 2 please choose a position from 0 to 8"))
            board[P2_pos]=c2
            for i in range(0,3):
                for j in range(0,3):
                    row_1[i][j]=board[i*3+j]

            print_board()
            check_win()
            

            if game==True:
                break
        finish=input('Press Y to play again and N to quit game')
        
        if finish=="Y":
            game_start=True
        elif finish=="N":
            print("Thank you for playing")
            game_start=False
        while finish not in ['Y','N']:
            finish=input("please press Y to play again or N to quit game")    
   

    board_rep()




