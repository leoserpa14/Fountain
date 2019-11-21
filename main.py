# -*- coding: utf-8 -*-

from kivy.config import Config
Config.read("config.ini")

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

sm = ScreenManager()


class Menu1(Screen):
	pass
class Menu2(Screen):
	pass
class Menu3(Screen):
	pass
class Menu4(Screen):
	pass
class Menu5(Screen):
	pass

class IdeaApp(App):
	def build(self):

		menu1 = Menu1(name='menu1')
		menu2 = Menu2(name='menu2')
		menu3 = Menu3(name='menu3')
		menu4 = Menu4(name='menu4')
		menu5 = Menu5(name='menu5')

		sm.add_widget(menu1)
		sm.add_widget(menu2)
		sm.add_widget(menu3)
		sm.add_widget(menu4)
		sm.add_widget(menu5)

		return sm


IdeaApp().run()