from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class WidgetDemo(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        self.label = Label(text="Enter your name below:")
        self.text_input = TextInput(hint_text="Type here")
        button = Button(text="Submit")
        
        button.bind(on_press=self.on_button_click)
        layout.add_widget(self.label)
        layout.add_widget(self.text_input)
        layout.add_widget(button)
        return layout

    def on_button_click(self, instance):
        name = self.text_input.text.strip()
        if name:
            self.label.text = f"Hello, {name}!"
        else:
            self.label.text = "Please enter a name."

if __name__ == "__main__":
    WidgetDemo().run()
