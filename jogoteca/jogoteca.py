from flask import Flask, render_template

app = Flask(__name__) #Objeto que irá representar a aplicação
@app.route('/')
def home():
    return render_template('list.html')

app.run() #rodando aplicação