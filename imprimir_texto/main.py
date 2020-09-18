
from kivy.app import App
from kivy.uix.label import Label


def build():
	label = Label()
	label.text = "Imprimindo texto"
	label.italic = True
	label.font_size = 50
	return label


app = App()
app.build = build
app.run()
