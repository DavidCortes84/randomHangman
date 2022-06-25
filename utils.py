from window import Window

def foundIndexes(word:str,letter:str) -> list[int]:
    indexes = []
    currentIndex = word.find(letter)

    while currentIndex != -1:
        indexes.append(currentIndex)
        currentIndex = word.find(letter,currentIndex+1)

    return indexes

def checkGameOver(lifes,word):
        if not lifes:
            retry = Window.askForReplay(word)
            if retry:
                pass
        
        # is_all_shown = len(list(filter(lambda x: x.hidden == True,self.labels))) == 0
        
        # if is_all_shown:
        #     retry = askretrycancel(
        #         'Congratilations',
        #         'Completaste la palabra: {} con solo {} errores'.format(self.word,10 - self.lifes))
        #     if retry:
        #         self.restart()