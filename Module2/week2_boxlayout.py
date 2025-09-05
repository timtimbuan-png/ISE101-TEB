from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class BoxLayoutDemo(App):
    def build(self):
       
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)
        layout.add_widget(Button(text="Button 1"))
        layout.add_widget(Button(text="Button 2"))
        layout.add_widget(Button(text="Button 3"))
        return layout

if __name__ == "__main__":
    BoxLayoutDemo().run()
