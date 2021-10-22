from flask import Flask, render_template

app = Flask(__name__) #Objeto que irá representar a aplicação

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
        


@app.route('/')
def home():
    jogo1 = Jogo('Mario Kart', 'Aventura','PS')
    jogo2 = Jogo('New World', 'MMORPG','PC')
    jogo3 = Jogo('COD', 'FPS','PS/PC')
    jogo4 = Jogo('Civilization', 'rts','PS/pc')
    lista = [jogo1,jogo2,jogo3,jogo4]

    return render_template('list.html',titulo='Jogos', jogos=lista)

app.run() #rodando aplicação