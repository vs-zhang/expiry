import kivy

kivy.require('1.9.1')  # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        return Label(text='All set before expired.')


if __name__ == '__main__':
    MyApp().run()
