from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class NestedLayoutDemo(App):
    def build(self):
        main_layout = GridLayout(cols=2, spacing=10, padding=10)

        main_layout.add_widget(Button(text="Grid Button 1"))

        box_layout = BoxLayout(orientation='vertical', spacing=10)
        box_layout.add_widget(Button(text="Box Button 1"))
        box_layout.add_widget(Button(text="Box Button 2"))
        box_layout.add_widget(Button(text="Box Button 3"))

        main_layout.add_widget(box_layout)

        return main_layout

if __name__ == "__main__":
    NestedLayoutDemo().run()
