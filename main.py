from kivy.app import App
from kivy.uix.label import Label

class SarathiApp(App):
    def build(self):
        # यह आपके ऐप की मुख्य स्क्रीन है
        return Label(text='🔱 SARATHI MASTER CONTROL ACTIVE 🔱', font_size='30sp')

if __name__ == '__main__':
    SarathiApp().run()