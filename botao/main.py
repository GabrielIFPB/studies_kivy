
from kivy.app import App
from kivy.uix.button import Button


def click():
	print('O botão foi clicado')


def build():
	button = Button()
	button.text = "Imprimindo texto"
	button.italic = True
	button.font_size = 50
	button.on_press = click     # associando função de click ao button
	return button


app = App()
app.build = build
app.run()
