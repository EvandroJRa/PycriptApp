from kivy.app import App
from views.view_manager import ViewManager

class EncryptApp(App):
    def build(self):
        return ViewManager()  # Gerencia as telas

if __name__ == "__main__":
    EncryptApp().run()
