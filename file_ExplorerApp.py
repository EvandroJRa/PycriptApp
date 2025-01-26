import os
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.app import App


class FileExplorerApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.padding = 20
        self.spacing = 10

        # Define a pasta raiz do sistema operacional
        self.root_path = self.get_root_path()

        # Variável para armazenar o modo selecionado
        self.mode = "arquivos"  # Modo inicial: "arquivos" ou "pasta"

        # Adiciona os botões de navegação
        self.add_navigation_buttons()

        # FileChooser para seleção de múltiplos arquivos e pastas
        self.file_chooser = FileChooserIconView(
            path=self.root_path,
            show_hidden=True,
            size_hint=(1, 0.6),
            dirselect=False,  # Inicialmente seleciona arquivos
            multiselect=True
        )
        self.add_widget(self.file_chooser)

        # Botão para alternar entre criptografia de arquivos ou pastas
        self.toggle_mode_button = Button(
            text="Modo: Criptografar Arquivos",
            size_hint=(1, None),
            height=50
        )
        self.toggle_mode_button.bind(on_press=self.toggle_mode)
        self.add_widget(self.toggle_mode_button)

        # Campo de entrada para senha
        self.add_widget(Label(text="Senha:", size_hint=(1, None), height=30))
        self.password_input = TextInput(password=True, multiline=False, size_hint=(1, None), height=40)
        self.add_widget(self.password_input)

        # Botão para criptografar seleção
        self.encrypt_button = Button(text="Criptografar Seleção", size_hint=(1, None), height=50)
        self.encrypt_button.bind(on_press=self.encrypt_selection)
        self.add_widget(self.encrypt_button)

    def get_root_path(self):
        """
        Retorna a pasta raiz do sistema operacional.
        """
        if os.name == 'nt':  # Windows
            return "C:/"
        else:  # Linux/Mac
            return "/"

    def add_navigation_buttons(self):
        """
        Adiciona botões para navegação (voltar e raiz).
        """
        navigation_box = BoxLayout(orientation='horizontal', size_hint=(1, None), height=40)
        self.add_widget(navigation_box)

        back_button = Button(text="Voltar", size_hint=(0.5, 1))
        back_button.bind(on_press=lambda *args: self.navigate_back())
        navigation_box.add_widget(back_button)

        root_button = Button(text="Ir para Raiz", size_hint=(0.5, 1))
        root_button.bind(on_press=lambda *args: self.navigate_to_root())
        navigation_box.add_widget(root_button)

    def navigate_back(self):
        """
        Volta para a pasta anterior no FileChooser.
        """
        current_path = self.file_chooser.path
        parent_path = os.path.dirname(current_path)
        if os.path.exists(parent_path):
            self.file_chooser.path = parent_path

    def navigate_to_root(self):
        """
        Vai para a pasta raiz do sistema operacional.
        """
        self.file_chooser.path = self.root_path

    def toggle_mode(self, instance):
        """
        Alterna entre os modos de criptografia: arquivos ou pasta inteira.
        """
        if self.mode == "arquivos":
            self.mode = "pasta"
            self.file_chooser.dirselect = True
            self.toggle_mode_button.text = "Modo: Criptografar Pasta"
        else:
            self.mode = "arquivos"
            self.file_chooser.dirselect = False
            self.toggle_mode_button.text = "Modo: Criptografar Arquivos"

    def encrypt_selection(self, instance):
        """
        Criptografa a seleção com base no modo escolhido.
        """
        password = self.password_input.text
        if not password:
            self.show_popup("Erro", "Digite uma senha para criptografar!")
            return

        if self.mode == "arquivos":
            self.encrypt_files()
        elif self.mode == "pasta":
            self.encrypt_folder()

    def encrypt_files(self):
        """
        Criptografa os arquivos selecionados no FileChooser.
        """
        selected_files = self.file_chooser.selection
        if not selected_files:
            self.show_popup("Erro", "Nenhum arquivo selecionado!")
            return

        try:
            for file_path in selected_files:
                print(f"Criptografando arquivo: {file_path}")
                # Chamada fictícia para criptografia
            self.show_popup("Sucesso", "Arquivos criptografados com sucesso!")
        except Exception as e:
            self.show_popup("Erro", f"Erro ao criptografar arquivos: {e}")

    def encrypt_folder(self):
        """
        Criptografa todos os arquivos em uma pasta selecionada.
        """
        selected_folder = self.file_chooser.selection[0] if self.file_chooser.selection else None
        if not selected_folder or not os.path.isdir(selected_folder):
            self.show_popup("Erro", "Nenhuma pasta válida selecionada!")
            return

        try:
            for root, _, files in os.walk(selected_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    print(f"Criptografando arquivo na pasta: {file_path}")
                    # Chamada fictícia para criptografia
            self.show_popup("Sucesso", "Pasta criptografada com sucesso!")
        except Exception as e:
            self.show_popup("Erro", f"Erro ao criptografar pasta: {e}")

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


class MyApp(App):
    def build(self):
        return FileExplorerApp()


if __name__ == "__main__":
    MyApp().run()
