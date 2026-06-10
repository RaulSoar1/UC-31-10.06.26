from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

@app.route('/')
def index():
    nome = request.cookies.get('nome')
    email = request.cookies.get('email')
    tema = request.cookies.get('tema', 'claro')

    return render_template(
        'index.html',
        nome=nome,
        email=email,
        tema=tema
    )

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']

        resposta = make_response(redirect('/'))
        resposta.set_cookie('nome', nome, max_age=60*60*24*30)
        resposta.set_cookie('email', email, max_age=60*60*24*30)

        return resposta

    return render_template('cadastro.html')

@app.route('/tema/<modo>')
def tema(modo):
    resposta = make_response(redirect('/'))
    resposta.set_cookie('tema', modo, max_age=60*60*24*30)
    return resposta

if __name__ == '__main__':
    app.run(debug=True)