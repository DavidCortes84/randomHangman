from window import Window
import requests

URL = 'https://palabras-aleatorias-public-api.herokuapp.com/random'
res = requests.get(URL)
random_word = res.json().get("body").get("Word")
containsEnhie = random_word.find("ñ")
while containsEnhie != -1 or len(random_word.split(' ')) > 1:
    res = requests.get(URL)
    random_word = res.json().get("body").get("Word")
total_lifes = 10
print(random_word)

window = Window("HANGMAN","500x570")
window.layout(random_word)
 
window.window.mainloop()