import sys
import os
from kivy.app import App

# Adiciona o caminho base ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importa o novo layout principal
from file_ExplorerApp import FileExplorerApp

class EncryptApp(App):
    def build(self):
        # Define o layout principal como FileExplorerApp
        return FileExplorerApp()

if __name__ == "__main__":
    print("Caminhos de busca do Python:")
    for path in sys.path:
        print(path)

    # Executa o aplicativo
    EncryptApp().run()
