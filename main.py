from kivy.app import App
from kivy.uix.label import Label


class BGereApp(App):
    def build(self):
        return Label(
            text="B-Gère\nBienvenue",
            font_size="32sp",
            halign="center",
        )


BGereApp().run()