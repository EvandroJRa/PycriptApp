import sys
import os

# Adicionar caminho do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from kivy.uix.boxlayout import BoxLayout
from controllers.file_controller import FileController

class ViewManager(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = FileController()

    def encrypt_file(self, files, password):
        if not files or not password:
            print("Selecione um arquivo e insira uma senha!")
            return

        file_path = files[0]
        try:
            self.controller.encrypt(file_path, password)
            print("Arquivo criptografado com sucesso!")
        except Exception as e:
            print(f"Erro ao criptografar: {e}")

    def decrypt_file(self, files, password):
        if not files or not password:
            print("Selecione um arquivo e insira uma senha!")
            return

        file_path = files[0]
        try:
            self.controller.decrypt(file_path, password)
            print("Arquivo descriptografado com sucesso!")
        except Exception as e:
            print(f"Erro ao descriptografar: {e}")


