from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):
    def build(selfTEB):
        selfTEB.operators = {"+", "-", "*", "/"}
        selfTEB.last_was_operator = False

        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        selfTEB.display = TextInput(
            text="0",
            readonly=True,
            halign="right",
            font_size=48,
            background_color=(0.9, 0.9, 0.9, 1),
            foreground_color=(0, 0, 0, 1),
            multiline=False,
        )
        main_layout.add_widget(selfTEB.display)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", "Clear", "=", "+"],
        ]

        button_grid = GridLayout(cols=4, spacing=10, size_hint=(1, 0.8))

        for row in buttons:
            for label in row:
                btn = Button(text=label, font_size=32)
                btn.bind(on_press=selfTEB.on_button_press)
                button_grid.add_widget(btn)

        main_layout.add_widget(button_grid)

        return main_layout

    def on_button_press(self, instance):
        text = instance.text
        current = self.display.text

        if text == "Clear":
            self.display.text = "0"
            self.last_was_operator = False

        elif text == "=":
         
            pass

        elif text in self.operators:
            if current[-1] in self.operators:
                
                self.display.text = current[:-1] + text
            else:
                self.display.text += text
            self.last_was_operator = True

        else:  
            if current == "0" or self.last_was_operator or current == "Error":
                self.display.text = text
            else:
                self.display.text += text
            self.last_was_operator = False


if __name__ == "__main__":
    CalculatorApp().run()




