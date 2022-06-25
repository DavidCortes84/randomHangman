from tkinter import Tk,Frame,Label,Button,Canvas
from tkinter.messagebox import askretrycancel
from functools import partial
from utils import foundIndexes

class Window:
    def __init__(self,title,dimensions):
        self.window = Tk()
        self.window.title(title)
        self.canvasWrapper = Frame(self.window)
        # self.lifes = lifes
        self.canvasLifes = Canvas(self.canvasWrapper,width=400,height=30,bg="#000")
        self.canvas = Canvas(self.canvasWrapper,width=400,height=300,bg="#000")
        self.canvasLifes.pack()
        self.canvas.pack()
        self.wordWrapper = Frame(self.window)
        self.lettersWrapper = Frame(self.window)
        # self.word = word
        self.labels = []

        self.window.geometry(dimensions)

    def layout(self,random_word):
        # hangman draw
        self.canvasLifes.create_text(50,20,text='Lifes {}'.format(self.lifes),fill="#fff",font=('Ubuntu',18))
        self.canvasWrapper.pack()
        # hidden word
        for i,l in enumerate(random_word):
            label = Label(self.wordWrapper,text=l.upper())
            label.hidden = True
            self.labels.append(label)
            label.config(bg='#fff',fg='#fff',borderwidth=3,relief="sunken",width=2,height=2,font=('Ubuntu',18))
            label.grid(row=0,column=i)
        self.wordWrapper.pack()

        # btns with alphabet letters
        row,column = 0,0
        for v in range(65,91):
            btn = Button(
                self.lettersWrapper,
                text=chr(v),
                width=2,
                height=2
            )
            fun = partial(self.showLetter,chr(v),btn)
            btn.config(command=fun)
            column = column+1
            btn.grid(row=row,column=column)
            column = column % 10
            row = row+1 if not column else row
        self.lettersWrapper.pack()

    def showLetter(self,letter,btn,function):
        indexes = foundIndexes(self.word,letter.lower())
        if indexes:
            for i in indexes:
                self.labels[i].config(fg="#000")
                self.labels[i].hidden = False
            # btn.config(bg="#0f0",fg="#000")
            btn["state"] = "disable"
        else:
            self.lifes = self.lifes-1
            self.drawPart()
        self.checkGameOver()

    @staticmethod
    def askForReplayWinner(word,isWinner):
        retry = None
        if isWinner:
            retry = askretrycancel(
                'CONGRATS!!!',
                'You found the correct word {}'.format(word))
        else:
            retry = askretrycancel(
                'GAME OVER',
                'You did not guess the word {}'.format(word))
        return retry
    
    def restart(self):
        pass

    def drawPart(self):
        self.canvasLifes.delete("all")
        self.canvasLifes.create_text(50,20,text='Lifes {}'.format(self.lifes),fill="#fff",font=('Ubuntu',18))
        dictionary_parts ={
            0:
                self.canvas.create_line(200,200,220,240,fill="#fff",width=5)
            ,1:
                self.canvas.create_line(200,200,180,240,fill="#fff",width=5)
            ,2:
                self.canvas.create_line(200,120,220,160,fill="#fff",width=5)
            ,3:
                self.canvas.create_line(200,120,180,160,fill="#fff",width=5)
            ,4:
                self.canvas.create_line(200,120,200,200,fill="#fff",width=4)
            ,5:
                self.canvas.create_oval(180,80,220,120,fill="#fff")
            ,6:
                self.canvas.create_line(200,12,200,80,fill="#fff",width=5)
            ,7:
                self.canvas.create_line(350,12,200,12,fill="#fff",width=5)
            ,8:
                self.canvas.create_line(350,275,350,10,fill="#fff",width=5)
            ,9:
                self.canvas.create_line(0,280,400,280,fill="#fff",width=10)
            }
        counter = 0
        while counter <= part:
            dictionary_parts[counter]()
            counter = counter+1