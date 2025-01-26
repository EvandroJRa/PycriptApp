import sys
print("Caminhos de busca do Python:")
print(sys.path)

import os
from kivy.app import App
from kivy.uix.label import Label
from views.view_manager import ViewManager

# Adiciona o caminho base ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from kivy.app import App
from views.view_manager import ViewManager

class EncryptApp(App):
    def build(self):
        return ViewManager()  # Gerencia as telas

if __name__ == "__main__":
    EncryptApp().run()