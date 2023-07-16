from flask import Flask, render_template, request
from pusher import Pusher

app = Flask(__name__)
pusher = Pusher(app_id=u'1231224', key=u'65b42d90558d920dd849', secret=u'1ed6e951420633e4fd10', cluster=u'us2')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/nomedatela')
def nomedatela():
	return render_template('nome_da_tela.html')

@app.route('/mensagem')
def mensagem():
	return render_template('mensagem.html')

@app.route('/playstoploop')
def playstoploop():
	return render_template('playstoploop.html')

@app.route('/numinput')
def numinput():
	return render_template('numinput.html')

@app.route('/adjustnomedatela', methods=['POST'])
def adjustnomedatela():
	data = request.form
	pusher.trigger(u'nomedatela', u'send', {
		u'nomedatela': data['nomedatela']
	})
	return "Nome da tela alterado"

@app.route('/adjustmensagem', methods=['POST'])
def adjustmensagem():
	data = request.form
	pusher.trigger(u'mensagem', u'send', {
		u'mensagem': data['mensagem']
	})
	return "Mensagem Enviada"

@app.route('/adjustplaystoploop', methods=['POST'])
def adjustplaystoploop():
	data = request.form
	pusher.trigger(u'playstoploop', u'send', {
		u'playstoploop': data['playstoploop']
	})
	return "Imagem Alterada"

@app.route('/adjustnuminput', methods=['POST'])
def adjustnuminput():
	data = request.form
	pusher.trigger(u'numinput', u'send', {
		u'numinput': data['numinput']
	})
	return "Numero de inputs Alterado"

if __name__ == '__main__':
	app.run(debug=True)

