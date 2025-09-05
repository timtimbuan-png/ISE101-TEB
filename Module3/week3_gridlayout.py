from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class GridDemo(App):
    def build(self):
        layout = GridLayout(cols=3, spacing=5, padding=5)  
        for i in range(1, 10): 
            btn = Button(text=f"Button {i}")
            btn.bind(on_press=self.on_press_button)
            layout.add_widget(btn)
        return layout

    def on_press_button(self, instance):
        print(f"You clicked: {instance.text}")

if __name__ == "__main__":
    GridDemo().run()
