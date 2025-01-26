import sys
import os
from kivy.app import App

# Adiciona o caminho base ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Imports ajustados
from views.view_manager import ViewManager  # Use ViewManager para gerenciar as telas

class EncryptApp(App):
    def build(self):
        return ViewManager()  # Define o layout principal

if __name__ == "__main__":
    print("Caminhos de busca do Python:")
    for path in sys.path:
        print(path)

    # Executa o aplicativo
    EncryptApp().run()
