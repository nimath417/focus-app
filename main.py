from kivy.app import App
from kivy.uix.label import Label

class FocusApp(App):
    def build(self):
        return Label(text="Hello from Focus App")

FocusApp().run()
