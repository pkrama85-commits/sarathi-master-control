from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle

class MyApp(App):
    def build(self):
        layout = BoxLayout()
        with layout.canvas:
            Color(0, 0, 0, 1)  # Set background to black
            self.rect = Rectangle(size=(300, 300), pos=(0, 0))  # You can adjust size/position as needed
        label = Label(text='SARATHI SYSTEM ACTIVE', color=(1, 1, 1, 1))  # White text
        layout.add_widget(label)
        return layout

if __name__ == '__main__':
    MyApp().run()