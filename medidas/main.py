
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class RootWidget(FloatLayout):
	pass


class Medida(App):
	
	title = 'Photo Studio'
	
	def build(self):
		return RootWidget()


main = Medida()
main.run()
