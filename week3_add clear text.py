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
        
        submit_button = Button(text="Submit")
        clear_button = Button(text="Clear")
        
        submit_button.bind(on_press=self.on_button_click)
        clear_button.bind(on_press=self.on_clear_click)
        
        layout.add_widget(self.label)
        layout.add_widget(self.text_input)
        layout.add_widget(submit_button)
        layout.add_widget(clear_button)
        
        return layout

    def on_button_click(self, instance):
        name = self.text_input.text.strip()
        if name:
            self.label.text = f"Hello, {name}!"
        else:
            self.label.text = "Please enter a name."

    def on_clear_click(self, instance):
        self.text_input.text = ""
        self.label.text = "Enter your name below:" 

if __name__ == "__main__":
    WidgetDemo().run()
