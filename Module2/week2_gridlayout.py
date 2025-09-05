from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class GridLayoutDemo(App):
    def build(self):
        layout = GridLayout(cols=3, spacing=10, padding=10)  
        for i in range(1, 10):  
            layout.add_widget(Button(text=f"Button {i}"))
        return layout

if __name__ == "__main__":
    GridLayoutDemo().run()
