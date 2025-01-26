import os
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from controllers.file_controller import FileController


class ViewManager(BoxLayout):
    def __init__(self, **kwargs):
        print("Inicializando ViewManager...")
        super().__init__(orientation='vertical', **kwargs)

        self.padding = 20
        self.spacing = 10

        self.controller = FileController()

        # Define a pasta raiz do sistema operacional
        root_path = self.get_root_path()
        print(f"Pasta raiz configurada: {root_path}")

        # FileChooser para seleção de múltiplos arquivos e pastas
        self.file_chooser = FileChooserIconView(
            path=root_path,  # Inicia na pasta raiz
            show_hidden=True,
            size_hint=(1, 0.6),
            dirselect=False,  # Inicialmente seleciona arquivos
            multiselect=True  # Ativa seleção múltipla
        )
        self.add_widget(self.file_chooser)

        # Botão para alternar entre seleção de arquivos e pastas
        self.toggle_button = Button(
            text="Alternar para Seleção de Pastas",
            size_hint=(1, None),
            height=50
        )
        self.toggle_button.bind(on_press=self.toggle_selection_mode)
        self.add_widget(self.toggle_button)

        # Campo de entrada para senha
        self.add_widget(Label(text="Senha:", size_hint=(1, None), height=30))
        self.password_input = TextInput(password=True, multiline=False, size_hint=(1, None), height=40)
        self.add_widget(self.password_input)

        # Botão para criptografar seleção
        self.encrypt_file_button = Button(text="Criptografar Seleção", size_hint=(1, None), height=50)
        self.encrypt_file_button.bind(on_press=self.encrypt_selection)
        self.add_widget(self.encrypt_file_button)

        # Botão para descriptografar seleção
        self.decrypt_file_button = Button(text="Descriptografar Seleção", size_hint=(1, None), height=50)
        self.decrypt_file_button.bind(on_press=self.decrypt_selection)
        self.add_widget(self.decrypt_file_button)

    def get_root_path(self):
        """
        Retorna a pasta raiz do sistema operacional.
        """
        if os.name == 'nt':  # Windows
            return "C:/"
        else:  # Linux/Mac
            return "/"

    def toggle_selection_mode(self, instance):
        """
        Alterna entre seleção de arquivos e pastas.
        """
        if self.file_chooser.dirselect:
            # Trocar para seleção de arquivos
            self.file_chooser.dirselect = False
            self.toggle_button.text = "Alternar para Seleção de Pastas"
            print("Modo de seleção: Arquivos")
        else:
            # Trocar para seleção de pastas
            self.file_chooser.dirselect = True
            self.toggle_button.text = "Alternar para Seleção de Arquivos"
            print("Modo de seleção: Pastas")

    def encrypt_selection(self, instance):
        """
        Criptografa os itens selecionados (arquivos ou pastas).
        """
        selected_items = self.file_chooser.selection
        password = self.password_input.text
        if not selected_items:
            self.show_popup("Erro", "Nenhum item selecionado!")
            return
        if not password:
            self.show_popup("Erro", "Digite uma senha para criptografar!")
            return

        try:
            for item in selected_items:
                if os.path.isdir(item):
                    # Criptografar todos os arquivos na pasta
                    for root, _, files in os.walk(item):
                        for file in files:
                            file_path = os.path.join(root, file)
                            self.controller.encrypt(file_path, password)
                else:
                    # Criptografar arquivo único
                    self.controller.encrypt(item, password)
            self.show_popup("Sucesso", "Itens selecionados criptografados com sucesso!")
        except Exception as e:
            self.show_popup("Erro", f"Erro ao criptografar: {e}")

    def decrypt_selection(self, instance):
        """
        Descriptografa os itens selecionados (arquivos ou pastas).
        """
        selected_items = self.file_chooser.selection
        password = self.password_input.text
        if not selected_items:
            self.show_popup("Erro", "Nenhum item selecionado!")
            return
        if not password:
            self.show_popup("Erro", "Digite uma senha para descriptografar!")
            return

        try:
            for item in selected_items:
                if os.path.isdir(item):
                    # Descriptografar todos os arquivos na pasta
                    for root, _, files in os.walk(item):
                        for file in files:
                            file_path = os.path.join(root, file)
                            self.controller.decrypt(file_path, password)
                else:
                    # Descriptografar arquivo único
                    self.controller.decrypt(item, password)
            self.show_popup("Sucesso", "Itens selecionados descriptografados com sucesso!")
        except Exception as e:
            self.show_popup("Erro", f"Erro ao descriptografar: {e}")

    def show_popup(self, title, message):
        """
        Exibe um popup com título e mensagem.
        """
        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.8, 0.4)
        )
        popup.open()
