
from kivy.app import App
from kivy.uix.textinput import TextInput


def build():
	text_input = TextInput()
	text_input.text = "Entrada de dados"
	text_input.italic = True
	text_input.font_size = 50
	return text_input


app = App()
app.build = build
app.run()
