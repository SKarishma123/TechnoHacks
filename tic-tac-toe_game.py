#Tic-Tac-Toe Game-Task1
from  tkinter  import *
root=Tk()
root.geometry("600x600")
root.title("Tic Tac Toe")

frame1=Frame(root)
frame1.pack()
titlelabel=Label(frame1,text="Tic Tac Toe game",font=("Arial",30))
titlelabel.grid(row=0,column=0)

frame2 =Frame(root)
frame2.pack()
board={1:" ",2:" ",3:" ",
       4:" ",5:" ",6:" ",
       7:" ",8:" ",9:" "}
turn ="x"
def checkforwin(player):

  #Horizontal =row
    if board[1]==board[2]and board[2]==board[3] and board[3]==player:
        return True
    elif board[4]==board[5]and board[5]==board[6] and board[6]==player:
        return True
    elif board[7]==board[8]and board[8]==board[9] and board[9]==player:
        return True
    #vertical=column
    elif board[1]==board[4]and board[4]==board[7] and board[7]==player:
        return True
    elif board[2]==board[5]and board[5]==board[8] and board[8]==player:
        return True
    elif board[3]==board[6]and board[6]==board[9] and board[9]==player:
        return True
    #diagonal
    elif board[1]==board[5]and board[5]==board[9] and board[9]==player:
        return True
    elif board[3]==board[5]and board[5]==board[7] and board[7]==player:
        return True
    return False
    
def checkDraw():
        for i in board.keys():
            if board[i]==" ":
                return False
        return True
    
def restartGame():
     button1["text"]=" "
     for button in buttons:
         button["text"]=" "
        
        
def play(event):
    global turn
    button=event.widget
    buttonText=str(button)
    clicked=buttonText[-1]
    print(clicked)
    #print(str(button))
    if clicked == "n":
        clicked=1
    else:
        clicked=int(clicked)
    
    if button["text"]==" ":
        if turn =="x":
            button["text"]="X"
            board[clicked]=turn
            if checkforwin(turn ):
                winninglabel=Label(frame2,text=f"{turn} wins the games",font=("Arial",22))
                winninglabel.grid(row=3,column=1,columnspan =3)
                print(turn ,"Wins the game")
                print("Game Over")
            turn="0"
                 
        else:
            button["text"]="0"
            board[clicked]=turn
            if checkforwin(turn ):
                winninglabel=Label(frame2,text=f"{turn} wins the games",font=("Arial",22))
                winninglabel.grid(row=3,column=1,columnspan =3)
                print(turn ,"Wins the game")
                print("Game Over")
            turn="x"
        if checkDraw():
            winninglabel=Label(frame2,text=f"GameDraw",font=("Arial",22))
            winninglabel.grid(row=3,column=1,columnspan =3)
            print("Game tie")
               
            
    print(board)    
  
    
# Tic-tac-toe board
#first row
button1=Button(frame2, text=" ",width =4 ,height=2,font=("Arial",35))
button1.grid(row =0,column= 0)
button1.bind("<Button>",play)
button2=Button(frame2, text=" ",width =4 ,height=2,font=("Arial",35))
button2.grid(row =0,column= 1)
button2.bind("<Button>",play)
button3=Button(frame2, text=" ",width =4 ,height=2,font=("Arial",35))
button3.grid(row =0,column= 2)
button3.bind("<Button>",play)
#Seond row
button4=Button(frame2, text=" ",width =4 ,height=2,font=("Arial",35))
button4.grid(row =1,column= 0)
button4.bind("<Button>",play)
button5=Button(frame2, text=" ",width =4 ,height=2,font=("Arial",35))
button5.grid(row =1,column= 1)
button5.bind("<Button>",play)
button6=Button(frame2, text=" " ,width =4 ,height=2,font=("Arial",35))
button6.grid(row =1,column= 2)
button6.bind("<Button>",play)
#third row
button7=Button(frame2, text=" ",width =4 ,height=2,font=("Arial",35))
button7.grid(row =2,column= 0)
button7.bind("<Button>",play)
button8=Button(frame2, text=" ",width =4 ,height=2,font=("Arial",35))
button8.grid(row =2,column= 1)
button8.bind("<Button>",play)
button9=Button(frame2, text=" ",width =4 ,height=2,font=("Arial",35))
button9.grid(row =2,column= 2)
button9.bind("<Button>",play)
restartbutton=Button(frame2,text="Restart Game",width=10,height=3,font=("Arial",10),bg ='lightgreen',command=restartGame)
restartbutton.grid(row=4,column=0,columnspan=3)
buttons=[button1,button2,button3,button4,button5,button6,button7,button8,button9]
root.mainloop()

