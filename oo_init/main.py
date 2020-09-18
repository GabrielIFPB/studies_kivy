from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class Main(App):
	
	title = 'Photo Studio'
	
	def build(self):
		return FloatLayout()


main = Main()
main.run()
