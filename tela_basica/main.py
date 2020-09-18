
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

from kivy.core.window import Window


text_input = TextInput(text='Teste')
button = Button(text='Click aqui')


def click():
	print(text_input.text)


def build():
	layout = FloatLayout()
	
	text_input.size_hint = None, None
	text_input.height = 300
	text_input.width = 400
	text_input.x = 60
	text_input.y = 250
	layout.add_widget(text_input)
	
	button.size_hint = None, None
	button.height = 50
	button.width = 200
	button.x = 150
	button.y = 170
	button.on_press = click
	layout.add_widget(button)
	return layout


app = App()
app.title = 'Studio Photo'

Window.size = 520, 600

app.build = build
app.run()
